import csv

def split(filename,directory,perfile):
    with open(filename,"rw") as csvfile:
        lines = csv.reader(csvfile)
        i = 0
        file_num = 0
        newfile = open(directory+"/"+"part_"+str(file_num)+".csv","w")
        for line in lines:
            i+=1
            newfile.write(','.join(line)+"\n")
            if i > perfile:
                newfile.close()
                i = 0
                file_num+=1
                newfile = open(directory+"/"+"part_"+str(file_num)+".csv","w")
        newfile.close()
