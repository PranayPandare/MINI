from tkinter import *
import random,math,os
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('C:\\Users\\dr_an\\PycharmProjects\\QR code generator\\Details.db')
c = conn.cursor()

c.execute('SELECT * FROM Details1 ')
print(c.fetchall())
conn.commit()
conn.close()
