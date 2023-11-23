class MathServerCommunicationThread(Thread):
	def __init__(self, conn, addr):
		Thread.__init__(self)
	self.conn = conn
	self.addr = addr

def run(self):
	print("{} connected with back port {}".format(self.addr[0], self.addr[1]))
	self.conn.sendall("Simple Math Server developed by LAHTP \n\nGive any math expressions, and I will answer you :) \n\n$ ".encode())

	p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	output = ProcessOutputThread(p, self.conn)
	output.start()

	while not p.stdout.closed or not self.conn._closed:
		try:
			data = self.conn.recv(1024)
			if not data:
				break
			else:
				try:
					data = data.decode()
					query = data.strip()
					if query == 'quit' or query == 'exit':
						p.communicate(query.encode(), timeout=1)
						if p.poll() is not None:
							break
					query = query + '\n'
					p.stdin.write(query.encode())
					p.stdin.flush()
				except:
					pass
		except:
			pass
	self.conn.close()   
