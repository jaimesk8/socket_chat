#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:49:57 2023

@author: jaime
"""

import socket 
import threading 

host = '127.0.0.1'
port = 55000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host,port))
server.listen()
print(f'Servidor está conectado com o {host}:{port}')

#criação de lista para armazenar (array vazio) 
clients = []
usernames = []

def broadcast(message, _client): 
    for client in clients:
        if client != _client:
            client.send(message)

def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
            
        except:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f'Chatbot: {username} disconected'.encode("utf-8"))
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break
        
def receive_connections():
    while True:
        client, address = server.accept()
        
        client.send("@username".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        
        clients.append(client)
        usernames.append(username)
        
        print(f"{username} is connected with {str(address)}")
        
        message = f"Chatbot: {username} joined the chat!".encode('utf-8')
        broadcast (message, client)
        client.send("Connected to server".encode('utf-8'))
        
        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()
        
receive_connections()
            
            
            
            
            
        
