# Alghoritm 3

n = 1800
a = 1

while n != 6174 and n!= 0:
    print(f"Iteration: {a}")
    n_string = str(n)
    n_array = []
    for i in range(len(n_string)):
        n_array.append(int(n_string[i]))

    n_array.sort()

    if n_array[0] == 0:
        for i in n_array:
            if i != 0:
                index = n_array.index(i)
                n_array[0] = i
                n_array[index] = 0
                break
    
    n1_temp = "" 
    for myN in n_array: 
        n1_temp += str(myN)
    n1 = int(n1_temp)
    
    n_array.sort(reverse=True)
    n2_temp = "" 
    for myN in n_array: 
        n2_temp += str(myN)
    n2 = int(n2_temp)

    print(n1, n2)
    n = n2 - n1

    a += 1