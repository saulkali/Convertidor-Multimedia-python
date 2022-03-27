import platform

class System(object):
    
    type:str = platform.system()
    
    def __init__(self) -> None:
        pass