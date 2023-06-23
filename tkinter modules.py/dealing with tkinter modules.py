import tkinter
window = tkinter.Tk()
# renaming the title of the windows
window.title("THE BADDEST")
# pack is used to show the object in the window
#Label =tkinter.Label(window, text="hello dude ").pack()
#erc =  tkinter.Label(window, text ="the beddest!").pack()
#erc.grid(column = 1, row = 1)

txt = tkinter.Entry(window, width=10)

def cliicked():
     res = "it has been clicked jhus chill it "
     i1.configure(text= res )
bt = tkinter.Button(window=" enter ", command=cliicked()).pack()










#window.geometry("300*200")




window.mainloop()