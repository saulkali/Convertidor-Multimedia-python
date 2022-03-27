#helper
from helper import singleton
#pys settings
from .downloader import Downloader
from .system import System

@singleton
class SettingsManager(object):
    downloader:Downloader = None
    system:System = None
    
    def __init__(self) -> None:
        self.system = System()
        self.downloader = Downloader()