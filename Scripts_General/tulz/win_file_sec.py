import os
import sys
import ctypes as ctypes
from ctypes import wintypes as wintypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)  # interrupts, mem management, & i/o
advapi32 = ctypes.WinDLL('advapi32', use_last_error=True)  # Microsoft's "Advanced Services API"

# DEFINE CONSTANTS
ERROR_INVALID_FUNCTION  = 0x0001
ERROR_FILE_NOT_FOUND    = 0x0002
ERROR_PATH_NOT_FOUND    = 0x0003
ERROR_ACCESS_DENIED     = 0x0005
ERROR_SHARING_VIOLATION = 0x0020

SE_FILE_OBJECT_CODE                                    = 1
OWNER_SECURITY_INFORMATION                             = 0x00000001
GROUP_SECURITY_INFORMATION                             = 0x00000002
DISCRETIONARY_ACCESS_CONTROL_LIST_SECURITY_INFORMATION = 0x00000004
SYSTEM_ACCESS_CONTROL_LIST_SECURITY_INFORMATION        = 0x00000008
LABEL_SECURITY_INFORMATION                             = 0x00000010

# XOR SECURITY CODES TOGETHER, EXEMPT SYSTEM_ACCESS_CONTROL_LIST_SECURITY_INFORMATION
_DEFAULT_SECURITY_INFORMATION = (
    OWNER_SECURITY_INFORMATION                              |
    GROUP_SECURITY_INFORMATION                              |
    DISCRETIONARY_ACCESS_CONTROL_LIST_SECURITY_INFORMATION  |
    LABEL_SECURITY_INFORMATION
)

LONG_POINTER_DWORD = ctypes.POINTER(wintypes.DWORD)
SE_OBJECT_TYPE = wintypes.DWORD
SECURITY_INFORMATION = wintypes.DWORD
SECURITY_ID_TYPES = {
    1:  'User',
    2:  'Group',
    3:  'Domain',
    4:  'Alias',
    5:  'WellKnownGroup',
    6:  'DeletedAccount',
    7:  'Invalid',
    8:  'Unknown',
    9:  'Computer',
    10: 'Label'
}

''' Some information on win32 naming conventions
https://docs.microsoft.com/en-us/windows/desktop/stg/coding-style-conventions
LP generally means "Long Pointer"
DWORD means unsigned long
'''

class SecurityIdentifierNameUse(wintypes.DWORD):
    _security_identifier_types = SECURITY_ID_TYPES

    def __init__(self, value=None):
        if value is not None:
            if value not in self.security_identifier_types:
                raise ValueError('invalid SID type')
            wintypes.DWORD.__init__(value)

    def __str__(self):
        if self.value not in self._security_identifier_types:
            raise ValueError('invalid SID type')
        return self._security_identifier_types[self.value]

    def __repr__(self):
        return 'SecurityIdentifierNameUse(%s)' % self.value


# This was originally named PLOCAL and was renamed to PACL which is PortAccessControlList
# I'm not sure why the initial copy was made but my rename to PortAccess is my best guess
class PortAccessControlList(wintypes.LPVOID):
    _needs_free = False

    def __init__(self, value=None, needs_free=False):
        super(PortAccessControlList, self).__init__(value)
        self._needs_free = needs_free

    def __del__(self):
        if self and self._needs_free:
            kernel32.LocalFree(self)
            self._needs_free = False


class PhysicalSecurityIdentifier(PortAccessControlList):

    def __init__(self, value=None, needs_free=False):
        super(PhysicalSecurityIdentifier, self).__init__(value, needs_free)

    def __str__(self):
        if not self:
            raise ValueError('NULL pointer access')
        security_identifier = wintypes.LPWSTR()
        advapi32.ConvertSidToStringSidW(self, ctypes.byref(security_identifier))
        try:
            return security_identifier.value
        finally:
            if security_identifier:
                kernel32.LocalFree(security_identifier)


class PhysicalSecurityDescriptor(PortAccessControlList):

    def __init__(self, value=None, needs_free=False):
        super(PhysicalSecurityDescriptor, self).__init__(value, needs_free)
        self.physical_owner                                 = PhysicalSecurityIdentifier()
        self.physical_group                                 = PhysicalSecurityIdentifier()
        self.physical_discretionary_access_control_list     = PortAccessControlList()
        self.physical_system_access_control_list            = PortAccessControlList()
        # back references to keep this object alive
        self.physical_owner._SD                             = self
        self.physical_group._SD                             = self
        self.physical_discretionary_access_control_list._SD = self
        self.physical_system_access_control_list._SD        = self

    def get_owner(self, system_name=None):
        if not self or not self.physical_owner:
            raise ValueError('NULL pointer access')
        return look_up_account_security_identifier(self.physical_owner, system_name)

    def get_group(self, system_name=None):
        if not self or not self.physical_group:
            raise ValueError('NULL pointer access')
        return look_up_account_security_identifier(self.physical_group, system_name)


def _check_bool(result, func, args):
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

