from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- # password generating function
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


# ---------------------------- SAVE PASSWORD ------------------------------- # password saving funtion

def save():

    website = web_entry.get()
    username = email_username_entry.get()
    password = pass_entry.get()
    new_data = {website: {
            "email" : username,
            "password" : password
            }
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Fill all the required boxes")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except (FileNotFoundError, JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0,  END)

        messagebox.showinfo(title="Password Manager", message="password saved successfully")

# ---------------------------- FIND PASSWORD ------------------------------- # fucntion to search existing passwords in manager

def find_password():
    web = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="This data file doesn't exist")

    else:
        if web in data:
            email = data[web]["email"]
            password= data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops!", message="No result matching to your input")


# ---------------------------- UI SETUP ------------------------------- # UI funtion for password manager

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
email_username_entry.insert(0, 'example@gmail.com')

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, padx=10)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, pady=10)

search_button = Button(text="Search", width=14, command=find_password, bg="DarkBlue", fg="White")
search_button.grid(row=1, column=2)

window.mainloop()
