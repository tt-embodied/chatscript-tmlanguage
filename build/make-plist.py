import sys
import json
from plistlib import writePlist

def main ():
	inFile = sys.argv [1]
	outFile = sys.argv [2]
	json_object = json.load(open(inFile))

	writePlist(json_object, outFile)

if __name__ == "__main__":
	main ()