from fileOps import fileStat

myfileStat = fileStat(filepath="sample.txt")
if (myfileStat.fileReady):
    print(myfileStat.getFileStat())