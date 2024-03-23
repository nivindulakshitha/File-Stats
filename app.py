""" import os

def viewStat(filepath, view_content):        
    if (not os.path.exists(filepath)):
        print("Path is not locatable.")
    
    elif (not os.path.isfile(filepath)):
        print("Provided location is not a readable file.")
    
    else:
        size = os.path.getsize(filepath)
        print("Total size of the file:", size, "bytes")
        
        lines = sum(1 for line in open(filepath))
        print("Total number of lines:", lines)
        
        with open(filepath, mode="r", encoding="utf8") as file:
            file_content = file.read()

            splitted_content = file_content.strip().split()
            print(f"Total number of words: {len(splitted_content)}")
            
            if (view_content):
                print(file_content)

def runApp():
    filepath = input("Enter file location: ")
    view_content = True if input("Do you want to see the content? (yes/no): ") == "yes" else False
    viewStat(filepath, view_content)

if __name__ == "__main__":
    runApp() """
    
from fileOps import fileStat

myfileStat = fileStat("sample.txt")
if (myfileStat.fileReady):
    pass
    print(myfileStat.getFileStat())
    
