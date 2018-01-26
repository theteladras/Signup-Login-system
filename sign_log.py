# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:48:07 2018

@author: samsung pc
"""

from tkinter import *
import os
extfile = 'extfilee.temp'

def Signup():
    global uname
    global upwd
    global root
    
    root = Tk()
    root.title('Signup')
    header = Label(root, text = 'Please fill the signup fields!\n')
    header.grid(row=0, column=0, sticky=E)
    unameLabel = Label(root, text = 'Username: ')
    unameLabel.grid(row=1, column=0, sticky=W)
    upwdLabel = Label(root, text = 'Password: ')
    upwdLabel.grid(row=2, column=0, sticky=W)
    uname = Entry(root)
    uname.grid(row=1, column=1)
    upwd = Entry(root, show='*')
    upwd.grid(row=2, column=1)
    signupBtn = Button(root, text = 'Signup', command = signupFunction)
    signupBtn.grid(row=3, column=0, padx = (100,100), pady=(10,10),columnspan=3, sticky=W)
    root.mainloop()
    
def signupFunction():
    with open(extfile, 'w') as file:
        file.write(uname.get())
        file.write('\n')
        file.write(upwd.get())
        file.close()
    root.destroy()
    Login()
    
def Login():
    global unameLogin
    global upwdLogin
    global loginRoot
    
    loginRoot = Tk()
    loginRoot.title('Login')
    intruction = Label(loginRoot, text='Please fill in and Login\n')
    intruction.grid(sticky=E)
    unameLabel = Label(loginRoot, text = 'Username: ')
    unameLabel.grid(row=1, column=0, sticky=W)
    upwdLabel = Label(loginRoot, text = 'Password: ')
    upwdLabel.grid(row=2, column=0, sticky=W)
    unameLogin = Entry(loginRoot)
    unameLogin.grid(row=1, column=1)
    upwdLogin = Entry(loginRoot, show='*')
    upwdLogin.grid(row=2, column=1)
    loginBtn = Button(loginRoot, text = 'Login', command = verify)
    loginBtn.grid(columnspan=2, sticky=W)
    loginRoot.mainloop()
    
def verify():
    with open(extfile) as file:
        data = file.readlines()
        username = data[0].rstrip()
        password = data[1].rstrip()
        if unameLogin.get() == username and upwdLogin.get() == password:
            userRoot = Tk()
            userRoot.title('Profile')
            userRoot.geometry('150x150')
            info = Label(userRoot, text='\n[+] Logged In')
            info.pack()
            r.mainloop()
        else:
            userRoot = Tk()
            userRoot.title('D:')
            userRoot.geometry('150x150')
            info = Label(userRoot, text='\n[!] Invalid Login')
            info.pack()
            userRoot.mainloop()
            
def DelUser():
    os.remove(extfile)
    loginRoot.destroy()
    Signup()
    
if os.path.isfile(extfile):
    Login()
else:
    Signup()
    
    
    
    