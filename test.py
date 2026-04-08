Email,Parole,AdministrativasTiesibas,Username,SaglabatasTiesisbas
sdada
ddddd


Email,Parole,AdministratoraTiesibas,Username,SaglabataTiesraide
emailName@gmail.com,yuyu54,False,Geak_998,
emailhuhu@gmail.com,kjkjkjk,False,Poirko,
Joids@gmail.com,Moidsa,False,Urosda,
        

    print("Lūdzu, izvēlieties darbību:")
    print("1. Pievienot komandu")
    print("2. Dzēst komandu")
    print("3. Pievienot jaunu spēli")
    print("4. Dzēst spēli")
    print("5. Pievienot jaunu sacensību")
    print("6. Dzēst sacensību")
    print("7. Izdrukāt komandas un MVP balles")
    print("8. Izdrukāt spēles")
    print("9. Izdrukāt sacensības")
    print("10. Saglabāt spēles tiešraidi")
    print("11. Izdrukāt lietotāja informāciju")
    print("exit. Iziet")

inp = input()
    if inp == "1":
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

    elif inp == "2":    
        if adminTies == True:
            num = int(input("Ievadiet dzēšamās komandas rindu numuru: "))
            DeleteDataToFile("Komandas.csv", num)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "3":    
        if adminTies == True:
            mas = [input("Ievadiet spēles nosaukumu: "), input("Ievadiet spēles datumu: "), input("Ievadiet spēles rezultatu: "), input("Ievadiet pirmo komandu: "), input("Ievadiet otro komandu: ")]
            AppendDataToFile("Speles.csv", mas)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "4":    
        if adminTies == True:
                num = int(input("Ievadiet dzēšamās spēles rindu numuru: "))
                DeleteDataToFile("Speles.csv", num)
                pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "5":    
        if adminTies == True:
            mas = [input("Ievadiet sacensības nosaukumu: "), input("Ievadiet sacensības datumu: "), input("Ievadiet sacensības rezultātu: "), input("Ievadiet pirmo komandu: "), input("Ievadiet otro komandu: ")]
            AppendDataToFile("Saciensibas.csv", mas)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "6":    
        if adminTies == True:
            num = int(input("Ievadiet dzēšamās sacensības rindu numuru: "))
            DeleteDataToFile("Saciensibas.csv", num)
            pass
        else:
            print("Jums nav administratora tiesību, lai veiktu šo darbību.")

    elif inp == "7":    
        PrintData(Komandas)
        PrintData(mvpBalles)

    elif inp == "8":    
        PrintData(Speles)

    elif inp == "9":    
        PrintData(Saciensibas)

    elif inp == "10":
        safeInfo = input("Ievadiet speles indeksu, kuru tiešraide vēlaties saglabāt: ")
        Lietotaji[lietotajaIndex][len(Lietotaji[lietotajaIndex]) - 1] = Speles[int(safeInfo) - 1][5]
        ChangeDataToFile("Lietotaji.csv", lietotajaIndex, Lietotaji[lietotajaIndex])
        Lietotaji = ReadDataFromFile("Lietotaji.csv")
        lietotajaIndex = len(Lietotaji) - 1
        Lietotajs[1] = Lietotaji[lietotajaIndex]
        PrintData(Lietotajs)

    elif inp == "11":
        PrintData(Lietotajs)

    elif inp == "exit":
        print("Paldies, Uz redzēšanos!")
        exit = True
    else:
        print("Nederīga izvēle. Lūdzu, izvēlieties darbību no 1 līdz 10.")