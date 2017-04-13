
import socket
     
host = socket.gethostname()

port = 21000               

print 'Connecting to ', host, port

while True:
  s = socket.socket() 
  s.connect((host, port))
  msg = raw_input('CLIENT >> ')
  s.send(msg)
  msg = s.recv(1024)
  print 'SERVER >> ', msg
  s.close() 
