import os
import sqlite3 as sq
import string 
import colors as co

class functions :

    def __init__(self) :
        self.conn = sq.connect("passwords.db") # connect to database
        self.cur = self.conn.cursor()


    def signup(self,mpword):# in firt time ..
        self.cur.execute(f"UPDATE  mainpassword SET mpword = '{mpword}' ")
        self.conn.commit()


    def login(self,mpword):# every time or change ..
        result = False
        self.cur.execute("SELECT * FROM mainpassword")
        password = self.cur.fetchall()
        if mpword == password[0][0] :
            result = True
        else :
            result = False
        self.conn.commit() # To execute command in database ..
        return result
            

    def addpassword(self,title,npassword):# add pass word to database ..
        self.cur.execute(f"INSERT INTO passwords VALUES('{title}','{npassword}')")
        self.conn.commit()


    def changepassword(self,title,npassword):# change pass word already exist ..
        self.cur.execute(f"UPDATE passwords SET pword = '{npassword}' WHERE title = '{title}' ")
        self.conn.commit()


    def show(self): # display all password user save its ..
        self.cur.execute("SELECT * FROM passwords")
        data = self.cur.fetchall()
        self.conn.commit()
        n = 1
        for i in data :
            print(f" {n} , {i[0]}  : '{i[1]}'")
            n += 1


    def removepword(self,title):# delete password from database ..
        self.cur.execute(f"DELETE FROM passwords WHERE title = '{title}' ")
        self.conn.commit()


    def isvalidtitle(self,title):# is valid title / to creat new password with new title / check if title is exist ..
        self.cur.execute("SELECT title FROM passwords")
        data = self.cur.fetchall()
        self.conn.commit()
        for i in data:
            if title == i[0]:
                return False
        return True


    def isexisttitle(self,title):# is valid change / to change password for exist title / check if title is exist ..
        self.cur.execute("SELECT title FROM passwords")
        data = self.cur.fetchall()
        self.conn.commit()
        for i in data:
            if title == i[0]:
                return True
        return False


    def closedata(self):# close database ..
        self.conn.close()


    def isvalidmpword(self,mpword):#is valid main password / to creat strong main password ..
        if len(mpword) < 8 :
            return False
        return True
    

    def isfirsttime(self):# if user use the program in fist time ..
        self.cur.execute("SELECT * FROM mainpassword")
        password = self.cur.fetchall()
        self.conn.commit()
        if password[0][0] == '':
            return True
        else:
            return False
        

