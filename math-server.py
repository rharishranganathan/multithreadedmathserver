import socket
from subprocess import Popen, STDOUT, PIPE
from threading import Thread
from comm_thread import MathServerCommunicationThread
from comm_thread import ProcessOutputThread

HOST = ''
PORT = 4444

def start_new_math_thread(conn, addr):
	t = MathServerCommunicationThread(conn, addr)
	t.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((HOST, PORT))
s.listen() # Look for calling bell
while True: # To accept many incoming connections. 
	conn, addr = s.accept() # Open door 
	start_new_math_thread(conn, addr)
s.close()
