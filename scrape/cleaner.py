import csv

def fileBurner(title,phone):
    
    f = open("clean.csv","a")
    # f.write(title+"\n"+phone+"\n\n")
    f.write(title+", "+phone+"\n")
    f.close()


with open("dumpfile.csv", newline='') as f:
    reader = csv.reader(f)
    count = 0
    changeFlag = 0
    masterList = list(reader)
    print(masterList)
    for a in masterList:
        if len(a) is not 0:
            if len(a) is 1:
                changeFlag=count
            else:
                if changeFlag is not 0:
                    #print("Stick = > "+str(masterList[changeFlag]))
                    print(str(masterList[changeFlag][0]+" "+masterList[count][0]))
                    print(str(masterList[count][1]))
                    fileBurner(str(masterList[changeFlag][0]+" "+masterList[count][0]),str(masterList[count][1]))
                    changeFlag=0
        count = count+1



