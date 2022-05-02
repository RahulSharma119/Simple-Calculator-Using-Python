from struct import pack
from tkinter import *

#to put the input character to impact output string
def solve_event(text):
    global scvalue
    if text == '=':#to evaluate the output string when input is = or <ENTER>
        try:
            res = eval(scvalue.get())
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            res = "Invalid Input"
        scvalue.set(str(res))
        screen.update()
    elif text == 'C':#to clear the output string when input is <ESC>
        scvalue.set("")
        screen.update()
    elif text == 'B':# to delete the last string in the output string when input is <BACKSPACE>
        scvalue.set(scvalue.get()[:-1])
        screen.update()
    else:# all other authorized input is appended to output string
        scvalue.set(scvalue.get() + text)
        screen.update()

# the input is entered through GUI
def click(event):
    text = event.widget.cget("text")# cget gets the string in the text area of the button
    solve_event(text)

# the input is entered through Keyboard
def typed(event):
    text = event.char # the entered character
    # print(event)
    accepted = '0123456789+-*/.=()%' # the accepted character except for <ENTER =  \r> <ESC = \x1b> <BACKSPACE = \x08>
    if (text == '\r') or (text == '\x1b') or (text == '\x08') or (text in accepted):
        if text == '\r':
            text = "="
        if text == '\x1b':
            text = 'C'
        if text == '\x08':
            text = 'B'
        solve_event(text)

root = Tk()
root.title("Claculator")
root.geometry("450x600")

scvalue = StringVar() # the output string
scvalue.set("")
screen = Entry(root,textvariable=scvalue,font="lucida 40")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

frame1 = Frame(root,bg="grey") # 9 8 7 +
button1 = Button(frame1,text="9",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="8",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="7",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="+",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

frame1.pack(fill=X)

####################################
frame1 = Frame(root,bg="grey") # 6 5 4 -
button1 = Button(frame1,text="6",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="5",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="4",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="-",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

frame1.pack(fill=X)

###########################################
frame1 = Frame(root,bg="grey") # 3 2 1 *
button1 = Button(frame1,text="3",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="2",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="1",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="*",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

frame1.pack(fill=X)

#######################################
frame1 = Frame(root,bg="grey") # . 0 = /
button1 = Button(frame1,text=".",font="lucida 25 bold")
button1.pack(side=LEFT,padx=15,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="0",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="=",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="/",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

frame1.pack(fill=X)

###########################################
frame1 = Frame(root,bg="grey") # C ( ) %
button1 = Button(frame1,text="C",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="(",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text=")",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

button1 = Button(frame1,text="%",font="lucida 25 bold")
button1.pack(side=LEFT,padx=10,pady=20,ipadx=20)
button1.bind("<Button-1>", click)

frame1.pack(fill=X)

##################################
root.bind("<Key>",typed) # binding the keyboard input

root.mainloop()

