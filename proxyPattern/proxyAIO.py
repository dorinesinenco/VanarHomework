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
        self.jsonname = "jsondata.json"

    def save(self, data):
        file = open(self.name, "a")
        file.write(data)
        file.close()

    def load(self):
        file = open(self.name, "r")
        data = file.read()
        file.close()
        return data

    def save_to_json(self, datadict):
        with open(self.name, 'w') as json_file:
            json.dump(datadict, json_file)
        return json_file

    def load_from_json(self):
        pass


class StorageProxy:
    def __init__(self, storageType="memory"):
        if storageType == "memory":
            self.realStorage = MemoryStorage()
        elif storageType == "file":
            self.realStorage = FileStorage()
        elif storageType == "tojson":
            self.realStorage = FileStorage()
        else:
            raise Exception("Wrong storage type")

    def __getattr__(self, name):
        if name == "load":
            return self.realStorage.load
        if name == "save":
            return self.realStorage.save
        if name == "tojson":
            return self.realStorage.save_to_json


storage = StorageProxy("memory")   # in memory
storage.save("data in memory")
print(storage.load())

# storage = StorageProxy("file")   # in file
# storage.save("Test Data")
# print(storage.load())

storage = StorageProxy("tojson")   # in json file
storage.save_to_json(datadict)
# print(storage.load())
