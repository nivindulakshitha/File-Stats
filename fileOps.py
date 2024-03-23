import os
from datetime import datetime

class file:
    def __init__(self, filepath):
        self.filepath = filepath      

class fileStat(file):
    
    def __init__(self, filepath):
        super().__init__(filepath)
        self.fileReady = False
        self.filestat = {}
        self.__getFileReady()
    
    def __getFileReady(self):
        try:
            with open(file=self.filepath, mode="r", encoding="utf8") as file:
                self.fileReady = True
                self.filestat["readyState"] = True
                self.filestat["readyStateError"] = NotImplemented
                self.filestat["readyStateErrorLog"] = NotImplemented
                self.__prepareFileStat()
            
        except FileNotFoundError as error:
            self.filestat["readyState"] = False
            self.filestat["readyStateError"] = error
            self.filestat["readyStateErrorLog"] = "Provided location cannot be found."
            
        except FileExistsError as error:
            self.filestat["readyState"] = False
            self.filestat["readyStateError"] = error
            self.filestat["readyStateErrorLog"] = "No any file exists in provided location"
        
        except:
            self.filestat["readyState"] = False
            self.filestat["readyStateError"] = NotImplemented
            self.filestat["readyStateErrorLog"] = NotImplemented
            
        
    def getFilepath(self):
        return self.filepath
    
    def setFilePath(self, new_filepath):
        self.filepath = new_filepath
        self.__getFileReady()
        
    def __prepareFileStat(self):
        file_stat = os.stat(self.filepath)
        properties = {
            "fullpath": os.path.abspath(self.filepath),
            "size": file_stat.st_size,
            "ownerUid": file_stat.st_uid,
            "groupGid": file_stat.st_gid,
            "lastAccessed": self.__formatTimestamp(file_stat.st_atime),
            "lastModified": self.__formatTimestamp(file_stat.st_mtime),
            "creationTime": self.__formatTimestamp(file_stat.st_birthtime)
        }
        self.filestat.update(properties)
        
    def __formatTimestamp(self, timestamp):
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        
    def getFileStat(self):
        return self.filestat