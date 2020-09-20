
from tkinter import*
from random import choice

root = Tk()
root.title("Enter your name and get a lucky matra for today :)")

entry1 = Entry(root, width=15)

#the place where the user sees the name 
def myClick(number):
	current =entry1.get()
	entry1.delete(0, END)
	entry1.insert(0, str(current) + str(number))

#gathering of the quotes 		
quotes = "Dwell on the beauty of life.",\
         "Watch the stars, and see yourself ",\
         "Everything we hear is an opinion",\
		 "Never let the future disturb you",\
		 "If it is not true do not say it",\
		 "Reject your sense of injury ",\
		 "Look well into thyself",\
		 "The best answer to anger is silence",\
         "Be alive, think, enjoy, and love ..."

#output display 
def myOut():
	myOut = Label(root, text = "Hi " + entry1.get() + " Mantra for you is : " +choice(quotes), fg = "red", bg="yellow")
	myOut.grid(row =0, column =3, columnspan = 10)
	

#attempting to sum the vaule of each alphabet in the name 
def addd():
	first_number =entry1.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	entry1.delete(0, END)
	

#creating the keyboard for the user to keep their name 
myClick1 = Button(root, text="A", pady =20, padx =20, command = lambda:myClick("A"))
myClick2 = Button(root, text="B", pady =20, padx =20, command = lambda:myClick("B"))
myClick3 = Button(root, text="C", pady =20, padx =20, command = lambda:myClick("C"))
myClick4 = Button(root, text="D", pady =20, padx =20, command = lambda:myClick("D"))  
myClick5 = Button(root, text="E", pady =20, padx =20, command = lambda:myClick("E"))
myClick6 = Button(root, text="F", pady =20, padx =20, command = lambda:myClick("F"))
myClick7 = Button(root, text="G", pady =20, padx =20, command = lambda:myClick("G"))
myClick8 = Button(root, text="H", pady =20, padx =20, command = lambda:myClick("H"))
myClick9 = Button(root, text="I", pady =20, padx =20, command = lambda:myClick("I"))
myClick10 = Button(root, text="J", pady =20, padx =20, command = lambda:myClick("J"))
myClick11 = Button(root, text="K", pady =20, padx =20, command = lambda:myClick("K"))
myClick12 = Button(root, text="L", pady =20, padx =20, command = lambda:myClick("L"))
myClick13 = Button(root, text="M", pady =20, padx =20, command = lambda:myClick("M"))
myClick14 = Button(root, text="N", pady =20, padx =20, command = lambda:myClick("N"))  
myClick15 = Button(root, text="O", pady =20, padx =20, command = lambda:myClick("O"))
myClick16 = Button(root, text="P", pady =20, padx =20, command = lambda:myClick("P"))
myClick17 = Button(root, text="Q", pady =20, padx =20, command = lambda:myClick("Q"))
myClick18 = Button(root, text="R", pady =20, padx =20, command = lambda:myClick("R"))
myClick19 = Button(root, text="S", pady =20, padx =20, command = lambda:myClick("S"))
myClick20 = Button(root, text="T", pady =20, padx =20, command = lambda:myClick("T"))
myClick21 = Button(root, text="U", pady =20, padx =20, command = lambda:myClick("U"))
myClick22 = Button(root, text="V", pady =20, padx =20, command = lambda:myClick("V"))
myClick23 = Button(root, text="W", pady =20, padx =20, command = lambda:myClick("W"))
myClick24 = Button(root, text="X", pady =20, padx =20, command = lambda:myClick("X"))  
myClick25 = Button(root, text="Y", pady =20, padx =20, command = lambda:myClick("Y"))
myClick26 = Button(root, text="Z", pady =20, padx =20, command = lambda:myClick("Z"))

myClick27 = Button(root, text=" Todays Mantra", pady =20, padx =100,  command = myOut, fg = "blue", bg="orange")


#showing it in the screen
entry1.grid(row =0, column =0, padx = 10, pady = 2, columnspan = 3)

myClick17.grid(row =1, column = 1)
myClick23.grid(row =1, column = 2)
myClick5.grid(row =1, column = 3)
myClick18.grid(row =1, column = 4)
myClick20.grid(row =1, column = 5)
myClick25.grid(row =1, column = 6)
myClick21.grid(row =1, column = 7)
myClick9.grid(row =1, column = 8)
myClick15.grid(row =1, column = 9)
myClick16.grid(row =1, column = 10)

myClick1.grid(row =2, column = 2)
myClick19.grid(row =2, column = 3)
myClick4.grid(row =2, column = 4)
myClick6.grid(row =2, column = 5)
myClick7.grid(row =2, column = 6)
myClick8.grid(row =2, column = 7)
myClick10.grid(row =2, column = 8)
myClick11.grid(row =2, column = 9)
myClick12.grid(row =2, column = 10)

myClick26.grid(row =3, column = 2)
myClick24.grid(row =3, column = 3)
myClick3.grid(row =3, column = 4)
myClick22.grid(row =3, column = 5)
myClick2.grid(row =3, column = 6)
myClick14.grid(row =3, column = 7)
myClick13.grid(row =3, column = 8)

myClick27.grid(row =4, column = 1, columnspan = 10)


root.mainloop()

