#!/usr/bin/python

import glob, fileinput


fsave = open('output.txt', 'w')
fsave.write('filename,#bins,#activebins\n')
binctr = 0
activectr = 0
#fname = 
curfile = 'none'
prevfile = 'none'

for filename in glob.glob('*.pir'):
	activectr = 0
	for line in fileinput.input(filename):
		#print(fileinput.filename() + ' ' + str(fileinput.lineno()))
		binval = int(line)
		if binval > 0:
			activectr+=1
		
	#fragmentation = activectr/fileinput.lineno()
	fsave.write(fileinput.filename() + ',' + str(fileinput.lineno()) + ',' +  str(activectr) + '\n')
fsave.close()
