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
        teams_players = [["Komandas nosaukums", "Spēlētājs 1", "Spēlētājs 2", "Spēlētājs 3", "Spēlētājs 4", "Spēlētājs 5", "Vislabākais spēlētājs"]]
        all_numbers = [["Komandas nosaukums", "MVPBalles1Spēlētāja", "MVPBalles2Spēlētāja", "MVPBalles3Spēlētāja", "MVPBalles4Spēlētāja", "MVPBalles5Spēlētāja", "VislabakajaSpeletajaPunkti"]]

        with open(filePath, "r") as file:
            next(file)

            for line in file:
                values = [v.strip() for v in line.split(",")]         #funkcija ReadDataFromFile pieņem Filepath tipa vērtību FilePath atgriež divdimensijas masivu tipa vērtību target_list

                komandas = [values[0]]
                for i in range(1, len(values), 2):
                    komandas.append(values[i])
                komandas.append("")

                MVP_points = [values[0]]
                for i in range(2, len(values), 2):
                    try:
                        MVP_points.append(int(values[i]))
                    except:
                        pass
                MVP_points.append("")

                teams_players.append(komandas)
                all_numbers.append(MVP_points)
        return teams_players, all_numbers

def AppendDataToFile(FilePath, data):
    with open(FilePath, "a") as file:        #funkcija AppendDataToFile pieņem Filepath, list tipa vērtību FilePath, data atgriež neko
        line = ",".join(data)
        file.write(line + "\n")
        file.write("")

def ChangeDataToFile(FilePath, ChangeIndex, new_data):
    DeleteDataToFile(FilePath, ChangeIndex)           #funkcija ChangeDataToFile pieņem Filepath, int tipa vērtību FilePath, index, list tipa vērtību new_data, atgriež neko

    AppendDataToFile(FilePath, new_data)

