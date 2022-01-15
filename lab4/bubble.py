# Bubble sorting

testList = [20, 31, 9, 1]
lastIndex = len(testList) - 1
tempIndex = lastIndex

for i in range(lastIndex):
    print(f"------ i = {i} ------") # How many digits from end are ommited
    for j in range(tempIndex):
        print(f"j = {j}")
        print(f"Before: {testList}")
        if testList[j] > testList[j + 1]:
            greater = testList[j]
            smaller = testList[j + 1]
            testList[j] = smaller
            testList[j + 1] = greater
        print(f"After: {testList}")
    tempIndex -= 1 # Decrease because last element was set