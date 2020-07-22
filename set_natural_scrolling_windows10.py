import winreg

REG_PATH = r"SOFTWARE\my_program\Settings"

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


# e.g. HID\VID_17EF&PID_600E\7&780CAA2&0&0000, found in Mouse Properties > Hardware > Properties > Details > Device Instance Path
MOUSE_PATH = input('Mouse device instance path: ')
sucess = set_reg(
    'Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\{MOUSE_PATH}\Device Parameters\FlipFlopWheel',
    '1'
)

print('FlipFlopWheel set to 1 success status: ' + sucess)
