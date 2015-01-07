import sys
import os
import split

class SplitCsv:
    def main(self):
        args = sys.argv
        if len(args) > 1:
            filename = args[1]
        else:
            print "Parameter 1 [CSV File] Required"
            sys.exit(0)
        if len(args) > 2:
            directory = args[2]
        else:
            directory = filename.split('/')[-1].split('.')[0]
        if len(args) > 3:
            perfile = int(args[3])
        else:
            perfile = 1000

        if os.path.isfile(filename) != True:
            print "Invalid File"

        if os.path.exists(directory) != True:
            os.mkdir(directory)
        else:
            print "Directory Already Exists"
            sys.exit()

        print "Splitting " + filename + " into " + directory + "("+str(perfile)+")"

        split.split(filename,directory,perfile)
