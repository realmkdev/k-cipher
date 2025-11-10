# 🔐 K-Cipher

**K-Cipher** is a simple yet effective text encryption and decryption tool written in Python.  
It uses a custom substitution cipher based on a character set and a user-provided key to securely transform text.

---

## 🚀 Features
- Encrypt and decrypt any text using a custom key.
- Works with letters, numbers, symbols, and spaces.
- Simple command-line interface.
- Fully written in pure Python (no external dependencies).

---

## 🧠 How It Works

The cipher shifts each character in your text based on:
- Its position in a predefined list of characters.
- The corresponding character in your password.
- The password length.

This makes it slightly stronger than a basic Caesar cipher, as it combines the text and key dynamically.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/realmkdev/k-cipher.git
cd k-cipher
````
OR you can download as ZIP file.

No external libraries are required — just Python 3!

---

## 🧩 Usage

Run the script directly in your terminal:

```bash
python3 main.py
```
OR
```bash
python main.py
```
based on your OS.

You’ll see a simple menu:

```
-----------------
Author: M.Kamran
-----------------
1. Encrypt
2. Decrypt
3. Exit
-----------------
Enter your option (1-3):
```

### 🔸 Example — Encryption

```
Enter your option (1-3): 1
Enter text for encryption: Hello123!
Enter the password: key
-----------------
Encrypted text (exclude outer ''): 'VmNzw>'"{'
```

### 🔹 Example — Decryption

```
Enter your option (1-3): 2
Enter encrypted text: VmNzw>'"{
Enter the password: key
-----------------
Decrypted text (exclude outer ''): 'Hello123!'
```

---

## 🧑‍💻 Author

[**Muhammad Kamran**](https://github.com/realmkdev)

💡 Simple ideas, secure results.

---

## ⭐ Support

If you like this project, give it a star on GitHub ⭐ to show your support!
