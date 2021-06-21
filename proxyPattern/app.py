from storage import StorageProxy

storage = StorageProxy()   # in memory
storage.save("Test Data in memory")
print(storage.load())

storage = StorageProxy("file")   # in file
storage.save("Test Data in file")
print(storage.load())
