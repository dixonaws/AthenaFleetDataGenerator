import sys
from time import sleep

def main():
	intRecords=int(sys.argv[1])

	print 'Records: ' + str(intRecords)

	# print a maximum of 50 characters
	print 'Records%50 = ' + str(intRecords%50)

main()

