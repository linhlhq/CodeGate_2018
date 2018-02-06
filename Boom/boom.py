import subprocess

def main10(a1,a2):
    v5 = -a2
    v4 = 32 - a2
    v3 = 32 - a2
    return ((a1 << (v3 & 0x1f)) | ~(-1 << (v4 & 0x1f)) & (a1 >> (a2 & 0x1f)))&0xffffffff

def fun12(a1,a2):
    if a2 == 1:
        v4 = a1 + 1
    elif a2 % 2 == 1:
        v3 = 3 * a2
        v4 = fun12(a1+1,v3+1)
    else:
        v4 = fun12(a1+1,a2/2)
    return v4

def find_number():
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    proc = subprocess.Popen(['./boom'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                    s = "Know what? It's a new day~\n49 15 15 31 1 23 13\n31\n"
                    s1 = str(i) + ' ' + str(j) + " " + str(k) + " " + str(l) + '\n'
                    # print s1
                    s += s1
                    if proc.communicate(s)[0].find("Here's another one~") != -1:
                        return s1


#open file tmp/files/1-2-3
print '[+] solution 1'
print "\tKnow what? It's a new day~\n\tIt's cold outside..\n\tWe need little break!"

base = 'f7*zq5$ase0t6ui#^yd2owgb_n8pu4!k&vc@lrj19mx3h'
key = ["carame1",'w33kend','pand0ra']
prob_1 = []
index = []

#open file tmp/files/4-5-6

for i in key:
    tmp = []
    for c in i:
        for j in xrange(len(base)):
            if c == base[j]:
                tmp.append(j)
                break
    index.append(tmp)

for i in index:
    tmp=[]
    for c in i:
        for j in xrange(0x100):
            x = main10(main10(main10(j,3)^0x62,5)^0x32,7)
            if x % 0x2f == c:
                tmp.append(j)
                break
    prob_1.append(tmp)

print "[+] solution 2: "
for i in xrange(3):
    print '\t'+key[i],prob_1[i]

#open file /tmp/files/13
print "[+] solution 3:"
for i in xrange(0x10,0x50):
    if fun12(0,i) == 0x6b:
        print '\t',i

#open file /tmp/file/8

print "[+] solution 4:"
print '\t',find_number()

#open file /tmp/files/11
s = 'H_vocGfsg4p_xicwcrwexg4r'
print "[+] Solution 5:"
prob_5 = []
for i in xrange(len(s)):
    if i % 5 == 1:
        prob_5.append(chr(ord(s[i])+2))
    else:
        prob_5.append(chr(ord(s[i])-4))
print '\t'+''.join(prob_5)
#open file /tmp/files/8
print "[+] solution 6:"
print '\t17 24 1 8 15 23 5 7 14 16 4 6 13 20 22 10 12 19 21 3 11 18 25 2 9'