#0-1 Knapsack

##vars
space = 16	#max space allowed
k = 0 			#knapsack
c = []			#stores v/w
o = []			#ordered c, by index 
m = 0 			#a tempory maximum value. i think i'm using too many variables. 
###constants-- you should never change these
v = [4,2,2,1,10]
w = [12,1,2,1,4]

##calc V/W
for i in range(len(v)):
    c.append((v[i]/w[i]))
##order list, but weirdly
while len(c) > len(o):
    m = -1
    i = 0
    for x in range(c):
        if c[x] > m:
            m = c[x]
            i = x
    o.append(i)
    c[i] = -1

##fill the knapsack
i = 0		#set index back to 0
while space > 0:
    if w[o[i]] <= space:
        space -= w[o[i]]
        k += v[o[i]]
    else: i += 1
print(k)
