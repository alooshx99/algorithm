def charCounter(x):
    arr = []
    subArr = []
    preChar = x[0]
    counter = 0
    for i in x:
            
        if i == preChar:
            counter += 1

        else:
            subArr.append(counter)
            subArr.append(preChar)
            arr.append(subArr)
            subArr = []
            counter = 1
            preChar = i

    subArr.append(counter)
    subArr.append(preChar)
    arr.append(subArr)

    return arr



def createString(x):
    string = ""
    for i in x:
        for j in range(i[0]):
            string = string + i[1]

    return string

