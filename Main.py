#funkcijas daļa

def ReadDataFromFile(filePath):
    target_list = []

    if filePath != "Komandas.csv":
        with open(filePath, "r") as file:
            for line in file:
                values = line.strip().split(",")
                target_list.append(values)
        return target_list

    else:
        teams_players = [["Komandas nosaukums", "Spēlētājs 1", "Spēlētājs 2", "Spēlētājs 3", "Spēlētājs 4", "Spēlētājs 5"]]
        all_numbers = [["MVPBalles1Spēlētāja", "MVPBalles2Spēlētāja", "MVPBalles3Spēlētāja", "MVPBalles4Spēlētāja", "MVPBalles5Spēlētāja"]]

        with open(filePath, "r") as file:
            next(file)

            for line in file:
                values = [v.strip() for v in line.split(",")]

                komandas = [values[0]]
                for i in range(1, len(values), 2):
                    komandas.append(values[i])

                MVP_points = []
                for i in range(2, len(values), 2):
                    try:
                        MVP_points.append(int(values[i]))
                    except:
                        pass

                teams_players.append(komandas)
                all_numbers.append(MVP_points)

        return teams_players, all_numbers

def AppendDataToFile(FilePath, data):
    with open(FilePath, "a") as file: #Atveram failu rakstīšanas režīmā, lai pievienotu datus
        line = ",".join(data)
        file.write(line + "\n")
        file.write("")

def DeleteDataToFile(FilePath, index):
    with open(FilePath, "r") as file:
        lines = file.readlines()

    if 0 <= index < len(lines):
        del lines[index]

    with open(FilePath, "w") as file:
        file.writelines(lines)

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

def registration():
    print("Lūdzu, ievadiet savu e-pasta adresi:")
    email = input()
    with open("Lietotaji.csv", "r") as file:
        for line in file:
            values = line.strip().split(",")
            if values[0] == email:
                print("Šī e-pasta adrese jau ir reģistrēta. Lūdzu, izvēlieties citu e-pasta adresi.")
                return 

    print("Lūdzu, ievadiet savu parole:")
    parole = input()
    print("Lūdzu, ievadiet vai tu esi administrators:")
    AdministratoraTiesibas = input()
    print("Lūdzu, ievadiet savu lietotājvārdu:")
    Username = input()

    user_data = [email, parole, AdministratoraTiesibas, Username, ""]
    AppendDataToFile("Lietotaji.csv", user_data)
    print("Reģistrācija veiksmīga!")
    return AdministratoraTiesibas

def autorization():
    print("Lūdzu, ievadiet savu e-pasta adresi:")
    email = input()
    print("Lūdzu, ievadiet savu parole:")
    parole = input()

    with open("Lietotaji.csv", "r") as file:
        for line in file:
            values = line.strip().split(",")
            if values[0] == email and values[1] == parole:
                print("Autorizācija veiksmīga!")
                return values[2]
    print("Neizdevās autorizēties. Lūdzu, pārbaudiet savu e-pasta adresi un paroli.")
    return False
#Galvenā programma

Lietotaji = ReadDataFromFile("Lietotaji.csv")
Speles = ReadDataFromFile("Speles.csv")
Saciensibas = ReadDataFromFile("Saciensibas.csv")
Komandas, mvpBalles = ReadDataFromFile("Komandas.csv")
adminTies = False
exit = False

print("Sveicināti! Lūdzu, izvēlieties darbību:")
print("1. Reģistrācija")
print("2. Autorizācija")

while input != "1" and input != "2":
    inp = input()
    if inp == "1":
        adminTies = registration()
    elif inp == "2":    
        adminTies = autorization()

while exit == False:
