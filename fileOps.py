import os

class fileStat:
    def __init__(self, filepath):
        self.filepath = filepath
        
        
        self.fileReady = False
        self.filestat = {}
        self.__getFileReady()
        self.__prepareStat()
        
        
    def __getFileReady(self):
        try:
            with open(file=self.filepath, mode="r", encoding="utf8") as file:
                self.fileReady = True
                self.filestat["readyState"] = True
                self.filestat["readyStateError"] = NotImplemented
                self.filestat["readyStateErrorLog"] = NotImplemented
            
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
        
    def __prepareStat(self):
        file_stat = os.stat(self.filepath)
        properties = {
            "size": file_stat.st_size,
            "ownerUid": file_stat.st_uid,
            "groupGid": file_stat.st_gid,
            "lastAccessed": file_stat.st_atime,
            "lastModified": file_stat.st_mtime,
            "creationTime": file_stat.st_birthtime
        }
        self.filestat.update(properties)
        
    def getStat(self):
        return self.filestat