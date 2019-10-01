import os
from box.table import *

def createTables():
    tables = []

    for name in getFileNames():
        txt = getText(name)
        for section in txt.split("======"):
            if (section != ''):
                lines = section.splitlines()
                t = table(name.capitalize() + " " + lines[0])
                combined = ""
                for line in lines[1:]:
                    print(line)
                    if ((line[:2-len(line)]=="||") & (line[len(line)-2:]!="||")):
                        combined += line[2:] + "\n"
                    else:
                        if (line[len(line)-2:]=="||"):
                            combined += line[2:len(line)-2] + "\n"
                            #Sprint(combined[:combined.find("\n")] + "\n" + combined[combined.find("\n"):])
                            t.addRow(getRow(combined[:combined.find("\n")], combined[combined.find("\n"):]))
                            combined = ""
                        else:
                            t.addRow(getRow(line, ""))
                tables.append(t)

    return tables

def getRow(text, text2):
    begin = int(text[:2])
    if (begin == 0):
        begin = 100
    end = int(text[3:5])
    if (end == 0):
        end = 100
    return row(text[6:], begin, end, text2)

def getText(filename):
    f = open("./box/" + filename + ".txt", "r")
    text = f.read()
    f.close()
    return text
	
def saveText(data):
	f = open("./tsoutput/output.txt", "a")
	f.write(data)
	f.close()
    
def getFileNames():
    result = []
    for file in os.listdir("./box"):
        if file.endswith(".txt"):
            result.append(file[:-4])
    return result
