from tkinter import*

root =Tk()
root.title('BillEase (retail billing system)')   #title of the window
root.geometry('1400x1470')       #change the size of widow so we use geometry method('widthxheight)
root.iconbitmap('pay_cash_payment_money_dollar_bill_icon_143267.ico') #by default the icon is leaf so we change the icon using method iconbitmap
root.resizable(0,0)
#-------------          HEADING LABEL(BILL EASE)        ----------------------------------------------------
#add font ,background color,font color for text, than add border (bd)to label in x-direction
headingLabel=Label(root,text='BillEase (Retail Billing System)',
                   font=('times new roman',30,'bold'),bg='steel blue',fg='midnight blue',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)       #position of label, so it simply add label in top fill=X is for completely fill label on x-axis


#----------------------------------                        CUSTOMER DETAILS LABEL FRAME         --------------------------------------------------------------------------:
customer_detail_frame=LabelFrame(root,text='Customer Details',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
customer_detail_frame.pack(fill=X,pady=5)

#<----------|     NAME        |--------->
dateLabel=Label(customer_detail_frame,text='Date',font=('times new roman',14,'bold'),bg='light goldenrod',fg='brown')
dateLabel.grid(row=0,column=0,padx=20)

#<----------|     NAME ENTRY      |---------->
dateEntry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=21)
dateEntry.grid(row=0,column=1,padx=8)

#<----------|     PHONE       |---------->
PhoneLabel=Label(customer_detail_frame,text='Phone No.',font=('times new roman',14,'bold'),bg='light goldenrod',fg='brown')
PhoneLabel.grid(row=0,column=2,padx=20,pady=2)

#<----------|     PHONE ENTRY     |---------->
PhoneEntry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=21)
PhoneEntry.grid(row=0,column=3,padx=8)

#<----------|     BILL_NO     |---------->
Bill_noLabel=Label(customer_detail_frame,text='Bill No.',font=('times new roman',14,'bold'),bg='light goldenrod',fg='brown')
Bill_noLabel.grid(row=0,column=4,padx=20,pady=2)

#<----------|     BILL_NO ENTRY       |---------->
Bill_noEntry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=21)
Bill_noEntry.grid(row=0,column=5,padx=8)

#<----------|     SEARCH BUTTON       |---------->
searchButton=Button(customer_detail_frame,text='SEARCH',font=('arial',11,'bold'),bd=10,width=11)
searchButton.grid(row=0,column=6,padx=35,pady=20)


#----------------------------------                        COSMATICS LABEL FRAME         --------------------------------------------------------------------------:
productFrame=Frame(root)
productFrame.pack(pady=5)

