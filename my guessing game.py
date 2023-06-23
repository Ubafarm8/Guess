from random import shuffle
from random import randint
from tkinter import *
login=Tk()
login.configure(bg='white')
login.title('login')
login.geometry('230x230')
label=Label(login,text="Guessing Game",font=("Ariel Bold",17),bg='blue',fg='white')
label.place(x=90,y=4)
queen=['1,','2,','3,','4,','5,','6,','7,','8,','9,','10,']
shuffle(queen)
label2=Label(login,text=(queen),bg='blue',fg='white')
label2.place(x=200, y=100)
lab=Label(login,text='pick a number from 1-10',bg='black',fg='white')
lab.place(x=200, y=230)  
global gat

def clicked(number):
     gat.delete(0,END)
     gat.insert(0,number)
def guess():
    global csv
    global hor
    global we
    genarator_of_number=randint(1,10)
    player_guess=gat.get()
    if genarator_of_number== int(player_guess):
                hor=Label(login,text='YOU WIN',fg='green',bg='white')
                hor.place(y=900, x=200)
    else:
                hor=Label(login,text='YOU SHOULD TRY BETTER',fg='red',bg='white')
                hor.place(y=900, x=200)
        
    csv=Label(login,text=f'The answer is: {genarator_of_number}',bg='white')
    csv.place(x=200,y=938,)
    but=Button(login,text='click',bg='blue'
    ,fg='white',command=guess
    ,state='disabled')
    but.place(x=300, y=800) 


def again():
    gat.delete(0,END)
    csv.place_forget()
    hor.place_forget()
    
    but=Button(login,text='click',bg='blue',fg='white',command=guess,state='normal')
    but.place(x=300, y=800)
    shuffle(queen)
    label2=Label(login,text=(queen),bg='blue',fg='white')
    label2.place(x=200, y=100) 
    


       
but=Button(login,text='click',bg='blue',fg='white',command=guess)
button1=Button(login,text='1',command=lambda:clicked(1),bg='blue',fg='white')
button2=Button(login,text='2',command=lambda:clicked(2),bg='blue',fg='white')
button3=Button(login,text='3',command=lambda:clicked(3),bg='blue',fg='white')
button4=Button(login,text='4',command=lambda:clicked(4),bg='blue',fg='white')
button5=Button(login,text='5',command=lambda:clicked(5),bg='blue',fg='white')
button6=Button(login,text='6',command=lambda:clicked(6),bg='blue',fg='white')
button7=Button(login,text='7',command=lambda:clicked(7),bg='blue',fg='white')
button8=Button(login,text='8',command=lambda:clicked(8),bg='blue',fg='white')
button9=Button(login,text='9',command=lambda:clicked(9),bg='blue',fg='white')
button10=Button(login,text='10',command=lambda:clicked(10),bg='blue',fg='white')
trya=Button(login,text='Try again',command=again,bg='black',fg='red')


trya.place(x=300,y=988)



button1.place(x=200, y=400)
button2.place(x=300, y=400)
button3.place(x=400, y=400)

button4.place(x=200, y=500)
button5.place(x=300, y=500)
button6.place(x=400, y=500)

button7.place(x=200, y=600)
button8.place(x=300, y=600)
button9.place(x=400, y=600)

button10.place(x=200, y=700)
but.place(x=300, y=800)

gat=Entry(login,borderwidth=5)



gat.place(y=300,x=200)
dem=Button(login,text='Exit',command=login.quit,bg='black',fg='red')
dem.place(y=800,x=500)



ghw=Label(login,text='created by:VIZKID.py',font=('times new roman',10),fg='black',bg='white')
ghw.place(x=300,y=1330)

login.mainloop()