#!/usr/bin/env python
import time
from sage.all import *
def rsa_func():
    cipher=Integer(int(raw_input("Enter the message(in numbers):")))
    n=25737144289
    e=13
    p=28649
    q=898361
    start_time=time.time()
    m=(q-1)*(p-1)
    d=inverse_mod(e,m)
    #cipher=power_mod(msg,e,n)
    msg=power_mod(cipher,d,n)
    end_time=time.time()-start_time
    print "Message:",msg
    return end_time

def main():
    end_time=rsa_func()
    print "time in seconds:", end_time
if __name__ == '__main__':
    main()
