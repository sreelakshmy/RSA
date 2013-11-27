import time
from sage.all import*
def rsa_chinesereminder():
    n=25737144289
    e=13
    q=28649
    p=898361
    cipher=Integer(int(raw_input("Enter the message(in numbers):")))
    m=(q-1)*(p-1)
    start_time=time.time()
    d=inverse_mod(e,m)
    #n.factor()
    a1=mod(d,(p-1))
    a2=mod(d,(q-1))
    in_q=inverse_mod(q,p)
    m1=Integer(int(pow(cipher,a1,p)))
    m2=Integer(int(pow(cipher,a2,q)))
    dm=Integer(int(m1-m2))
    ci=Integer(int(in_q*dm))
    msg1=Integer(int(mod(in_q*(m1-m2),p)))
    msg=Integer(int(m2+(msg1*q)))
    end_time=time.time()-start_time
    print "Message:",msg
    return end_time

def main():
    end_time=rsa_chinesereminder()
    print "Total time:",end_time
if __name__=='__main__':
    main()
