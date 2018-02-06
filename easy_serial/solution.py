block1 = [70,108,97,103,123,83,48,109,101,48,102,85,53]
block2 = [103,110,105,107,48,76,51,114,52]
block3 = []
s1b3_info = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s1b4_info = "abcdefghijklmnopqrstuvwxyz"
s1b2_info = "1234567890"
block3.append(s1b3_info[0])
block3.append(s1b4_info[19])
block3.append(s1b3_info[19])
block3.append(s1b4_info[7])
block3.append(s1b2_info[2])
block3.append(s1b3_info[18])
block3.append(s1b4_info[19])
block3.append(s1b2_info[3])
block3.append(s1b4_info[17])
block3.append(s1b4_info[18])

block1 = ''.join(chr(e) for e in block1)
block2 = ''.join(chr(e) for e in block2)
block3 = ''.join(block3)
print '%s#%s#%s'%(block1,block2,block3)