def look_up_account_security_identifier(security_identifier, system_name=None):
    buffer_size   = 256
    name          = ctypes.create_unicode_buffer(buffer_size)
    domain        = ctypes.create_unicode_buffer(buffer_size)
    c_char_name   = wintypes.DWORD(buffer_size)
    c_char_domain = wintypes.DWORD(buffer_size)
    security_identifier_type = SecurityIdentifierNameUse()
    advapi32.LookupAccountSidW(
        system_name,
        security_identifier,
        name,
        ctypes.byref(c_char_name),
        domain,
        ctypes.byref(c_char_domain),
        ctypes.byref(security_identifier_type)
    )
    return name.value, domain.value, security_identifier_type


def get_file_security(filename, request=_DEFAULT_SECURITY_INFORMATION):
    # N.B. This query may fail with ERROR_INVALID_FUNCTION
    # for some filesystems.
    physical_security_descriptor = PhysicalSecurityDescriptor(needs_free=True)
    error = advapi32.GetNamedSecurityInfoW(
        filename,
        SE_FILE_OBJECT_CODE,
        request,
        ctypes.byref(physical_security_descriptor.physical_owner),
        ctypes.byref(physical_security_descriptor.physical_group),
        ctypes.byref(physical_security_descriptor.physical_discretionary_access_control_list),
        ctypes.byref(physical_security_descriptor.physical_system_access_control_list),
        ctypes.byref(physical_security_descriptor)
    )
    if error != 0:
        raise ctypes.WinError(error)
        print(
            "Note: it's possible that your filesystem type \
             has triggered an ERROR_INVALID_FUNCTION"
        )
    return physical_security_descriptor

# msdn.microsoft.com/en-us/library/aa376399
advapi32.ConvertSidToStringSidW.errcheck = _check_bool
advapi32.ConvertSidToStringSidW.argtypes = (
    PhysicalSecurityIdentifier,         # _In_  Sid
    ctypes.POINTER(wintypes.LPWSTR)     # _Out_ StringSid
)

# msdn.microsoft.com/en-us/library/aa379166
PhysicalSecurityIdentifierNameUse   = ctypes.POINTER(SecurityIdentifierNameUse)
advapi32.LookupAccountSidW.errcheck = _check_bool
advapi32.LookupAccountSidW.argtypes = (
    wintypes.LPCWSTR,                   # _In_opt_  long Pointer System Name
    PhysicalSecurityIdentifier,         # _In_      Physical Security Identifier
    wintypes.LPCWSTR,                   # _Out_opt_ long pointer Name
    LONG_POINTER_DWORD,                 # _Inout_   C Character Name
    wintypes.LPCWSTR,                   # _Out_opt_ long Pointer Referenced Domain Name
    LONG_POINTER_DWORD,                 # _Inout_   C Character Referenced Domain Name
    PhysicalSecurityIdentifierNameUse   # _Out_     peUse
)

# msdn.microsoft.com/en-us/library/aa446645
advapi32.GetNamedSecurityInfoW.restype = wintypes.DWORD
advapi32.GetNamedSecurityInfoW.argtypes = (
    wintypes.LPWSTR,                             # _In_      physical_object_name
    SE_OBJECT_TYPE,                              # _In_      ObjectType
    SECURITY_INFORMATION,                        # _In_      SecurityInfo
    ctypes.POINTER(PhysicalSecurityIdentifier),  # _Out_opt_ physical_system_identifier_owner
    ctypes.POINTER(PhysicalSecurityIdentifier),  # _Out_opt_ physical_system_identifier_group
    ctypes.POINTER(PortAccessControlList),       # _Out_opt_ physical_discretionary_access_ctrl_list
    ctypes.POINTER(PortAccessControlList),       # _Out_opt_ physical_system_access_control_list
    ctypes.POINTER(PhysicalSecurityDescriptor)   # _Out_opt_ PhysicalSecurityDescriptor
)


def get_file_owner(file_name, as_string=False):
    if isinstance(file_name, bytes):
        if hasattr(os, 'fsdecode'):
            file_name = os.fsdecode(file_name)
        else:
            file_name = file_name.decode(sys.getfilesystemencoding())

    physical_security_descriptor = get_file_security(file_name)
    physical_owner_information   = physical_security_descriptor.get_owner()
    owner_name, owner_domain, owner_security_identifier_type = physical_owner_information

    if not as_string:  # return as tuple
        return (owner_name, owner_domain, owner_security_identifier_type)
    else:              # return as string
        return "{}\\{} ({})".format(owner_domain, owner_name, owner_security_identifier_type)

def get_file_security_identifier(file_name):
    if isinstance(file_name, bytes):
        if hasattr(os, 'fsdecode'):
            file_name = os.fsdecode(file_name)
        else:
            file_name = file_name.decode(sys.getfilesystemencoding())

    return get_file_security(file_name).physical_owner


if __name__ == '__main__':

    if len(sys.argv) < 2:
        script_name = os.path.basename(__file__)
        sys.exit('usage: {} file_name'.format(script_name))

    file_name = sys.argv[1]

    owner_name, owner_domain, owner_security_identifier_type = get_file_owner(file_name)
    print(file_name + " is owned by " + get_file_owner(file_name, True))
    print("SID: " + get_file_security_identifier(file_name))
