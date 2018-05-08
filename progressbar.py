from time import sleep
import sys

def main():
	intRecords=int(sys.argv[1])

	intTotal=intRecords
	intPoint=intTotal/100
	intIncrement=intTotal/20

	for i in xrange(intTotal):
		sleep(0.05)

		if(i%(5*intPoint)==0):
			sys.stdout.write("\r[" + "=" * (i / intIncrement) + " " * ((intTotal - i) / intIncrement) + "]" + str(i / intPoint) + "%")
			sys.stdout.flush()

main()



