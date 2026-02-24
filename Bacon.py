#Bacon Cipher Encoder

##vars
plain = "cOol SecreT PhRasE"
bits = ""

##get bits
for x in plain:
    if x.isupper(): bits += 1
    elif x.islower(): bits += 0
    else: continue

##decode bits
s = 0
for i in range(int(len(bits)/8)):
    t=bits[s:s+8]
    print(chr(int(t, 2)), end="")
    s += 8
print()
