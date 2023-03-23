## BrainBin by Pooky,
## < > to move pointer
## , to push to compiler
## ; to move to new line
## . to end and run code

## Declare needed libs and vars
import os
array = [0, 0, 0, 0, 0, 0, 0, 0]
byte = []
point = 1

## Scan the current dir for .bf file
def fileLoad():
	global file
	list = os.listdir()

	for i in list:
		if i.endswith('.bbin'):
			file = i
		else:
			pass

	fileInter()

def fileInter():
	global point
	frl = open(file, 'r').readlines()

	for line in frl:
		for letter in line:

			## Pointer movement
			if letter == '>':
				point += 1
				if point > 8:
					point = 8

			if letter == '<':
				point = point - 1
				if point < 1:
					point = 1

			## Adding and subtracting
			if letter == '+':
				if array[int(point) - 1] != 1:
					array[int(point) - 1] += 1
				else:
					print('Cant go above 1!')
					pass

			if letter == '-':
				if array[int(point) - 1] != 0:
					array[int(point) - 1] -= 1
				else:
					print('Cant go below 0!')
					pass

			## Pushing to compiler
			if letter == ',':
				byte.append(''.join(str(i) for i in array))

			## New line identifier
			if letter == ';':
				byte.append('\n')

			## Running compiler
			if letter == '.':
				fileCompile()

def fileCompile():
	output = []

	for i in byte:
		if i == '\n':
			output.append(i)

		else:
			x = int(i, 2)
			output.append(x.to_bytes(1, "big").decode())
			print(i)

	print(''.join(output))
	print(output)

fileLoad()