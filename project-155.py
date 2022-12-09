# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6  2022

@author: User
"""

from tkinter import *
import random
root=Tk()
root.title("random_bg")
root.geometry("400x400")
dictionary = {'colours':['maroon1','lawn green', 'magenta2', 'purple1', 'springgreen2','chocolate1','deeppink', 'cyan']}


def ran_bg():
    random_colour = random.randint(0,7)
    bg=dictionary["colours"][random_colour]
    
    print((bg))
    root.configure(background=dictionary["colours"][random_colour])
    


btn = Button(root, text="Change Background", bg="lime", command=ran_bg)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()