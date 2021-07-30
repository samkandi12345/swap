def swap():
    enterfile1 = input("enter file 1: ")
    enterfile2 = input("enter file 2: ")

    with open(enterfile1 , "r") as a:
        dataA = a.read()
    with open(enterfile2 , "r") as b:
        dataB = b.read()

    with open(enterfile1 , "w") as a:
        a.write(dataB)
    with open(enterfile2 , "w") as b:
        b.write(dataA)

swap()