class Functions : # this functions use the functions from class functions  ..

    def __init__(self):
        # import class function ..
        self.func = functions()
        self.conn = sq.connect('passwords.db') # connect to database ..
        self.cur = self.conn.cursor()
        self.alpha = string.ascii_letters
        self.commands = {
                         "help":" to read the list of commands you can use .",
                         "addpw":" to add new password to save it, remmember every password needs a title .",
                         "chpw":" to change password already exist .",
                         "show":" to display passwords you saved its .",
                         "exit":" to exit program .",
                         "clear":" to clear screen .",
                         "rempw":" to remove (delete) password you already saved its .",
                         "chmpw":" to change the main passowrd .",
                         }
        

    def LogIn(self):       
        mpword = input(co.ToYellow(f"\nEnter the main password : {co.ToPink('>>')} ")) # use co.ToYellow() to coloring the string
        if self.func.login(mpword) : # Line 18 ..
            return True
        else:
            print(co.ToRed("\n   The password is wrong, try again !!"))        
            return False


    def SignUp(self):
        while True :
            mpword = input(f"Create a main password to save your files :\n  (equal or more than 8 characters) {co.ToPink('>>')} ")
            if self.func.isvalidmpword(mpword) : # Line 79 ..
                self.func.signup(mpword) # Line 13 ..
                break
            else :
                print(co.ToRed("\n   Invalide password !!"))


    def ChangeMPWord(self):
        if self.LogIn():
            sure = input (f"Are you sure to change main password :\n  ( 'y' to change, any character to exit ) {co.ToPink('>>')} ")
            # if user is sure ..
            if sure.lower() == 'y':    
                self.SignUp() # Line 124 ..
                print(co.ToLYellow("\n   Successfully completed ..."))
            else:
                print(co.ToGray("\n   Nothing changed !"))


    def OpenProgram(self): # every time the user open the program ..
        if self.func.isfirsttime() : # Line 85 ..
            self.SignUp()
        else :
            while True :
                if self.LogIn():
                    break


    def AddPassWord(self):
        if self.LogIn():
            title = input (f"Enter the title of password {co.ToPink('>>')} ")
            # check if title is exist ..
            if self.func.isvalidtitle(title): # Line 55 ..
                npword = input(f"Enter the password {co.ToPink('>>')} ")
                if title!="" and title[0] in self.alpha and len(npword) != 0 : # the first character in title must be letter ..
                   self.func.addpassword(title,npword) # Line 27 ..
                   print(co.ToLYellow('\n   Successfully completed ...'))
                else :
                    print(co.ToRed("""\n   Not seccessful there is wrong in title or password
  ( use letter in title, don't write space in title and don't enter empty password ) !!!\n"""))
            else:
                print(co.ToRed("\n   This title is already exist !!"))


    def ChangePassWord(self): # change password already exists ..
        if self.LogIn() :
            title = input (f"Enter the password's title : {co.ToPink('>>')} ")
            # check if title of password exists ..
            if self.func.isexisttitle(title): # Line 65 ..
                # select the wonted password ..
                self.cur.execute(f"SELECT * FROM passwords WHERE title='{title}'")
                passworddata = self.cur.fetchall()
                # print the details of password
                print("Your password's details :")
                print(co.ToLBlue(f"    {passworddata[0][0]} : '{passworddata[0][1]}'"))
                # ask the user if sure or not  .. # 'y' = continue ..
                sure = input (f"Do want to change this password \n( 'y' to continue, any character to exit ) : {co.ToPink('>>')} ")
                if sure.lower() == "y" :
                    # make the user enter new password ..
                    npassword = input(f"Enter the new password : {co.ToPink('>>')} ")
                    self.func.changepassword(title,npassword) # Line 35 ..
                    print(co.ToLYellow("\n   Successfully completed ..."))
                else:
                    print(co.ToGray("\n   Nothing changed ! "))
            else:
                print(co.ToRed("\n   This title is not exist !! try again !"))


    def RemPWord(self): # remove password
        if self.LogIn():
            title = input(f"Enter the password's title : {co.ToPink('>>')} ")
            # check if title exists ...
            if self.func.isexisttitle(title):
                sure = input(f"Are you sure :\n( 'y' to delete, any character to exit ) {co.ToPink('>>')} ")
                # if user is sure ...
                if sure.lower() == 'y':
                    self.func.removepword(title) # Line 44 ..
                    print(co.ToLYellow("\n   Successfully completed ..."))
                else:
                    print(co.ToGray("\n   Nothing changed ! "))
            else:
                print(co.ToRed("\n   This title is not exist !! try again !"))


    def ShowData(self): # print all password already saved ..
        if self.LogIn():
            self.func.show() # Line 35 ..


    def Help(self) : # To print all commands of program  ..
        n = self.commands # Line 103 ..
        for i in n :
            if len(i)==5:
                print(i,": ",n[i])
            else:
                print(i," : ",n[i])


    def MainPart(self): # present the information and help ..
        txt1 = co.ToLWhite('( Password Keeper )')
        txt3 = co.ToLWhite("'help'")
        txt4 = co.ToGray('to display all commands you can use .')
        txt2 = co.ToGray(f"use the command {txt3} {txt4}")
        txt6 = co.ToLWhite("'exit'")
        txt7 = co.ToGray('to quit program is better than click X button .')
        txt5 = co.ToGray(f'Enter a main password and use the program .\nNote : using the command {txt6} {txt7}')
        print(co.ToGray(f"Welcome in {txt1} {txt2} \n{txt5}"))        


    def Clear(self): # Clear screen ..
        if os.name == 'nt' : # if user use Windows ..
            os.system('cls')
        else :
            os.system('clear') # if user use Unix, MacOs or Linux  ..
        self.MainPart() # the main part must be displayed frot of user ..


    def CloseData(self): # Close database file ..
        self.func.closedata()


    def Exit(self): # exit game ..
        exit()


class main :

    def __init__(self,):
        # import class Function ..
        self.Func = Functions()

    def start(self):
        self.Func.OpenProgram() # Line 145 ..

    def main (self): # the main function ..
        Input = input(co.ToLPink("\n>>> "))
        if Input == "addpw" :
            self.Func.AddPassWord()
        elif  Input == "show" :
            self.Func.ShowData()
        elif Input == "chpw":
            self.Func.ChangePassWord()
        elif Input == "exit":
            self.Func.CloseData()
            self.Func.Exit()
        elif Input == "help":
            self.Func.Help()
        elif Input == "clear":
            self.Func.Clear()
        elif Input == "rempw":
            self.Func.RemPWord()
        elif Input == "chmpw":
            self.Func.ChangeMPWord()
        else :
            print(co.ToLGray(f"\n   '{Input}' is not recognized use 'help' to read the commands you can use !!"))
    
    def play(self):
        self.Func.MainPart()
        self.start()
        while True :
            self.main()  

'''-------------------------------------------'''

Main = main()
Main.play()