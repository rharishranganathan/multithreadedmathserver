import socket
from subprocess import Popen, STDOUT, PIPE
from threading import Thread
from comm_thread import MathServerCommunicationThread
from comm_thread import ProcessOutputThread

HOST = ''
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((HOST, PORT))
s.listen() # Look for calling bell
