from time import sleep
import sys

def main():
	for i in range(21):
		sys.stdout.write('\r')
		sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
		sys.stdout.flush()
		sleep(0.15)

main()

