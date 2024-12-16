from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip



#  PASSWORD GENERATOR 
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

    password_lr = [choice(letters) for _ in range(randint(8, 10))]
    password_nr = [choice(numbers) for _ in range(randint(2, 4))]
    password_sl = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_lr+password_nr+password_sl
    shuffle(password_list)

    password = ''.join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# SAVE PASSWORD 

def save():

    website = web_entry.get()
    username = email_username_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Fill all the required boxes")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f" These are the given info \nUsername: {username},\nPassword: {password} \nis it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0,  END)
            done = messagebox.showinfo(title="password manager", message="password saved successfully")
            print(done)

#  UI 

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels

label_website = Label(text="Website: ")
label_website.grid(row=1, column=0, sticky='w', padx=20)

label_username = Label(text="Email/Username: ")
label_username.grid(row=2, column=0, sticky='w', padx=20)

label_pass = Label(text="Password: ")
label_pass.grid(row=3, column=0, sticky='w', padx=20)

# Entries

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, padx=10, pady=5)
web_entry.focus() # focus is to have the cursor on the entry by default

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, padx=10, pady=5)
email_username_entry.insert(0, 'josephaltrin825@gmail.com')

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, padx=10)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, pady=10)


window.mainloop()
