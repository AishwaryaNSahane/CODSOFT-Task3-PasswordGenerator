import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    complexity = complexity_var.get()
    characters = ''
    
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation 
    elif complexity == 5:
        characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(password_length))
    generated_password.set(password)

def reset_password():
    generated_password.set('')
    length_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Password Generator")
app.geometry("700x600")
app.configure(bg="white")

heading_label = tk.Label(app, text="Password Generator", font=("Arial", 36), bg="white",fg="darkblue")
heading_label.pack(pady=20)

user_label = tk.Label(app, text="Enter User Name :", bg="white" ,font=("arial",16),border="2px solid black")
user_label.pack(anchor=tk.W)

user_entry = tk.Entry(app)
user_entry.pack()

length_label = tk.Label(app, text="Enter Password Length:", bg="white",font=("arial",16),border="2px solid black")
length_label.pack(anchor=tk.W)

length_entry = tk.Entry(app)
length_entry.pack()

generated_password_label = tk.Label(app, text="Generated Password : ", bg="white",font=("arial",16),border="2px solid black")
generated_password_label.pack(pady=10, padx=10, anchor=tk.W)

generated_password = tk.StringVar()
generated_password_label = tk.Label(app, textvariable=generated_password, bg="white", font=("Arial", 16),border="2px solid black")
generated_password_entry = tk.Entry(app)
generated_password_label.pack()


complexity_var = tk.IntVar()
complexity_var.set(1)  

complexity_frame = tk.Frame(app, bg="white")
complexity_frame.pack()

tk.Radiobutton(complexity_frame, text="Low (letters only)", variable=complexity_var, value=1, bg="white").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(complexity_frame, text="Medium (letters and digits)", variable=complexity_var, value=2, bg="white").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(complexity_frame, text="High (letters, digits, and symbols)", variable=complexity_var, value=3, bg="white").pack(side=tk.LEFT, padx=10 ,pady=10)

generate_button = tk.Button(app, text="Generate Password", command=generate_password, bg="darkblue", fg="white",font=("Arial", 16),border="2px solid black")
generate_button.pack(pady=20)



accept_button = tk.Button(app, text="ACCEPT", bg="white", fg="darkblue",font=("Arial", 16),border="2px solid black")
accept_button.pack(pady=10)

reset_button = tk.Button(app, text="RESET", command=reset_password, bg="white", fg="darkblue",font=("Arial", 16),border="2px solid black")
reset_button.pack(pady=10)

app.mainloop()
