#funkcijas daļa

def ReadDataFromFile(FilePath):
    target_list = []
    with open(FilePath, "r") as file:
        for line in file:
            values = line.strip().split(",")  #Lasam katru rindu, noņemam liekās atstarpes un sadalām pēc komatiem
            target_list.append(values)
    print(target_list)
    return target_list

#Galvenā programma

Speles, Saciensibas, Komandas, Lietotaji = [], [], [], []

Lietotaji = ReadDataFromFile("Lietotaji.csv")
Speles = ReadDataFromFile("Speles.csv")
Saciensibas = ReadDataFromFile("Saciensibas.csv")
Komandas = ReadDataFromFile("Komandas.csv")