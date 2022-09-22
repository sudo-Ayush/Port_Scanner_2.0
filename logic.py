#!/usr/bin/env python3

from colorama import Fore
import pyfiglet
import random
import socket

def banner():
    x = random.randint(0,11)
    
    if x == 0:
        result = pyfiglet.Figlet()
        print(Fore.BLUE + result.renderText("PORT SCANNER"))
    
    elif x == 1:
        result = pyfiglet.Figlet(font = "slant")
        print(Fore.CYAN + result.renderText("PORT SCANNER"))

    elif x == 2:
        result = pyfiglet.Figlet(font = "3-d")
        print(Fore.GREEN + result.renderText("PORT SCAN"))
        
    elif x == 3:
        result = pyfiglet.Figlet(font = "dotmatrix")
        print(Fore.MAGENTA + result.renderText("PORT SCAN"))
        
    elif x == 4:
        result = pyfiglet.Figlet(font = "5lineoblique")
        print(Fore.RED + result.renderText("PORT SCAN"))
        
    elif x == 5:
        result = pyfiglet.Figlet(font = "banner3-D")
        print(Fore.YELLOW + result.renderText("PORT SCAN"))
        
    elif x == 6:
        result = pyfiglet.Figlet(font = "doh")
        print(Fore.LIGHTBLUE_EX + result.renderText("PS"))
        
    elif x == 7:
        result = pyfiglet.Figlet(font = "isometric1")
        print(Fore.LIGHTCYAN_EX + result.renderText("PORT SCAN"))
        
    elif x == 8:
        result = pyfiglet.Figlet(font = "alligator")
        print(Fore.LIGHTYELLOW_EX + result.renderText("PORT SCAN"))
        
    elif x == 9:
        result = pyfiglet.Figlet(font = "bubble")
        print(Fore.LIGHTMAGENTA_EX + result.renderText("PORT SCANNER"))
        
    elif x == 10:
        result = pyfiglet.Figlet(font = "digital")
        print(Fore.LIGHTGREEN_EX + result.renderText("PORT SCANNER"))
        
    else:
        result = pyfiglet.Figlet(font = "bulbhead")
        print(Fore.LIGHTRED_EX + result.renderText("PORT SCANNER"))
        
def port_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
                
        if s.connect_ex((ip,port)):
            pass
                    
        else:
            print(f'{Fore.GREEN}[+] port {port} => service name {socket.getservbyport(port, "tcp")} is open')
            s.close()
                
    except socket.error:
        print(f"{Fore.RED}[-] port {port} => with UNKNOWN SERVICE is open | filtered")
            
    except:
        print(f"{Fore.RED}[-] Error : Server is not responding...!")
        
def validation(ip):
    try:    
        ip = ip.split('.')
        if len(ip) != 4:
            return
                
        for i in ip:
            if not isinstance(int(i), int):
                return
                    
            if int(i) < 0 or int(i) > 255:
                return
                
            if len(i) > 1:
                if int(i[0]) == 0:
                    return
                    
        if int(ip[0]) == 0:
            return
            
        if int(ip[-1]) == 0 or int(ip[-1]) == 255:
            return
        
        else:
            return True
    
    except ValueError:
        print(f"{Fore.RED}[-] Error values entered are not integer...!")
        exit()
