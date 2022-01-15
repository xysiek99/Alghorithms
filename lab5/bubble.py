# Bubble sorting

testList = [7, 31, 5, 1]
lastIndex = len(testList) - 1
tempIndex = lastIndex
a = 1

for i in range(lastIndex):
    print(f"------ i = {i} ------")
    for j in range(tempIndex):
        print(f"Iteration = {a}")
        print(f"Before: {testList}")
        if testList[j] > testList[j + 1]:
            greater = testList[j]
            smaller = testList[j + 1]
            testList[j] = smaller
            testList[j + 1] = greater
        print(f"After: {testList}")
        a += 1
    tempIndex -= 1 # Decrease because last element was set
    # Najgorsza postać danych wejściowych: gdy liczby ustawione są malejąco(największa ilość operacji przestawiania do wykonania) - ilość iteracji zawsze taka sama