cosmaticFrame=LabelFrame(productFrame,text='Cosmatics',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
cosmaticFrame.grid(row=0,column=0)
#.......................................................BATH SOAP............................................................ 
bathSoapLabel=Label(cosmaticFrame,text='Bath Soap',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
bathSoapLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')

bathSoap_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
bathSoap_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')
#........................................................FACE CREAM..........................................................
faceCreamLabel=Label(cosmaticFrame,text='Face Cream',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
faceCreamLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')

faceCream_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
faceCream_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')
#........................................................FACE WASH..........................................................
faceWashLabel=Label(cosmaticFrame,text='Face Wash',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
faceWashLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')

faceWash_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
faceWash_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')
#........................................................HAIR SPRAY..........................................................
hairSprayLabel=Label(cosmaticFrame,text='Hair Spray',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
hairSprayLabel.grid(row=3,column=0,pady=10,padx=20,sticky='w')

hairSpray_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
hairSpray_Entry.grid(row=3,column=1,pady=10,padx=20,sticky='w')
#........................................................HAIR WASH..........................................................
hairWashLabel=Label(cosmaticFrame,text='Hair Wash',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
hairWashLabel.grid(row=4,column=0,pady=10,padx=20,sticky='w')

hairWash_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
hairWash_Entry.grid(row=4,column=1,pady=10,padx=20,sticky='w')
#........................................................BODY LOTION..........................................................
bodyLotionLabel=Label(cosmaticFrame,text='Body Lotion',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
bodyLotionLabel.grid(row=5,column=0,pady=10,padx=20,sticky='w')

bodyLotion_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
bodyLotion_Entry.grid(row=5,column=1,pady=10,padx=20,sticky='w')



grossFrame=LabelFrame(productFrame,text='Grocery',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
grossFrame.grid(row=0,column=1)
#.......................................................    RICE    ............................................................ 
RiceLabel=Label(grossFrame,text='Rice',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
RiceLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')

Rice_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Rice_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')
# #........................................................ OIL ..........................................................
oilLabel=Label(grossFrame,text='Oil',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
oilLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')

oil_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
oil_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')
# #........................................................ DALL ..........................................................
dallLabel=Label(grossFrame,text='Dall',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
dallLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')

dall_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
dall_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')
# #........................................................      WHEAT   ..........................................................
wheatLabel=Label(grossFrame,text='Wheat',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
wheatLabel.grid(row=3,column=0,pady=10,padx=20,sticky='w')

wheat_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
wheat_Entry.grid(row=3,column=1,pady=10,padx=20,sticky='w')
# #........................................................     SUGAR   ..........................................................
sugarLabel=Label(grossFrame,text='Sugar',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
sugarLabel.grid(row=4,column=0,pady=10,padx=20,sticky='w')

sugar_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
sugar_Entry.grid(row=4,column=1,pady=10,padx=20,sticky='w')
# #........................................................     TEA     ..........................................................
TeaLabel=Label(grossFrame,text='Tea',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
TeaLabel.grid(row=5,column=0,pady=10,padx=20,sticky='w')

Tea_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Tea_Entry.grid(row=5,column=1,pady=10,padx=20,sticky='w')



# -----------------------------------------------         DRINK   -------------------------------------------------------------

drinkFrame=LabelFrame(productFrame,text='Cold Drinks',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
drinkFrame.grid(row=0,column=2)
#.......................................................    COCA COLA    ............................................................ 
ColaLabel=Label(drinkFrame,text='Coco Cola',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
ColaLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')

Cola_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Cola_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')
#.......................................................    MAZA    ............................................................ 
mazaLabel=Label(drinkFrame,text='Maza',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
mazaLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')

maza_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
maza_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')
#.......................................................    PEPSI    ............................................................ 
PepsiLabel=Label(drinkFrame,text='Pepsi',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
PepsiLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')

Pepsi_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Pepsi_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')
#.......................................................    SPRITE    ............................................................ 
SpriteLabel=Label(drinkFrame,text='Sprite',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
SpriteLabel.grid(row=3,column=0,pady=10,padx=20,sticky='w')

Sprite_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Sprite_Entry.grid(row=3,column=1,pady=10,padx=20,sticky='w')
#.......................................................    DEW    ............................................................ 
DewLabel=Label(drinkFrame,text='Dew',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
DewLabel.grid(row=4,column=0,pady=10,padx=20,sticky='w')

Dew_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Dew_Entry.grid(row=4,column=1,pady=10,padx=20,sticky='w')
#.......................................................    FROOTI    ............................................................ 
FrootiLabel=Label(drinkFrame,text='Frooti',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
FrootiLabel.grid(row=5,column=0,pady=10,padx=20,sticky='w')

Frooti_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Frooti_Entry.grid(row=5,column=1,pady=10,padx=20,sticky='w')

# ******************************************        BILL FRAME          *********************************************************

billFrame=Frame(productFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=15)

billareaLabel=Label(billFrame,text="Bill Area",font=('times new roman',15,'bold'),bd=8,relief=GROOVE)
billareaLabel.pack(fill=X)


scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)


textArea=Text(billFrame,height=18,width=60,yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.config(command=textArea.yview)


BillMenueFrame=LabelFrame(root,text='Bill Menu',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
BillMenueFrame.pack()

cosPriceLabel=Label(BillMenueFrame,text='Cosmatic Price',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
cosPriceLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')
cosPrice_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
cosPrice_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')

grossPriceLabel=Label(BillMenueFrame,text='Grocery Price',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
grossPriceLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')
grossPrice_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
grossPrice_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')

coldDrinkLabel=Label(BillMenueFrame,text='Cold Drink Price',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
coldDrinkLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')
coldDrink_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
coldDrink_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')

cosTaxLabel=Label(BillMenueFrame,text='Cosmatic Tax',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
cosTaxLabel.grid(row=0,column=2,pady=10,padx=20,sticky='w')
cosTax_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
cosTax_Entry.grid(row=0,column=3,pady=10,padx=20,sticky='w')

grossTaxLabel=Label(BillMenueFrame,text='Grocery Tax',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
grossTaxLabel.grid(row=1,column=2,pady=10,padx=20,sticky='w')
grossTax_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
grossTax_Entry.grid(row=1,column=3,pady=10,padx=20,sticky='w')

coldTaxLabel=Label(BillMenueFrame,text='Cold Drink Tax',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
coldTaxLabel.grid(row=2,column=2,pady=10,padx=20,sticky='w')
coldTax_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
coldTax_Entry.grid(row=2,column=3,pady=10,padx=20,sticky='w')

buttonFrame=Frame(BillMenueFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton = Button(buttonFrame,text="Total",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=7,pady=5)
totalButton.grid(row=0,column=0,pady=10,padx=10)

billButton = Button(buttonFrame,text="Bill",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=7,pady=5)
billButton.grid(row=0,column=1,pady=10,padx=10)

emailButton = Button(buttonFrame,text="Email",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=7,pady=5)
emailButton.grid(row=0,column=2,pady=10,padx=10)

printButton = Button(buttonFrame,text="Print",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=7,pady=5)
printButton.grid(row=0,column=3,pady=10,padx=10)

clearButton = Button(buttonFrame,text="Clear",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=7,pady=5)
clearButton.grid(row=0,column=4,pady=10,padx=10)

root.mainloop()   # it move vry fast so it help to viewing our window

