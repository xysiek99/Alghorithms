def saveToFile(filename, value):
    f = open(filename, 'a')
    f.write(value)
    f.write('\n')
    f.close()

s = [12, 6, 22, 1, 76, 18, 3, 43]

def insert(listName, myValue):
    listName.append(myValue)
    cost = len(listName) + 1
    print(cost)
    saveToFile("insert.txt", str(myValue))
    
def access(listName, myValue):
    position = 0
    for i in range(0, len(listName) - 1):
        if listName[i] == myValue:
            position = i
    cost = position 
    print(cost)
    saveToFile("access.txt", str(myValue))
            
def delete(listName, myValue):
    position = 0
    for i in range(0, len(listName) - 1):
        if listName[i] == myValue:
            listName.pop(i)
            transP = len(listName) - i
            position = i
    cost = transP + position + 1
    print(cost)
    saveToFile("delete.txt", str(myValue))
    
def operationTR(listName, myValue):
    access(listName, myValue)
    insert(listName, myValue)
    
    lastElement = listName[len(listName) - 1]
    oneBeforeLastElement = listName[len(listName) - 2]
    
    listName[len(listName) - 1] = oneBeforeLastElement
    listName[len(listName) - 2] = lastElement

    print(listName)    

delete(s, 18)
insert(s, 25)
operationTR(s, 23)
