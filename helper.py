from pathlib import Path
import os

def absPath(file):
    return Path(__file__).parent.absolute() / file

def getFile(file):
    dirname = os.path.dirname(__file__)+"/"+file
    print("dirname: ",dirname)
    return dirname
    
def singleton(cls):
    instances = dict()

    def wrap(*args,**kargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kargs)
            return instances[cls]        
        return instances[cls]

    return wrap