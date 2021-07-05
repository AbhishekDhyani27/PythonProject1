# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:23:40 2021

@author: dhyani
"""

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))