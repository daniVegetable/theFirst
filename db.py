def get_value(key: str, newPswd) -> str:
    with open("mission.db", "r") as file:
        for line in file:
            if key+":" in line:
                result = line.split(":")[1].replace("\n", "")
                newPas = line.replace(line.split(":")[1].replace("\n", ""), newPswd)
                file.writelines(newPas)

get_value("pop", "2345")