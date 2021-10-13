from tkinter import*

def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

    
def btnclearDisplay():
    global operator
    operator=""
    text_input.set("")

    
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    try:
        global exp
        total=str(eval(operator))
        text_input.set(total)
        exp=""
        eq=open('answer.txt','a+')
        eq.write(total)
        eq.write('\n')
        eq.close()
    except:
        text_input.set(total)
        exp=""


x=Tk() 
x.title("calculator")
operator=""
text_input=StringVar()


txtdisplay=Entry(x,font=('ariel',20,"bold"),textvariable=text_input,bd=50,insertwidth=5,bg="white",justify="right").grid(columnspan=5)
btn1=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="1",bg="white",command=lambda:btnclick(1)).grid(row=1,column=0)
btn2=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="2",bg="white",command=lambda:btnclick(2)).grid(row=1,column=1)
btn3=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="3",bg="white",command=lambda:btnclick(3)).grid(row=1,column=2)
Addition=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="+",bg="white",command=lambda:btnclick("+")).grid(row=1,column=3)


btn4=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="4",bg="white",command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="5",bg="white",command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="6",bg="white",command=lambda:btnclick(6)).grid(row=2,column=2)
Subtraction=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="-",bg="white",command=lambda:btnclick("-")).grid(row=2,column=3)


btn7=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="7",bg="white",command=lambda:btnclick(7)).grid(row=3,column=0)
btn8=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="8",bg="white",command=lambda:btnclick(8)).grid(row=3,column=1)
btn9=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="9",bg="white",command=lambda:btnclick(9)).grid(row=3,column=2)
Multiply=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="*",bg="white",command=lambda:btnclick("*")).grid(row=3,column=3)


btn0=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="0",bg="white",command=lambda:btnclick(0)).grid(row=4,column=0)
btnEquals=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="=",bg="white",command=btnEqualsInput).grid(row=4,column=1)
btnClear=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="c",bg="white",command=btnclearDisplay).grid(row=4,column=2)
Division=Button(x,padx=16,pady=16,bd=8,fg="blue",font=("ariel",15,"bold"),text="/",bg="white",command=lambda:btnclick("/")).grid(row=4,column=3)




x.mainloop()

