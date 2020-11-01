import string
from tkinter import*
from datetime import date

#setting up the tinker
root = Tk()
root.title("LOVE METER")

a = string.ascii_lowercase
value_list1 = []
value_list2 = []

def myName():
	myOut = Label(root, text = "Its good to meet you " + name1.get(), fg = "red")
	myOut.grid(row =1, column =3)

def myName2():
	myOut = Label(root, text = "Don't worry, I will not ask 4 her phone number :)", fg = "red" ) 
	myOut.grid(row =2, column =3)



def love():
	#getting the sum of each names 
	namee = name1.get()
	lower1 = namee.lower()
	nameee = name2.get()
	lower2 = nameee.lower()
		
	for i in lower1:
		value = (a.index(i) + 1)
		value_list1.append(value)
	
	for i in lower2:
		value = (a.index(i) + 1)
		value_list2.append(value)

	sum = 0
	for i in value_list1:
		sum += i
	
	sum2 = 0
	for i in value_list2:
		sum2 += i
	
	from datetime import date

	today = date.today()
	d1 = int(today.strftime("%d%m%Y"))
		
	sum3 = 0
	for s in str(d1):
		sum3 += int(s)
	
	#so love is defined as the sum of two individual at that particular day and influenced by some constant like 10 :) 
	lovely1 = (sum + sum2 + sum3 - 10 ) / 2
	
	if lovely1 > 100:
		lovely = 100
	else: 
		lovely = lovely1
	
	#for display of the result 
	if lovely < 15:
		mylove = Label(root, text = "Are you sure, its the real name " + str(lovely) + "% of love seems low" , fg = "red", bg = "powder blue", font = ("arial", 10, "bold"))
		mylove.grid(row =0, column =0, columnspan = 2)
	elif lovely < 60:
		mylove = Label(root, text = "Go and kiss her/him, love meter shows " + str(lovely) + "% of love" , fg = "red", bg = "powder blue", font = ("arial", 10, "bold"))
		mylove.grid(row =0, column =0, columnspan = 2)
	else:
		mylove = Label(root, text = "Don't let her/him go, love meter shows " + str(lovely) + "% of love", fg = "red", bg = "powder blue", font = ("arial", 10, "bold"))
		mylove.grid(row =0, column =0, columnspan = 2)



#creating lavel
Botm1 = Button(root, text="Enter your name:", pady =10, padx =20, command = myName)
Botm2 = Button(root, text="Your partner's name:", pady =10, padx =20, command = myName2)
Botm3 = Button(root, text="Calculate our LOVE", pady =10, padx =50, command = love, fg = "blue", bg="orange")


#entering your Name
name1 = Entry(root, width=10, borderwidth = 5)
name2 = Entry(root, width=10, borderwidth = 5)

#showing it in the screen
Botm1.grid(row =1, column = 0)
Botm2.grid(row =2, column = 0)
Botm3.grid(row =4, column = 0, columnspan = 2)
name1.grid(row =1, column =1, padx = 10, pady = 2)
name2.grid(row =2, column =1, padx = 10, pady = 2)



root.mainloop()

