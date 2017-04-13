def primes_sieve(num):
    limitn = num+1
    not_prime = set()
    primes = ''
    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes+=(str(i) +" ")
    return primes

import socket

s = socket.socket()         
host = socket.gethostname()
port = 21000               


print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))        
s.listen(5)                

while True:
  c, addr = s.accept()     
  print 'Got connection from', addr
  msg = c.recv(1024).decode()
  msg=int(msg)
  msg=primes_sieve(msg)
  print addr, ' >> ', msg
  c.send(msg);
  c.close()   

