import tkinter as tk

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
key_entry = tk.Entry(root, font=("Arial", 14))

buttons_frame = tk.Frame(root)
encrypt_button = tk.Button(buttons_frame, text="Encrypt", font=("Arial", 12), cursor="hand2")
decrypt_button = tk.Button(buttons_frame, text="Decrypt", font=("Arial", 12), cursor="hand2")
clear_button = tk.Button(buttons_frame, text="Clear", font=("Arial", 12), cursor="hand2")

output_label = tk.Label(root, text="Encrypted/Decrypted text", font=("Arial", 14))
output_entry = tk.Entry(root, state=tk.DISABLED, font=("Arial", 14), disabledforeground="#222222")
copy_button = tk.Button(root, text="Copy", font=("Arial", 12), cursor="hand2")

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