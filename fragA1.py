#!/usr/bin/python

import glob, fileinput


fSave = open('output.txt', 'w')
fSave.write('filename,#bins,#activebins,#activebouts\n')
binctr = 0

#fname = 
curFile = 'none'
prevFile = 'none'

for filename in glob.glob('*.pir'):
	actBinCtr = 0    # counter for the nr active bins in a file
	#totBoutCtr = 0   # counter for the nr activity bouts in a file
	actBoutCtr = 0   # counter for the total nr of bouts in a file
	
	active = True
	for line in fileinput.input(filename):
		#print(fileinput.filename() + ' ' + str(fileinput.lineno()))
		binVal = int(line)
				
		# 	
		if binVal > 0:
			actBinCtr += 1
			if active != True:
				active = True
				actBoutCtr += 1
				print ('active')
		else:
			active = False
			print ('inactive')
		
	#fragmentation = activectr/fileinput.lineno()
	fSave.write(fileinput.filename() + ',' + str(fileinput.lineno()) + ',' + str(actBinCtr) + ',' + str(actBoutCtr) + '\n')
fSave.close()
