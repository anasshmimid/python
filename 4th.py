from pwn import xor


a = "c1cbd6d9d6d0c7d1fdc0cbc7ccfdd6d7fdc3d1fdd6d0cdd7d4c7fdcec7fdc4cec3c5fd8383838383df"


a = bytes.fromhex(a)

for i in range(1,256) :
    b = xor(a,i)
    if  b"cit" in b :
        print(b)
        break












