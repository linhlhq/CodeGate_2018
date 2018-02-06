import hashlib
flag = []
#fun1
for i in range(32,127):
	for j in range(32,127):
		if i*2*((i^j)&0xff)-j==10858: 
			if i > 85 and i <= 95 and j > 96 and j <=111:
				flag.append(chr(i))
				flag.append(chr(j))
				#fun 2
				for i1 in range(32,127):
					if j % i1 == 7 and i1 > 90:
						flag.append(chr(i1))
						#fun 3
						for i2 in xrange(32,127):
							if (i1/i2+((i1^i2)&0xff)) == 21 and i2 < 119:
								flag.append(chr(i2))
								flag.append('_')
								#fun 4
								for i3 in xrange(32,127):
									if (i3 + 0x5f) ^ (i3) == 225 and i3 <= 89:
										#fun 5
										for i4 in xrange(32,127):
											for i5 in xrange(32,127):
												if i3 <= i4 and i4 <= i5 and i3 > 85 and i4 > 110 and i5 > 115 and (i4+i5)^(i3+i4) == 44 and (i4+i5)%i3+i4==161:
													flag.append(chr(i3))
													flag.append(chr(i4))
													flag.append(chr(i5))
													#fun 6
													for i6 in xrange(32,127):
														for i7 in xrange(32,127):
															if i5 >= i6 and i6 >= i7 and i5 <= 119 and i6 > 90 and i7 <= 89 and ((i5+i7)^(i6+i7))==122 and (i5+i7)%i6 + i7 == 101:
																flag.append(chr(i6))
																flag.append(chr(i7))
																#fun 7
																for i8 in xrange(32,127):
																	for i9 in xrange(32,127):
																		if i7 <= i8 and i8 <= i9 and i9 <= 117 and (i7 + i8)/i9 *i8==97 and (i9 ^ (i7-i8))*i8 == -10088 and i9 <= 114:
																			flag.append(chr(i8))
																			flag.append(chr(i9))
																			#fun 8
																			for a2 in xrange(32,127):
																				for a3 in xrange(32,127):
																					if i9 == a2 and a2 >= a3 and a3 <= 99 and a3+i9*(a3-a2)-i9==-1443:
																						flag.append(chr(a2))
																						flag.append(chr(a3))
																						#fun 9
																						for x2 in xrange(32,127):
																							for x3 in xrange(32,127):
																								if a3 >= x2 and x2 >= x3 and x2*(a3+x3+1)-x3 == 15514 and x2 > 90 and x2 <= 99:
																									flag.append(chr(x2))
																									flag.append(chr(x3))
																									# fun10
																									for b2 in xrange(32,127):
																										for b3 in xrange(32,127):
																											if b2 >= x3 and x3 >= b3 and b2 > 100 and b2 <= 104 and x3 + (b2^(b2-b3))-b3 == 70 and (b2+b3)/x3+x3 == 68:
																												#fun 11
																												for j2 in xrange(32,127):
																													for j3 in xrange(32,127):
																														if b3 >= j2 and j2 >= j3 and j2 <= 59 and j3 <= 44 and b3+(j2^(j3+j2))-j3==111 and (j2 ^(j2-j3))+j2 == 101:
																															flag.append(chr(b2))
																															flag.append(chr(b3))
																															flag.append(chr(j2))
																															flag.append(chr(j3))

y1 = ord(flag[len(flag)-1])
#fun 12
for y2 in xrange(32,127):
	for y3 in xrange(32,127):
		if y1 <= y2 and y2 <= y3 and y1 > 40 and y2 > 90 and y3 <= 109 and y3+(y2^(y3+y1))-y1 == 269 and (y3^(y2-y1))+y2 == 185:
			flag.append(chr(y2))
			flag.append(chr(y3))
			#fun 13
			for r2 in xrange(32,127):
				for r3 in xrange(32,127):
					if y3 >= r3 and r2 >= r3 and r2 <= 99 and r3 > 90 and y3 + (r2^(r2+y3))-r3==185:
						#fun 14
						for t2 in xrange(32,127):
							for t3 in xrange(32,127):
								if t2 >= t3 and t2 >= r3 and t3 > 95 and t2 <= 109 and ((t2 - r3)*t2^t3)-r3==1214 and ((t3-t2)*t3^r3)+t2==-1034:	
									res = ''.join(flag)+"%c%c"%(r2,r3)+"%c%c"%(t2,t3)
									hash256 = hashlib.sha256(res).hexdigest()
									if hash256 == '0a435f46288bb5a764d13fca6c901d3750cee73fd7689ce79ef6dc0ff8f380e5':
										print 'flag: '+res

