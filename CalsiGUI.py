from tkinter import *
root =Tk()
root.title("Calculator")
root.configure(bg='white')
root.geometry("356x390")
root.resizable(0,0)

op=Frame(root)
op.grid()

entry=Entry(op,font=('arial',14,"bold"),bd=5,width=22)
entry.grid(row=1,column=1)

inputLabel=Label(op,text='Input',font=('arial',12,"bold"),width=8,height=2,bg='sky blue',fg='blue')
inputLabel.grid(row=1,column=0,padx=2,pady=5)

entry2=Entry(op,font=('arial',14,"bold"),bd=5,width=22)
entry2.grid(row=2,column=1)

outputLabel=Label(op,text='Result',font=('arial',12,"bold"),width=8,height=2,bg='sky blue',fg='blue')
outputLabel.grid(row=2,column=0,padx=2,pady=5)

operation=Frame(root)
operation.grid()

button1=Button(operation,text="7",font=('arial',16,"bold"),width=8,height=1)
button1.grid(row=3,column=0,padx=2,pady=2)
button2=Button(operation,text="8",font=('arial',16,"bold"),width=8,height=1)
button2.grid(row=3,column=1,padx=2,pady=2)
button3=Button(operation,text="9",font=('arial',16,"bold"),width=8,height=1)
button3.grid(row=3,column=2,padx=2,pady=2)
button4=Button(operation,text="4",font=('arial',16,"bold"),width=8,height=1)
button4.grid(row=4,column=0,padx=2,pady=2)
button5=Button(operation,text="5",font=('arial',16,"bold"),width=8,height=1)
button5.grid(row=4,column=1,padx=2,pady=2)
button6=Button(operation,text="6",font=('arial',16,"bold"),width=8,height=1)
button6.grid(row=4,column=2,padx=2,pady=2)
button7=Button(operation,text="1",font=('arial',16,"bold"),width=8,height=1)
button7.grid(row=5,column=0,padx=2,pady=2)
button8=Button(operation,text="2",font=('arial',16,"bold"),width=8,height=1)
button8.grid(row=5,column=1,padx=2,pady=2)
button9=Button(operation,text="3",font=('arial',16,"bold"),width=8,height=1)
button9.grid(row=5,column=2,padx=2,pady=2)
button10=Button(operation,text="+",font=('arial',16,"bold"),width=8,height=1,bg="sky blue",fg='midnight blue')
button10.grid(row=6,column=0,padx=2,pady=2)
button11=Button(operation,text="-",font=('arial',16,"bold"),width=8,height=1,bg="sky blue",fg='midnight blue')
button11.grid(row=6,column=1,padx=2,pady=2)
button12=Button(operation,text="*",font=('arial',16,"bold"),width=8,height=1,bg="sky blue",fg='midnight blue')
button12.grid(row=6,column=2,padx=2,pady=2)
button13=Button(operation,text="/",font=('arial',16,"bold"),width=8,height=1,bg="sky blue",fg='midnight blue')
button13.grid(row=7,column=0,padx=2,pady=2)
button14=Button(operation,text="%",font=('arial',16,"bold"),width=8,height=1,bg="sky blue",fg='midnight blue')
button14.grid(row=7,column=1,padx=2,pady=2)
button15=Button(operation,text="=",font=('arial',16,"bold"),width=8,height=1,bg="midnight blue",fg='white')
button15.grid(row=7,column=2,padx=2,pady=2)

Start_button=Button(operation,text="START",font=('arial',12,"bold"),width=10,height=1,fg='white',bg='orange')
Start_button.grid(row=8,column=0,padx=3,pady=5)

Close_button=Button(operation,text="END",font=('arial',12,"bold"),width=10,height=1,fg='white',bg='orange')
Close_button.grid(row=8,column=1,padx=3,pady=5)

Clear_button=Button(operation,text="CLEAR",font=('arial',12,"bold"),width=10,height=1,fg='white',bg='orange')
Clear_button.grid(row=8,column=2,padx=3,pady=5)

root.mainloop()