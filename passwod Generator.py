import random
import string

if __name__=="__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercasen
    s3=string.digits
    s4=string.punctuation
    plen=int(input("enter the password length\n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("".join(s[0:plen]))




