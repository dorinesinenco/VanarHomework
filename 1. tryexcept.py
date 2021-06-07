def getData(index):
    global data
    data = [10, 20, 30, 40, 50]
    return data[index]


try:
    index = int(input("Enter an index: "))
    print(getData(index))
except ValueError:
    print("Index must be an integer")
except IndexError:
    print("Index can't be larger than " + str(len(data)))
