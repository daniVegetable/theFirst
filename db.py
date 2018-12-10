def changePswrd(key: str, newPswrd):
    file2 = []
    with open("mission.db", "r") as file:
        for line in file:
            if key+":" in line:
                file2.append(line.split(":")[0].replace("\n", "") + ":" + newPswrd + "\n")
                continue
            file2.append(line)
    with open("mission.db", "w") as file:
        for i in range(len(file2)):
            file.writelines(file2[i])

changePswrd("pop", "2345")