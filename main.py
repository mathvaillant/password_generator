from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
  print("Generating password")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()

  with open("passwords.txt", "a") as file:
    file.write(f"{website} | {email} | {password}\n")
  file.close()

  # Clear the website and password fields
  website_entry.delete(0, END)
  password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

#Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Lables
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "matheus@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Buttons
new_password = Button(text="Generate Password", highlightthickness=0, command=gen_password)
new_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=5, columnspan=2)  



# ---------------------------- Mainloop ------------------------------- #
window.mainloop()
