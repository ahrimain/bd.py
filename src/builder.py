import os
import shutil

buildpath = ".build/"

def buildmodules():
    modules = []

    for module in os.listdir('./modules'):
        modules.append(module.replace(".bdp", ""))
    return modules

def build(filein, fileout):
    modules = buildmodules()
    file = open(filein, "r")
    fileout = open(fileout, "w")
    for line in file:
        for module in modules:
            if "<"+module+" />" in line:
                modsrc = open("./modules/"+module+".bdp", "r")
                for modline in modsrc:
                    fileout.write(modline)
                break
        fileout.write(line)
        continue
    
    file.close()
    fileout.close()

def pagenav(path):
    pages = os.listdir(path)
    for page in pages:
        if os.path.isdir(path+page):
            pagenav(path+page+"/")
            try:
                os.mkdir(path.replace("pages", ".output")+page)
            except FileExistsError:
                continue
        elif ".bdp" in page:
            file = open(buildpath+"pages", "a")
            file.write(path+page+"\n")
            file.close()
        else:
            continue

def assetsnav(path):
    assets = os.listdir(path)
    for asset in assets:
        if os.path.isdir(path+asset):
            assetnav(path+asset+"/")
        else:
            file = open(buildpath+"assets", "a")
            file.write(path+asset+"\n")
            file.close

def buildpages():
    rootpath = "pages/"
    pagenav(rootpath)
    pages = open(buildpath+"pages", "r")
    for line in pages:
        if line.strip() == "":
            continue
        else:
            build(line.strip(), line.strip().replace("pages", ".output").replace(".bdp", ".html"))

def buildassets():
    assetsnav("./assets/")
    try:
        shutil.copytree("./assets", "./.output/assets")
    except FileExistsError:
        shutil.rmtree("./.output/assets")
        shutil.copytree("./assets", "./.output/assets")

def buildserver():
    pages = open(buildpath+"pages", "r")
    assets = open(buildpath+"assets", "r")
    file = open(".output/server.js", "w")
    file.write("const http = require('http');\n")
    file.write("const fs = require('fs');\n")
    file.write("const server = http.createServer((req, res) => {\n")
    for line in pages:
        if line.strip() == "":
            continue
        else:
            file.write("if (req.url ==='"+line.strip().replace("pages", "").replace("index.bdp", "")+"' || req.url === '"+line.strip().replace("pages", "").replace(".bdp", ".html")+"') {\n")
            file.write("res.writeHead(200, { 'Content-Type': 'text/html' });\n")
            file.write("(fs.readFile('"+line.strip().replace("pages", ".output").replace(".bdp", ".html")+"', (err, data) => {if (err) {console.log(err)};res.end(data);}));\n")
            file.write("}\n")
    for line in assets:
        if line.strip() == "":
            continue
        else:
            file.write("if (req.url ==='"+line.strip().replace(".", "", 1).replace("index.bdp", "")+"' || req.url === '"+line.strip().replace("pages", "").replace(".bdp", ".html")+"') {\n")
            if ".jpg" in line:
                file.write("res.writeHead(200, { 'Content-Type': 'image/jpg' });\n")
            elif ".png" in line:
                file.write("res.writeHead(200, { 'Content-Type': 'image/png' });\n")
            elif ".js" in line:
                file.write("res.writeHead(200, { 'Content-Type': 'text/js' });\n")
            elif ".ts" in line:
                file.write("res.writeHead(200, { 'Content-Type': 'image/jpg' });\n")
            else:
                file.write("res.writeHead(200, { 'Content-Type': 'text/plaintext' });\n")
            file.write("(fs.readFile('.output"+line.strip().replace(".", "", 1)+"' , (err, data) => {if (err) {console.log(err)};res.end(data);}));\n")
            file.write("}\n")
    file.write("});\n")
    file.write("const PORT = 3000\n")
    file.write("server.listen(PORT, () => {")
    file.write("});")
    file.close()
    assets.close()
    pages.close()