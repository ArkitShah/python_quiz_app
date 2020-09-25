import random
import re
import tkinter
from tkinter import *
import csv


global user_answer, correct_answer
indexes = []
user_answer = []
questions = []
answers_choice = []
correct_answer = []


with open('quiz.csv', 'r') as file:
    reader = csv.reader(file)
    header = 0
    column_names = []
    for row in reader:
        if header == 0:
            column_names.append(row)
            header = 1
        else:
            questions.append(row[1])
            temp = [row[2], row[3], row[4], row[5]]
            answers_choice.append(temp)
            correct_answer.append(int(row[6]))


def generate_question_numbers():
    global indexes
    while len(indexes) < len(questions):
        x = random.randint(0, len(questions)-1)
        if x not in indexes:
            indexes.append(x)
        else:
            continue


ques = 1


def show_result(score):
    labelQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelResult = Label(root,
                        font=('Times', 20),
                        text='You scored ' + str(score) + ' out of ' + str(len(questions)) + ' marks !',
                        background='#ffffff')
    labelResult.pack(pady=(200, 10))


def calculate_score():
    global indexes, user_answer, correct_answer
    x = 0
    score = 0
    for index in indexes:
        if user_answer[x] == correct_answer[index]:
            score += 1
        x += 1
    show_result(score)


def selected():
    global radiovar, user_answer, labelQuestion, r1, r2, r3, r4, ques
    x = radiovar.get()
    user_answer.append(x)
    if ques < len(questions):
        labelQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calculate_score()


def start_quiz():
    global labelQuestion, r1, r2, r3, r4
    labelQuestion = Label(root,
                          text=questions[indexes[0]],
                          font=('Times', 16),
                          justify='center',
                          wraplength=400,
                          width=500,
                          background='#ffffff')
    labelQuestion.pack(pady=(100, 30))
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(root,
                     text=answers_choice[indexes[0]][0],
                     font=('Times', 14),
                     value=0,
                     variable=radiovar,
                     command=selected,
                     background='#ffffff')
    r1.pack(pady=5)
    r2 = Radiobutton(root,
                     text=answers_choice[indexes[0]][1],
                     font=('Times', 14),
                     value=1,
                     variable=radiovar,
                     command=selected,
                     background='#ffffff')
    r2.pack(pady=5)
    r3 = Radiobutton(root,
                     text=answers_choice[indexes[0]][2],
                     font=('Times', 14),
                     value=2,
                     variable=radiovar,
                     command=selected,
                     background='#ffffff')
    r3.pack(pady=5)
    r4 = Radiobutton(root,
                     text=answers_choice[indexes[0]][3],
                     font=('Times', 14),
                     value=3,
                     variable=radiovar,
                     command=selected,
                     background='#ffffff')
    r4.pack(pady=5)


def start_pressed():
    labelRules.destroy()
    labelIconImage.destroy()
    labelInstructions.destroy()
    buttonStart.destroy()
    generate_question_numbers()
    start_quiz()


root = tkinter.Tk()
root.title("Aptitude Test")
root.geometry("800x600")
# Uncomment the below line to prevent the user from maximizing or resizing the window
# root.resizable(0, 0)
root.config(background='#ffffff')

icon = PhotoImage(file='quiz icon.png')
labelIconImage = Label(root,
                       image=icon,
                       background='#ffffff')
labelIconImage.pack(pady=(100, 40))

startButtonIcon = PhotoImage(file='start button.png')
buttonStart = Button(root,
                     image=startButtonIcon,
                     relief=FLAT,
                     border=0,
                     background='#ffffff',
                     command=start_pressed)
buttonStart.pack()

labelInstructions = Label(root,
                          text='Read the Instructions and\nClick on START once you are ready!',
                          background='#ffffff',
                          font=('Times', 14),
                          justify='center')
labelInstructions.pack(pady=(10, 70))

labelRules = Label(root,
                   text='All the questions are compulsory.\nYou will get 60 seconds to solve each question.\n' +
                        'Once you have selected the option, it cannot be changed.\nSo think before you answer.\n' +
                        'BEST OF LUCK!',
                   font=('Times', 14),
                   width=150,
                   background='#000000',
                   foreground='#ffffff')
labelRules.pack()

root.mainloop()
