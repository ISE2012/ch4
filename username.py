# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:17:00 2020

@author: ucobiz
"""

# get user’s first and last names
first = input("Please enter your first name: ")
last  = input("Please enter your last name:  ")

# concatenate first initial with 7 chars of last name
uname = first[0].lower() + last[:7].lower()
print("Your username is: ", uname)
