# Import required library
from tkinter import *

# Initialize variable
backgroundColor = "#FFFFFF"

# Initialize the UI variables
calcUI = Tk()
calcUI.title("CASIO 991-Std")
calcUI.geometry("250x300")
calcUI.configure(background=backgroundColor)

display_values = StringVar()

def clear_values():
    display_values.set="0"

# Add the entry widget for display
calcDisplay = Entry(calcUI,bg="light blue",borderwidth=5, width=15,font=('calibre',20,'normal'),justify=RIGHT,textvariable=display_values).grid(row=0,column=0,sticky=W,padx=10,pady=15)

button_Neg = Button(calcUI,bg='light gray',text="+/-",height = 2,width=6).grid(row=1,column=0,sticky=W, padx=10,pady=1)
button_Del = Button(calcUI,bg='light gray',text="Del",height = 2,width=6).grid(row=1,column=0,sticky=W,padx=68,pady=1)
button_C = Button(calcUI,bg='light gray',text="C",height = 2,width=6).grid(row=1,column=0,sticky=W,padx=126,pady=1)
button_CE = Button(calcUI,bg='light gray',text="CE",height = 2,width=6,command=clear_values).grid(row=1,column=0,sticky=W,padx=184,pady=1)

button_7 = Button(calcUI,bg='light gray',text="7",height = 2,width=6).grid(row=2,column=0,sticky=W, padx=10,pady=1)
button_8 = Button(calcUI,bg='light gray',text="8",height = 2,width=6).grid(row=2,column=0,sticky=W,padx=68,pady=1)
button_9 = Button(calcUI,bg='light gray',text="9",height = 2,width=6).grid(row=2,column=0,sticky=W,padx=126,pady=1)
button_Div = Button(calcUI,bg='light gray',text="/",height = 2,width=6).grid(row=2,column=0,sticky=W,padx=184,pady=1)

button_4 = Button(calcUI,bg='light gray',text="4",height = 2,width=6).grid(row=3,column=0,sticky=W, padx=10,pady=1)
button_5 = Button(calcUI,bg='light gray',text="5",height = 2,width=6).grid(row=3,column=0,sticky=W,padx=68,pady=1)
button_6 = Button(calcUI,bg='light gray',text="6",height = 2,width=6).grid(row=3,column=0,sticky=W,padx=126,pady=1)
button_Mul = Button(calcUI,bg='light gray',text="*",height = 2,width=6).grid(row=3,column=0,sticky=W,padx=184,pady=1)

button_1 = Button(calcUI,bg='light gray',text="1",height = 2,width=6).grid(row=4,column=0,sticky=W, padx=10,pady=1)
button_2 = Button(calcUI,bg='light gray',text="2",height = 2,width=6).grid(row=4,column=0,sticky=W,padx=68,pady=1)
button_3 = Button(calcUI,bg='light gray',text="3",height = 2,width=6).grid(row=4,column=0,sticky=W,padx=126,pady=1)
button_Sub = Button(calcUI,bg='light gray',text="-",height = 2,width=6).grid(row=4,column=0,sticky=W,padx=184,pady=1)

button_Dec = Button(calcUI,bg='light gray',text=".",height = 2,width=6).grid(row=5,column=0,sticky=W, padx=10,pady=1)
button_Zero = Button(calcUI,bg='light gray',text="0",height = 2,width=6).grid(row=5,column=0,sticky=W,padx=68,pady=1)
button_Eq = Button(calcUI,bg='light gray',text="=",height = 2,width=6).grid(row=5,column=0,sticky=W,padx=126,pady=1)
button_Add = Button(calcUI,bg='light gray',text="+",height = 2,width=6).grid(row=5,column=0,sticky=W,padx=184,pady=1)

# Loop UI for actions
calcUI.mainloop()
