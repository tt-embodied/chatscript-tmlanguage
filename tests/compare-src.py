import sys
import json
from plistlib import readPlist

def main ():
	plistFile = sys.argv [1]
	jsonFile = sys.argv [2]

	plist_object = readPlist(open(plistFile))
	json_object = json.load(open(jsonFile))

	if sorted(plist_object.items()) != sorted(json_object.items()):
		sys.exit("*** Error: discrepency between '" + str(plistFile) + "' and '" + str(jsonFile) + "'. Make sure you have run 'npm run build'")

if __name__ == "__main__":
	main ()