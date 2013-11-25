from sage.all import*
import binascii
file1=open('2_enc.dat','r')
f=file1.read()
file1=open('file.txt','r')
key=file1.read()


n=Integer(int(key,16))
e=Integer(3)
i=f.strip().encode('hex')
f=Integer(int(i,16))
ci = f

print "Computing..."
while True:
   try:
    m = f.nth_root(e)
    p=power_mod(m,e,n)
    if p == ci:
        break
   except Exception:
     f+=n

m=hex(m).replace('0x','')
ms=str(0)+str(m)
#print ms
msg=ms.decode("hex")
print "Message is:",  msg
