#!/usr/bin/env python3

from concurrent.futures import thread
from os import system, name
from colorama import Fore
from logic import *
import threading
import colorama
import time

colorama.init(autoreset=True)

if name == 'nt':
    _ = system('cls')
    
else:
    _ = system('clear')
        
banner()

time.sleep(2)

if name == 'nt':
    _ = system('cls')
    
else:
    _ = system('clear')

print(f"{Fore.YELLOW}[*] Enter the domain name without <http> or <https> or simply enter IP Address...")
print(f"{Fore.YELLOW}[*] Example = github.com or 20.207.73.82")
print(f"{Fore.LIGHTCYAN_EX}--------------------------")
name = input(f"{Fore.BLUE}[*] Enter IP : ").strip()
ip = socket.gethostbyname(name)

if validation(ip) == True:
    rs = input(f"{Fore.BLUE}[*] Do you want to use defult ports scan[Y/N]: ").upper()

    if rs == "N":
        print(f"{Fore.LIGHTCYAN_EX}-----------------"+ "-" * len(ip))
        print(f"{Fore.LIGHTRED_EX}[*] Target IP : {ip}")
        print(f"{Fore.LIGHTCYAN_EX}-----------------"+ "-" * len(ip))

        start = int(input(f"{Fore.LIGHTBLUE_EX}[*] Enter start point : "))
        end = int(input(f"{Fore.LIGHTBLUE_EX}[*] Enter end point : "))
        print(f"{Fore.LIGHTMAGENTA_EX}-----------------"+ "-" * len(ip))
        ts = time.time()
                
        for port in range(start,end+1):
            time.sleep(0.009)
            thread = threading.Thread(target = port_scan, args = (ip, port))
            thread.start()
            
    elif rs == "Y":
        print(f"{Fore.LIGHTCYAN_EX}-----------------"+ "-" * len(ip))
        print(f"{Fore.LIGHTRED_EX}[*] Target IP : {ip}")
        print(f"{Fore.LIGHTCYAN_EX}-----------------"+ "-" * len(ip))
        
        l = [20,21,22,23,25,53,67,68,69,70,79,80,88,105,106,110,123,139,143,144,161,
            389,443,445,465,520,554,587,666,993,995,2222,2224,3360,3389,8000,8080]

        ts = time.time()
                    
        for port in l:
            time.sleep(0.009)
            thread = threading.Thread(target = port_scan, args = (ip, port))
            thread.start()
    else:
        print(f"{Fore.RED}[-] Invalid Selection...!")
        exit()

    done = (time.time()-ts)

    time.sleep(1)
    print(f"{Fore.LIGHTCYAN_EX}-------------------------"+ "-" * len(ip))
    print(f'{Fore.LIGHTMAGENTA_EX}[*] Finished | Scanned in {round(done,2)} seconds')
    exit()
   
else:
    print(f"{Fore.RED}[-] Invalid IP Address...!")
