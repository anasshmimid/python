from pwn import xor
a = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

a = bytes.fromhex(a)
b = "crypto{"
c = xor(a,b)
key = "myXORkey"
flag = xor(key,a)



print(flag)

