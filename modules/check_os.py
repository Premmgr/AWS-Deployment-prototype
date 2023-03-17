from modules import color
import platform, sys
# runtime os detector --------------------------------------
machine_os = []
def check_host_os():
    detected_os = platform.system()
    if "Linux" in detected_os:
        machine_os.append("linux")
    if "Windows" in detected_os:
        machine_os.append("windows")
check_host_os()

if "linux" in machine_os:
    print(f'{color.green}script is running on linux machine{color.ec}')
elif "windows" in machine_os:
    print(f'{color.green}script is running on windows machine{color.ec}')
else:
    print(f'{color.red}script running on unknown os{color.ec}')
    
    sys.exit(1)
# end of os detector ----------------------------------------