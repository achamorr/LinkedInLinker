import re
import os
import webbrowser

linkedinREGEX = "(www.linkedin.com\/in\/[A-Za-z\-0-9]*)"
linkedinFile = "shpe_chapter_presidents.txt"
phonenumberREGEX = "([0-9 \-]{10,})"
region3File = "region3.txt"

if __name__ == "__main__":
    linkedInList = list()
    wFile = open('output_text.txt', "a+")
    with open(linkedinFile, 'r') as rFile:
        line = rFile.readline()

        while (line):
            m = re.search(linkedinREGEX, line)
            if (m):
                group = m.group(1)
                print(group)
                linkedInList.append(group)
                wFile.write(group + "\n")

            line = rFile.readline()
        
    wFile.close()


    #open browser
    
    for link in linkedInList:
        webbrowser.open(link, new=2)
    

    #next up: connect and note