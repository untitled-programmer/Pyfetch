import os
import socket
import requests
import platform
from colorama import Fore
import psutil

def get_local_ip():
            """Get local IP address"""
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip

def get_public_ip():
    """Get public IP address"""
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.exceptions.RequestException as e:
        return "Failed to retrieve public IP address"

def main():
    print("\nNetwork information:-----------------------------")
    print("- Local IP Address:", get_local_ip())
    print("- Public IP Address:", get_public_ip())

def system_info():
    # Get system information using platform module
    print("\nCPU Information:---------------------------------")
    print("- Processor:", platform.processor())
    print("- Architecture:", platform.machine())
    print("\nMemory Information:------------------------------")
    svmem = psutil.virtual_memory()
    print(f"- Total: {svmem.total / (1024 ** 3):.2f} GB")
    print(f"- Available: {svmem.available / (1024 ** 3):.2f} GB")
    print(f"- Used: {svmem.used / (1024 ** 3):.2f} GB")
    print(f"- Percentage: {svmem.percent}%")

def windows():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + "Microsoft")
    print("██     ██ ██ ███    ██ ██████   ██████  ██     ██ ███████")
    print("██     ██ ██ ████   ██ ██   ██ ██    ██ ██     ██ ██")
    print("██  █  ██ ██ ██ ██  ██ ██   ██ ██    ██ ██  █  ██ ███████")
    print("██ ███ ██ ██ ██  ██ ██ ██   ██ ██    ██ ██ ███ ██      ██")
    print(" ███ ███  ██ ██   ████ ██████   ██████   ███ ███  ███████")
    print(Fore.CYAN + "")
    main()
    system_info()
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

def gnulinux():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTGREEN_EX + " ██████  ███    ██ ██    ██     ██ ██      ██ ███    ██ ██    ██ ██   ██ ")
    print("██       ████   ██ ██    ██    ██  ██      ██ ████   ██ ██    ██  ██ ██  ")
    print("██   ███ ██ ██  ██ ██    ██   ██   ██      ██ ██ ██  ██ ██    ██   ███   ")
    print("██    ██ ██  ██ ██ ██    ██  ██    ██      ██ ██  ██ ██ ██    ██  ██ ██  ")
    print(" ██████  ██   ████  ██████  ██     ███████ ██ ██   ████  ██████  ██   ██ ")
    print(Fore.LIGHTGREEN_EX + "")
    main()
    system_info()
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')
                                                                        
os.system(windows() if os.name == "nt" else gnulinux())
