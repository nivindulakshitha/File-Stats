import os
from datetime import datetime

class __file__:
    def __init__(self, filepath):
        self.filepath = filepath
        self.fileReady = False
        self.__filestat__ = {}
        self.__textStat__ = {}
        self.__getFileReady()
        
    def __getFileReady(self):
        try:
            with open(file=self.filepath, mode="r", encoding="utf8") as file:
                self.fileReady = True
                self.__filestat__["readyState"] = True
                self.__filestat__["readyStateError"] = NotImplemented
                self.__filestat__["readyStateErrorLog"] = NotImplemented
            
        except FileNotFoundError as error:
            self.__filestat__["readyState"] = False
            self.__filestat__["readyStateError"] = error
            self.__filestat__["readyStateErrorLog"] = "Provided location cannot be found."
            
        except FileExistsError as error:
            self.__filestat__["readyState"] = False
            self.__filestat__["readyStateError"] = error
            self.__filestat__["readyStateErrorLog"] = "No any file exists in provided location"
        
        except:
            self.__filestat__["readyState"] = False
            self.__filestat__["readyStateError"] = NotImplemented
            self.__filestat__["readyStateErrorLog"] = NotImplemented
            
        
    def getFilepath(self):
        return self.filepath
    
    def setFilePath(self, new_filepath):
        self.filepath = new_filepath
        self.__getFileReady()

class fileStat(__file__):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.__prepare__filestat__()

    def __prepare__filestat__(self):
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
        self.__filestat__.update(properties)
        
    def __formatTimestamp(self, timestamp):
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        
    def getFileStat(self):
        return self.__filestat__