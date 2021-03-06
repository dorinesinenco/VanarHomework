import json

datadict = {
    "manufacturer": "Audi",
    "model": "RS6",
    "year": 2016
}


class MemoryStorage:
    def __init__(self):
        self.data = None

    def save(self, data):
        self.data = data

    def load(self):
        return self.data


class FileStorage:
    def __init__(self):
        self.name = "data.txt"

    def save(self, data):
        file = open(self.name, "w")
        file.write(data)
        file.close()

    def load(self):
        file = open(self.name, "r")
        data = file.read()
        file.close()
        return data


class JsonStorage():
    def __init__(self):
        self.name = "data.json"

    def save(self, data):
        with open(self.name, 'w') as json_file:
            json.dump(data, json_file)
        return json_file

    def load(self):
        file = open(self.name, "r")
        data = json.load(file)
        file.close()
        return data


class StorageProxy:
    def __init__(self, storageType="memory"):
        if storageType == "memory":
            self.realStorage = MemoryStorage()
        elif storageType == "file":
            self.realStorage = FileStorage()
        elif storageType == "json":
            self.realStorage = JsonStorage()
        else:
            raise Exception("Wrong storage type")

    def __getattr__(self, name):
        print(name)
        if name == "load":
            return self.realStorage.load
        if name == "save":
            return self.realStorage.save


storage = StorageProxy("memory")   # in memory
storage.save("data in memory")
print(storage.load())

# storage = StorageProxy("file")   # in file
# storage.save("Test Data")
# print(storage.load())

storage = StorageProxy("json")   # in json file
print(storage.realStorage)
storage.save(datadict)
# print(storage.load())
