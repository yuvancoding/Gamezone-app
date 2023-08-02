from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

label1 = Label(root)
label2 = Label(root)

list1 = ["Bottle", "Tiffin", "ID Card", "Chocolates", "Chips", "Biscuit"]
label1["text"] = "Listed_Items : " + str(list1)


def picnic_bag():
    randomlist = random.sample(range(1,8),1)
    label2["text"] = "Put Item Number : " + str(random_list)+ " In Bag"
    
    label1.place(relx=0.5,rely=0.4,anchor=CENTER)
    
    btn=Button(root,text="Which item to put in bag?", command=picnic_bag,bg="skyblue",fg="white")               
    btn.place(relx=0.5,rely=0.4,anchor=CENTER)
    label2.place(relx=0.5,rely=0.4,anchor=CENTER)

   
    root.mainloop()