Email,Parole,AdministrativasTiesibas,Username,SaglabatasTiesisbas
sdada
ddddd


def PrintData(File):
    for i in range(len(File[0])):
        print("+", end="")
        for i in range(32):
            print("-", end="")
        print("+", end="")
    print("")
    for data in File:
        for item in data:
            print("| ", end="")
            for i in range((30 - len(item)) // 2):
                print(" ", end="")
            print(item, end="")                             #Izdrukājam datu elementu, centrējot to 40 rakstzīmju platumā
            for i in range((31 - len(item)) // 2):
                print(" ", end="")
            print(" |", end="")
        print("")
    for i in range(len(File[0])):
        print("+", end="")
        for i in range(32):
            print("-", end="")
        print("+", end="")