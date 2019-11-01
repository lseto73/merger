#!/usr/bin/env python3

import sys
import os

def append_id(filename):
    parts = filename.split('.')
    return "".join(parts[:-1])+ '_' + '2' + '.' + parts[-1]
    
if __name__=="__main__":
    # grab parameters
    if len(sys.argv) != 3:
        print("usage: merger.py <original yaml file> <file containing config to add>")
        sys.exit(0)
    else:
        origfile = sys.argv[1]
        outputfile = append_id(sys.argv[1])
        configfile = sys.argv[2]
        append_after_str = input("Enter string to append after (e.g. \"element_extensions\": ")
        if os.path.exists(outputfile):
            print("There is already a file named ",outputfile)
            sys.exit(0)
        output = open(outputfile, 'w')
        userstring_in_file = -1
        for line in open(origfile):
            if append_after_str in line:
                userstring_in_file = 1
                output.write(line)
                for addconfig in open(configfile):
                    output.write(addconfig)
                print("Done! New File is: ",outputfile)
                sys.exit(1)
            else:
                output.write(line)
        if userstring_in_file == -1:
                print("Error: String was not in file")
                sys.exit(0)