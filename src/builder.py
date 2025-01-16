import os

def buildmodules():
    modules = []

    for module in os.listdir('./modules'):
        modules.append(module.replace(".bdp", ""))
    return modules

def build(file):
    modules = buildmodules()
    file = open(file, "r")
    for line in file:
        for module in modules:
            if "<"+module+" />" in line:
                modsrc = open("./modules/"+module+".bdp", "r")
                for modline in modsrc:
                    print(modline.strip())
                break
        print(line.strip())
        continue
    
    file.close()