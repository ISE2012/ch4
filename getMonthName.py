# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:22:21 2020

@author: ucobiz
"""

def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter a month number (1-12): "))

    # compute starting position of month n in months
    pos = (n-1) * 3
    
    # grab the appropriate slice from months
    monthAbbrev = months[pos:pos+3]

    # print the result    
    print ("The month abbreviation is", monthAbbrev)

main()

