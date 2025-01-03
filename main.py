from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for elements in range(nr_letters)]
    password_numbers = [random.choice(numbers) for elements in range(nr_symbols)]
    password_symbols = [random.choice(symbols) for elements in range(nr_numbers)]


    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
        try:
            with open("password_data.json", "r") as data_file:
                # Reading Old Data
                data = json.load(data_file)
    
        except FileNotFoundError:
            with open("password_data.json", "w") as data_file:
                #Creating New Data File, if it does not exist!
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("password_data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("password_data.json", "r") as search_file:
            data = json.load(search_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error Found", message="Error Reading the file")
    else:
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"The {website} does not exist in the file.")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image = mypass_img)
canvas.grid(column= 1, row = 0)

website_label = Label(text="Website:", font=("Courier", 12, "bold"))
website_label.grid(column = 0, row = 1)

email_label = Label(text="Email/Username:", font=("Courier", 12, "bold"))
email_label.grid(column = 0 , row =2)

password_label = Label(text="Password:", font=("Courier", 12, "bold"))
password_label.grid(column = 0 , row = 3)

website_entry = Entry(width=35)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(0, "myemail@hotmail.com")

password_entry = Entry(width=21)
password_entry.grid(column = 1, row = 3)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column = 2, row = 3)

add_button = Button(text="Add", width=36, command= save)
add_button.grid(column = 1, row = 4, columnspan = 2)








window.mainloop()