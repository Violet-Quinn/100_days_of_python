from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from random import choice,randint,shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)

    generated_password="".join(password_list)
    password_entry.insert(0,generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    ok_to_save = messagebox.askokcancel(title="Website",
                                        message=f"These are the details entered: \n"
                                        f"Email: {email}\nPassword: {password}\nDo you want to save?")
    if ok_to_save:
        if len(password)==0 or len(email)==0 or len(website)==0:
            messagebox.showinfo(title="Invalid Input", message="fields cannot be empty.")
        else:
            with open("saved_pass.txt","a") as file:
                file.write(f"{website} | {email} | {password}\n")
                print("Password saved")
        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)

original_image=Image.open("logo0.png")
resized_image=original_image.resize((200,200))
logo_image=ImageTk.PhotoImage(resized_image)
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

#Labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
website_entry=Entry(width=38)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=38)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"altarravik@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button=Button(text="Generate Password",width=13,command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()