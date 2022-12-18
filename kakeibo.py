import tkinter
import matplotlib.pyplot as plt
import csv
import re
from pprint import pprint

app = tkinter.Tk()
app.geometry('1200x600')



def input_page(widget):
    widget.place_forget()

    canvas_input = tkinter.Canvas(width=1200, height=600)
    canvas_input.place(x=0, y=0)

    btn1_input = tkinter.Button(canvas_input, text='Top', command=lambda: top_page(canvas_input))
    btn1_input.place(x=0, y=0)

    btn2_input = tkinter.Button(canvas_input,
                                text='入力',
                                command=lambda: csv_input())
    btn2_input.place(x=1000, y=250)

    label1_input = tkinter.Label(text='年')
    label1_input.place(x=100,y=225)

    box1_input = tkinter.Entry(canvas_input, width=10)
    box1_input.place(x=100, y=250)

    label2_input = tkinter.Label(text='月')
    label2_input.place(x=200,y=225)

    box2_input = tkinter.Entry(canvas_input, width=10)
    box2_input.place(x=200, y=250)

    label3_input = tkinter.Label(text='日')
    label3_input.place(x=300,y=225)

    box3_input = tkinter.Entry(canvas_input, width=10)
    box3_input.place(x=300, y=250)

    label4_input = tkinter.Label(text='費目')
    label4_input.place(x=400,y=225)

    box4_input = tkinter.Entry(canvas_input, width=10)
    box4_input.place(x=400, y=250)

    label5_input = tkinter.Label(text='額')
    label5_input.place(x=500,y=225)

    box5_input = tkinter.Entry(canvas_input, width=10)
    box5_input.place(x=500, y=250)

    label6_input = tkinter.Label(text='対象')
    label6_input.place(x=600,y=225)

    box6_input = tkinter.Entry(canvas_input, width=10)
    box6_input.place(x=600, y=250)

    label7_input = tkinter.Label(text='収支flag')
    label7_input.place(x=700,y=225)

    box7_input = tkinter.Entry(canvas_input, width=10)
    box7_input.place(x=700, y=250)

    label8_input = tkinter.Label(text='費目flag')
    label8_input.place(x=800,y=225)

    box8_input = tkinter.Entry(canvas_input, width=10)
    box8_input.place(x=800, y=250)

    label9_input = tkinter.Label(text='備考')
    label9_input.place(x=900,y=225)

    box9_input = tkinter.Entry(canvas_input, width=10)
    box9_input.place(x=900, y=250)

    label10_input = tkinter.Label(text='※収支flag')
    label10_input.place(x=700, y=325)

    label11_input = tkinter.Label(text='収入:1')
    label11_input.place(x=710, y=350)

    label12_input = tkinter.Label(text='支出:2')
    label12_input.place(x=710, y=375)

    label10_input = tkinter.Label(text='※費目flag')
    label10_input.place(x=800, y=325)

    label11_input = tkinter.Label(text='未実装')
    label11_input.place(x=810, y=350)

    def csv_input():
        data_input = []

        data_input.append(box1_input.get())
        data_input.append(box2_input.get())
        data_input.append(box3_input.get())
        data_input.append(box4_input.get())
        data_input.append(box5_input.get())
        data_input.append(box6_input.get())
        data_input.append(box7_input.get())
        data_input.append(box8_input.get())
        data_input.append(box9_input.get())

        with open('all_payments.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data_input)

        box1_input.delete(0, tkinter.END)
        box2_input.delete(0, tkinter.END)
        box3_input.delete(0, tkinter.END)
        box4_input.delete(0, tkinter.END)
        box5_input.delete(0, tkinter.END)
        box6_input.delete(0, tkinter.END)
        box7_input.delete(0, tkinter.END)
        box8_input.delete(0, tkinter.END)
        box9_input.delete(0, tkinter.END)





def output_page(widget):
    widget.place_forget()

    canvas_output = tkinter.Canvas(width=1200, height=600)
    canvas_output.place(x=0, y=0)

    btn1_output = tkinter.Button(canvas_output, text='Top', command=lambda: top_page(canvas_output))
    btn1_output.place(x=0, y=0)

    btn2_output = tkinter.Button(canvas_output, text='表出力', command=lambda: csv_output())
    btn2_output.place(x=500, y=125)

    btn3_output = tkinter.Button(canvas_output, text='統計', command=lambda: total_output())
    btn3_output.place(x=505, y=175)

    box1_output = tkinter.Text(canvas_output)
    box1_output.place(x=300, y=250, width=600, height=300)

    label1_output = tkinter.Label(text='年')
    label1_output.place(x=300,y=100)
    
    box2_output = tkinter.Entry(canvas_output, width=10)
    box2_output.place(x=300, y=125)

    label2_output = tkinter.Label(text='月')
    label2_output.place(x=400,y=100)

    box3_output = tkinter.Entry(canvas_output, width=10)
    box3_output.place(x=400, y=125)

    label2_output = tkinter.Label(text='※年月を指定して家計簿を表示')
    label2_output.place(x=600,y=130)

    label3_output = tkinter.Label(text='※家族の収支を表示')
    label3_output.place(x=600,y=180)


    def csv_output():
        box1_output.delete('1.0', 'end')
        data_year = box2_output.get()
        data_month = box3_output.get()

        with open('all_payments.csv', 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader, 1):
                if data_year == row[0] and data_month == row[1]:
                    data_length1 = ''
                    data_length2 = ''
                    for n in range(10-len(row[3])):
                        data_length1 += '　'
                    for n in range(2-len(row[5])):
                        data_length2 += '　'
                    box1_output.insert(str(float(i)), "{} {: >2} {: >2} {}{} {: >8} {}{} {} {} {} ".format(row[0], row[1], row[2], row[3], data_length1, row[4], row[5], data_length2, row[6], row[7], row[8]))
                    box1_output.insert(tkinter.END, '\n')

    def total_output():
        income = 0
        pay = 0
        goukei = 0
        cost = 0
        flag = 0
        count = 0
        father_income = 0
        father_pay = 0
        mother_income = 0
        mother_pay = 0
        man_income = 0
        man_pay = 0
        woman_income = 0
        woman_pay = 0
        family_income = 0
        family_pay = 0
        with open('all_payments.csv' , 'r' ) as f: #'r'=読み込み
            reader = csv.reader(f)
            for line in reader:
                count += 1
                if count == 1:
                    continue
                cost = int(line[1:][3])
                flag = int(line[1:][5])
                target = line[1:][4]
                if target == '父':
                    if flag == 1:
                        father_income += cost
                    elif flag == 2:
                        father_pay += cost
	
				
                elif target == '母':
                    if flag == 1:
                        mother_income += cost
                    elif flag == 2:
                        mother_pay += cost
	
	
	
                elif target == '長男':
                    if flag == 1:
                        man_income += cost
                    elif flag == 2:
                        man_pay += cost
	
	
	
                elif target == '長女':
                    if flag == 1:
                        woman_income += cost
                    elif flag == 2:
                        woman_pay += cost
	
	
	
                elif target == '家族':
                    if flag == 1:
                        family_income += cost
                    elif flag == 2:
                        family_pay += cost
	
	
                if flag == 1:
                    income += cost
                    goukei += cost
                elif flag == 2:
                    pay += cost
                    goukei -= cost
                else:
                    print("なんか、flagでバグってるよ。")

            box1_output.delete('1.0', 'end')
            box1_output.insert(tkinter.END, "収入{}\n".format(income))
            box1_output.insert(tkinter.END, "支出{}\n".format(pay))
            box1_output.insert(tkinter.END, "収支{}\n".format(goukei))
            box1_output.insert(tkinter.END, "父収入{}\n".format(father_income))
            box1_output.insert(tkinter.END, "父支出{}\n".format(father_pay))
            box1_output.insert(tkinter.END, "母収入{}\n".format(mother_income))
            box1_output.insert(tkinter.END, "母支出{}\n".format(mother_pay))
            box1_output.insert(tkinter.END, "長男収入{}\n".format(man_income))
            box1_output.insert(tkinter.END, "長男支出{}\n".format(man_pay))
            box1_output.insert(tkinter.END, "長女収入{}\n".format(woman_income))
            box1_output.insert(tkinter.END, "長女支出{}\n".format(woman_pay))
            box1_output.insert(tkinter.END, "家族収入{}\n".format(family_income))
            box1_output.insert(tkinter.END, "家族支出{}\n".format(family_pay))
            box1_output.insert(tkinter.END, '\n')

def top_page(widget):
    widget.place_forget()

    canvas_top = tkinter.Canvas(width=1200, height=600)
    canvas_top.place(x=0, y=0)

    btn1_top = tkinter.Button(canvas_top,
                                text='入力',
                                command=lambda: input_page(canvas_top))
    btn1_top.place(x=500, y=400, anchor=tkinter.CENTER)

    btn2_top = tkinter.Button(canvas_top,
                                text='出力',
                                command=lambda: output_page(canvas_top))
    btn2_top.place(x=700, y=400, anchor=tkinter.CENTER)

    label1_top = tkinter.Label(canvas_top, text='家計簿', fg="red", font=("", 100, "bold", "italic"))
    label1_top.place(x=75,y=150)

    label2_top = tkinter.Label(canvas_top, text='にしやがれ', fg="blue", font=("", 100, "bold", "italic"))
    label2_top.place(x=500,y=150)

canvas_top = tkinter.Canvas(width=1200, height=600)
canvas_top.place(x=0, y=0)

top_page(canvas_top)

app.mainloop()