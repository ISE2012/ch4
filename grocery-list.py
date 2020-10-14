# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:53:01 2020

@author: ucobiz
"""

def main():
    print("Welcome to the Grocery Manager 1.0")
    # initialize the value and the size of our list
    grocery_list = [None]*6
    grocery_size = len(grocery_list)
    
    for n in range(grocery_size):    
        grocery_list[n] = input("Please enter your item:  ")
    
    print(grocery_list)
    
    for item in grocery_list:
        print(item)
        
main()
