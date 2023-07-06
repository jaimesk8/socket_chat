#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 21:15:09 2023

@author: jaime
"""

import socket
import threading 

username = input("Enter your username: ")

host = '127.0.0.1'
port = 55000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host,port))

def receivemessage():
    while True: 
        try:
            message = client.recv(1024).decode('utf-8')
            
            if message == "@username":
                client.send(username.encode('utf-8'))
                
            else:
                print(message)
            
        except:
            print("Ocurreu um erro!")
            client.close()
            break
            
def writemessage():
    while True:
        message = f"{username}: {input('')}"
        client.send(message.encode('utf-8'))
        
receive_thread = threading.Thread(target=receivemessage)
receive_thread.start() 

write_thread = threading.Thread(target=writemessage)
write_thread.start()



    
    
    
    
    
    
    
    
    
                