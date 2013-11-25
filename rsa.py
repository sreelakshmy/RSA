#!/usr/bin/env python

from sage.all import *
import sys

n= 65354147
e = 13
p=7013
q=9319
phi=(q-1)*(p-1)
bezout = xgcd(e, phi);
d = Integer(mod(bezout[1], phi))
f = open( sys.argv[1] , "r" )
asdf = ""
for line in f: 
    line = int(line.strip())
    dec = power_mod(line,d,n)
    asdf += chr(dec)
print asdf
