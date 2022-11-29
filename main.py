from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # using the list comprehension for loop to randomize the password_letters and other variables and getting the
    # range of random numbers between the randint values established
    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    # creating a password_list to add the variables to shuffle them
    password_list = password_letters + password_symbols + password_numbers
    # random.shuffle to randomize numbers, symbols, and letters
    shuffle([password_list])

    # joining random char in password_list to random_password
    random_password = "".join(password_list)
    # inserting random_password into password text field when generate password button is hit
    password_text.insert(0, random_password)
    # import this module to copy random_password into the clipboard to automatically paste into whatever website needs
    # the new password
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # from tkinter using get method to fetch entry text
    website = website_text.get()
    username = username_text.get()
    password = password_text.get()

    # making sure user inputs info and if they don't then the error prompt will pop up, else everything will run
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="All fields are required!")
    else:
        # adding a messagebox to verify with user if info they entered is correct, if yes then it will go through the
        # writing to the data.txt file if user clicks no then it will go back to the screen for them to edit
        if_yes = messagebox.askyesno(title=website, message=f"Is this correct?\n Website: {website}\n Username/Email: "
                                                            f"{username}\n Password: {password}")
        if if_yes:
            # opening a data file using the "a" to append info to it... append creates the file
            with open("data.txt", "a") as data:
                # writing the data from the entries into the data.txt file and deleting the fields once the info is
                # accepted into data.txt file
                data.write(f"{website} | {username} | {password}\n")
                website_text.delete(0, END)
                username_text.delete(0, END)
                password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="tan")

canvas = Canvas(width=200, height=200, background="tan")
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website", background="tan")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username", background="tan")
username_label.grid(column=0, row=2)

password_label = Label(text="Password", background="tan")
password_label.grid(column=0, row=3)

# Entries
# adding columnspan to certain entries and buttons to stretch it to the next column by 2 and making the width a wider
website_text = Entry(width=40)
website_text.grid(column=1, row=1, columnspan=2)
# placing the cursor on the website entry line automatically
website_text.focus()

username_text = Entry(width=40)
username_text.grid(column=1, row=2, columnspan=2)

password_text = Entry(width=21)
password_text.grid(column=1, row=3)


# Buttons
generate_pass = Button(text="Generate Password", width=15, command=generate_password)
generate_pass.grid(column=2, row=3)

# adding command so when button is clicked the save function will activate
add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
