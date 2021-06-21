# from memoryStorage import MemoryStorage
# from fileStorage import FileStorage


class StorageProxy:
    def __init__(self, storageType="memory"):
        if storageType == "memory":
            self.realStorage = MemoryStorage()
        elif storageType == "file":
            self.realStorage = FileStorage()
        else:
            raise Exception('Wrong storage type')

    def __getattr__(self, name):
        if name == "load":
            return self.realStorage.load
        if name == "save":
            return self.realStorage.save
