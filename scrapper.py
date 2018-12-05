#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import hashlib
import sys
import re

#This program was created by Nicholas Graca
#Its job is to scrap a website looking for all the links
#However, it cannot get the same link twice 
#and it can not go off the origin website given

#This function will hash the page and see if we have already been there
#If it hasnt been there it will add it to the list of links 
#It also checks if the link is broken and if it goes off the original domain
def check():
        for link in page.findAll('a'):
                nexlink = link.get('href')
                if(nexlink == None or nexlink[0][0] == '#'):
                        continue
                temp = urlparse(nexlink).hostname
                if (nexlink[0][0] == '/'):
                        nexlink = oglink + nexlink
                        try:
                                checkhtml = urlopen(nexlink)
                        except:
                                if(nexlink not in broken):
                                        broken.append(nexlink)
                                continue
                        nexpage = BeautifulSoup(checkhtml, features="lxml")
                        h = hashlib.sha256(nexpage.encode()).hexdigest()
                        if (h not in hashes ):
                                links.append(nexlink)
                                hashes.append(h)
                        continue
                if(temp != root):
                        if(nexlink not in foreign):
                                foreign.append(nexlink)
                        continue
                try:
                        checkhtml = urlopen(nexlink)
                except:
                        if(nexlink not in broken):
                                broken.append(nexlink)
                        continue
                nexpage = BeautifulSoup(checkhtml, features="lxml")
                h = hashlib.sha256(nexpage.encode()).hexdigest()
                if (h not in hashes ):
                        links.append(nexlink)
                        hashes.append(h)
#This is were it all starts
out = 0
broke = 0
oglink = "https://freelake.org"
root = urlparse(oglink).hostname

#this if checks for command line arguments
if(len(sys.argv) > 1):
        i = 0
        while i < len(sys.argv):
                de = sys.argv[i]
                if(de == '-o'):
                        output = sys.argv[i+1]
                        out = 1
                elif(de == '-l'):
                        root = sys.argv[i+1]
                        
                elif(de == '-m'):
                        broke = 1
                i = i + 1
html = urlopen(oglink)
page = BeautifulSoup(html,features="lxml")
ogh = hashlib.sha256(page.encode()).hexdigest()
links= []
broken = []
foreign = []
hashes = []
hashes.append(ogh)
links.append(oglink)

#This is the loop that goes through all the links we need to go to
for l in links:
        temp = urlparse(l).hostname
        if (temp != root):
                if(l not in foreign):
                        foreign.append(l)
                continue
        else:
                try:
                        html = urlopen(l)
                except:
                        if(l not in broken):
                                broken.append(l)
                        continue
                page = BeautifulSoup(html,features="lxml")
                check()

#Everything below here handles the output whether it should be in a file or stdout and what it should output
if(out == 1):
        if(broke == 1 ):
                f = open(output, 'w')
                f.write("All the exceptable links: " + str(links) + "\n")
                f.close()
        else:
                f = open(output, 'w')
                f.write("All the exceptable links: " + str(links) + "\n")
                f.write("All the broken links: " + str(broken) + "\n")
                f.write("All the foreign links: " + str(foreign) + "\n")
                f.close()
else:
        if(broke == 1):
                print("All the exceptable links: " + str(links))
        else:
                print("All the exceptable links: " + str(links)) 
                print("All the broken links: " + str(broken))
                print("All the foreign links: " + str(foreign))