def DeleteDataToFile(FilePath, index):
    with open(FilePath, "r") as file:
        lines = file.readlines()

    if 0 <= index < len(lines):                 # funkcija DeleteDataToFile pieņem Filepath, int tipa vērtību FilePath, index atgriež neko
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
            if type(item) == int:
                item = str(item)
            print("| ", end="")
            for i in range((30 - len(item)) // 2):
                print(" ", end="")
            print(item, end="")                             #funkcija PrintData pieņem divdimensijas masīvu tipa vērtību File atgriež neko, izdrukā masīva elementus tabulas formātā
            for i in range((31 - len(item)) // 2):
                print(" ", end="")
            print(" |", end="")
        print("")

    for i in range(len(File[0])):
        print("+", end="")
        for i in range(32):
            print("-", end="")
        print("+", end="")
    print("")

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
    print("Lūdzu, ievadiet vai tu esi administrators(Ja/Ne):")                                          #funkcija registration pieņem neko un atgriež boolean tipa vērtību AdministratoraTiesibas
    if input() == "Ja":
        AdministratoraTiesibas = True
    else:         
        AdministratoraTiesibas = False
    print("Lūdzu, ievadiet savu lietotājvārdu:")
    Username = input()

    user_data = [email, parole, AdministratoraTiesibas, Username, ""]
    AppendDataToFile("Lietotaji.csv", user_data)
    print("Reģistrācija veiksmīga!")
    return AdministratoraTiesibas

def autorization():
    print("Lūdzu, ievadiet savu e-pasta adresi:")
    email = input()
    print("Lūdzu, ievadiet savu parole:")                #funkcija autorization pieņem neko un atgriež boolean tipa vērtību AdministratoraTiesibas
    parole = input()

    with open("Lietotaji.csv", "r") as file:
        i = 0
        for line in file:
            values = line.strip().split(",")
            if values[0] == email and values[1] == parole:
                print("Autorizācija veiksmīga!")
                return values[2], i
            i+=1
    print("Neizdevās autorizēties. Lūdzu, pārbaudiet savu e-pasta adresi un paroli.")
    return False

#Galvenā programma

Lietotaji = ReadDataFromFile("Lietotaji.csv")
Speles = ReadDataFromFile("Speles.csv")
Saciensibas = ReadDataFromFile("Saciensibas.csv")
Komandas, mvpBalles = ReadDataFromFile("Komandas.csv")
adminTies = False
exit = False
lietotajaIndex = 0

print("Sveicināti! Lūdzu, izvēlieties darbību:")
print("1. Reģistrācija")
print("2. Autorizācija")

inp = ""
while inp != "1" and inp != "2":
    inp = input()
    if inp == "1":
        adminTies = registration()
        lietotajaIndex = len(Lietotaji)
    elif inp == "2":    
        adminTies, lietotajaIndex = autorization()

Lietotajs = [Lietotaji[0], Lietotaji[lietotajaIndex]]

while exit == False:
    print("Lūdzu, izvēlieties darbību:")
    print("1. Izdrukāt komandas un MVP balles")
    print("2. Izdrukāt spēles")
    print("3. Izdrukāt sacensības")
    print("4. Saglabāt spēles tiešraidi")
    print("5. Izdrukāt lietotāja informāciju")
    if adminTies == "True":
        print("6. Pievienot komandu")
        print("7. Dzēst komandu")
        print("8. Pievienot jaunu spēli")
        print("9. Dzēst spēli")
        print("10. Pievienot jaunu sacensību")
        print("11. Dzēst sacensību")
    print("exit. Iziet")

    inp = input()
    if inp == "1":
        for i in range(1, len(mvpBalles)):
            bestPlayer = ""
            bestPlayerPoints = -1
            for j in range(1, len(mvpBalles[i])):
                try:
                    value = int(mvpBalles[i][j])
                    if value > bestPlayerPoints:
                        bestPlayerPoints = value
                        bestPlayer = Komandas[i][j]
                except:
                    continue
            mvpBalles[i][len(mvpBalles[i]) - 1] = bestPlayerPoints
            Komandas[i][len(Komandas[i]) - 1] = bestPlayer
        PrintData(Komandas)
        PrintData(mvpBalles)

    elif inp == "2":    
        PrintData(Speles)

    elif inp == "3":    
        PrintData(Saciensibas)

    elif inp == "4":    
        safeInfo = input("Ievadiet speles indeksu, kuru tiešraide vēlaties saglabāt: ")
        Lietotaji[lietotajaIndex][len(Lietotaji[lietotajaIndex]) - 1] = Speles[int(safeInfo) - 1][5]
        ChangeDataToFile("Lietotaji.csv", lietotajaIndex, Lietotaji[lietotajaIndex])
        Lietotaji = ReadDataFromFile("Lietotaji.csv")
        lietotajaIndex = len(Lietotaji) - 1
        Lietotajs[1] = Lietotaji[lietotajaIndex]
        PrintData(Lietotajs)

    elif inp == "5":    
        PrintData(Lietotajs)

    elif inp == "6":    
        if adminTies == True:
            i = 1
            mas = [input("Ievadiet komandas vārdu: ")]

            while i <= 5:
                mas[i] = input("Ievadiet spēlētāja vārdu: ")
                mas[i + 1] = input("Ievadiet viņas MVP balles: ")
                i += 2

            AppendDataToFile("Komandas.csv", mas)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "7":    
        if adminTies == True:
            num = int(input("Ievadiet dzēšamās komandas rindu numuru: "))
            DeleteDataToFile("Komandas.csv", num)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "8":    
        if adminTies == True:
            mas = [input("Ievadiet spēles nosaukumu: "), input("Ievadiet spēles datumu: "), input("Ievadiet spēles rezultatu: "), input("Ievadiet pirmo komandu: "), input("Ievadiet otro komandu: ")]
            AppendDataToFile("Speles.csv", mas)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "9":    
        if adminTies == True:
                num = int(input("Ievadiet dzēšamās spēles rindu numuru: "))
                DeleteDataToFile("Speles.csv", num)
                pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "10":
        if adminTies == True:
            mas = [input("Ievadiet sacensības nosaukumu: "), input("Ievadiet sacensības datumu: "), input("Ievadiet sacensības rezultātu: "), input("Ievadiet pirmo komandu: "), input("Ievadiet otro komandu: ")]
            AppendDataToFile("Saciensibas.csv", mas)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "11":
        if adminTies == True:
            num = int(input("Ievadiet dzēšamās sacensības rindu numuru: "))
            DeleteDataToFile("Saciensibas.csv", num)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "exit":
        print("Paldies, Uz redzēšanos!")
        exit = True
    else:
        print("Nederīga izvēle. Lūdzu, izvēlieties darbību no 1 līdz 10.")