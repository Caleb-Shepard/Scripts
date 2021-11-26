# Modified from Jason Go's response
# https://answers.microsoft.com/en-us/windows/forum/all/set-the-mouse-scroll-direction-to-reverse-natural/ede4ccc4-3846-4184-a86d-a028515040c0

$mode = Read-host "Set the scroll direction - Default [0] | Natural [1]: "
Get-PnpDevice -Class Mouse -PresentOnly -Status OK | ForEach-Object { "$($_.Name): $($_.DeviceID)"
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Enum\$($_.DeviceID)\Device Parameters" -Name FlipFlopWheel -Value $mode
"+--- Value of FlipFlopWheel is set to " + (Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Enum\$($_.DeviceID)\Device Parameters").FlipFlopWheel + "`n" }
