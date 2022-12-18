# -*- coding: utf-8 -*-

import tkinter
import requests
from bs4 import BeautifulSoup
import re

app=tkinter.Tk()

def btn_click1():
    url = "https://coronavirus.smartnews.com/jp/"
    bigdata = []

    country = txt1.get()

    html = requests.get(url+country)
    html.encoding = html.apparent_encoding
    
    soup = BeautifulSoup(html.text, "html.parser")

    for data in soup.find_all("strong"):
        data = str(data)
        data = int(re.sub("\\D", "", data))
        bigdata.append(data)

    if not bigdata:
        bigdata.append('発表待ち')
        bigdata.append('発表待ち')
    else:
        del bigdata[1]

    data = soup.find("div",class_="today")
    data = str(data)
    data = int(re.sub("\\D", "", data))
    bigdata.append(data)

    if not country:
        bigdata[0] = 'データなし'
        bigdata[1] = 'データなし'
        bigdata[2] = 'データなし'

    txt2.delete(0, tkinter.END)
    txt3.delete(0, tkinter.END)
    txt4.delete(0, tkinter.END)
    txt2.insert(tkinter.END,bigdata[0])
    txt3.insert(tkinter.END,bigdata[1])
    txt4.insert(tkinter.END,bigdata[2])


app.title('本日の新型コロナウイルス感染状況') 
app.geometry('500x250') 

label1 = tkinter.Label(text='都道府県名')
label1.place(x=50,y=55)

txt1 = tkinter.Entry(width=20)
txt1.place(x=140,y=50)

label2 = tkinter.Label(text='感染者数')
label2.place(x=50,y=150)

txt2 = tkinter.Entry(width=10)
txt2.place(x=50,y=175)

label3 = tkinter.Label(text='死亡者数')
label3.place(x=200,y=150)

txt3 = tkinter.Entry(width=10)
txt3.place(x=200,y=175)

label4 = tkinter.Label(text = '累計感染者数')
label4.place(x=350,y=150)

txt4 = tkinter.Entry(width=10)
txt4.place(x=350,y=175)

btn1 = tkinter.Button(app, text='検索', command=btn_click1)
btn1.place(x=320,y=50)


app.mainloop()