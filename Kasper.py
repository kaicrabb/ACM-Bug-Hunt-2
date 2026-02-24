#Literally just my cryptography homework

##vars
c = "oabaaby" #ciphertext
k = "nwbjybf" #same-length key
p = "" #plaintext, empty right now
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
###it would make more sense to use a dictionary, but we're just gonna use the index of the letter, okay? okay.

##split the strings into lists, make sure the text is all lowercase
c = (list(c.lower()))
k = (list(k.lower()))
if(len(c) == len(k)): #make sure the ciphertext and key are the same. we're assuming that neither have spaces because i don't wanna deal with whitelisting.
    for i in range(len(c)):
        p += l[(l.index(c[i]) - l.index(k[i]))%26] #the actual decryption-> (c-k)%25
    print(p)
else: print("uh oh")
