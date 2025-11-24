import main as kc
import tkinter as tk
from tkinter import messagebox

# Functions
def encrypt_callback():
  text = input_entry.get()
  key = key_entry.get()
  if text == "" or key == "":
    messagebox.showwarning("Empty", "Text or Key field is empty. Please enter some text.")
  else:
    encrypted_text = kc.encrypt(text, key)
    output_entry.config(state=tk.NORMAL) # switch to normal for changing it's content
    output_entry.delete(0, tk.END) # clear output first
    output_entry.insert(0, encrypted_text)
    output_entry.config(state=tk.DISABLED) # swtich back to disabled

def decrypt_callback():
  text = input_entry.get()
  key = key_entry.get()
  if text == "" or key == "":
    messagebox.showwarning("Empty", "Text or Key field is empty. Please enter some text.")
  else:
    decrypted_text = kc.decrypt(text, key)
    output_entry.config(state=tk.NORMAL) # switch to normal for changing it's content
    output_entry.delete(0, tk.END) # clear output first
    output_entry.insert(0, decrypted_text)
    output_entry.config(state=tk.DISABLED) # swtich back to disabled

def clear_callback():
  input_entry.delete(0, tk.END)
  key_entry.delete(0, tk.END)
  output_entry.config(state=tk.NORMAL) # switch to normal for changing it's content
  output_entry.delete(0, tk.END)
  output_entry.config(state=tk.DISABLED) # swtich back to disabled

def copy_callback():
  text_to_copy = output_entry.get()
  if text_to_copy == "":
    messagebox.showwarning("Empty", "Output is empty and is not copied.")
  else:
    root.clipboard_clear()
    root.clipboard_append(text_to_copy)
    messagebox.showinfo("Copied", "Output text is copied to clipboard.")

# Window setup
root = tk.Tk()
root.title("k_cipher GUI")
root.minsize(400, 300)

icon = tk.PhotoImage(file = "icon.png")
root.iconphoto(True, icon)

# Widgets variables
input_label = tk.Label(root, text="Text", font=("Arial", 14))
input_entry = tk.Entry(root, font=("Arial", 14))
key_label = tk.Label(root, text="Key", font=("Arial", 14))
key_entry = tk.Entry(root, font=("Arial", 14), show="*")

buttons_frame = tk.Frame(root)
encrypt_button = tk.Button(buttons_frame, text="Encrypt", font=("Arial", 12), cursor="hand2", command=encrypt_callback)
decrypt_button = tk.Button(buttons_frame, text="Decrypt", font=("Arial", 12), cursor="hand2", command=decrypt_callback)
clear_button = tk.Button(buttons_frame, text="Clear", font=("Arial", 12), cursor="hand2", command=clear_callback)

output_label = tk.Label(root, text="Encrypted/Decrypted text", font=("Arial", 14))
output_entry = tk.Entry(root, state=tk.DISABLED, font=("Arial", 14), disabledforeground="#222222")
copy_button = tk.Button(root, text="Copy", font=("Arial", 12), cursor="hand2", command=copy_callback)

# Showing widgets
input_label.pack()
input_entry.pack(padx=10, pady=5, fill="x")
key_label.pack()
key_entry.pack(padx=10, pady=5, fill="x")

buttons_frame.pack()
encrypt_button.grid(row=0, column=0, padx=5)
decrypt_button.grid(row=0, column=1, padx=5)
clear_button.grid(row=0, column=2, padx=5)

output_label.pack()
output_entry.pack(padx=10, pady=5, fill="x")
copy_button.pack()

root.mainloop()