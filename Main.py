#funkcijas daļa

def ReadDataFromFile(FilePath):
    target_list = []
    with open(FilePath, "r") as file:
        for line in file:
            values = line.strip().split(",")  #Lasam katru rindu, noņemam liekās atstarpes un sadalām pēc komatiem
            target_list.append(values)
    print(target_list)
    return target_list

def AppendDataToFile(FilePath, data):
    with open(FilePath, "a") as file: #Atveram failu rakstīšanas režīmā, lai pievienotu datus
        line = ",".join(data)
        file.write(line + "\n")

def DeleteDataToFile(FilePath, index):
    with open(FilePath, "r") as file:
        lines = file.readlines()

    if 0 <= index < len(lines):
        del lines[index]

    with open(FilePath, "w") as file:
        file.writelines(lines)

#Galvenā programma

Lietotaji = ReadDataFromFile("Lietotaji.csv")
Speles = ReadDataFromFile("Speles.csv")
Saciensibas = ReadDataFromFile("Saciensibas.csv")
Komandas = ReadDataFromFile("Komandas.csv")