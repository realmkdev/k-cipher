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

## ❓ FAQs

### 1. Why are there outer `' '` around the encrypted or decrypted text?

If your encrypted text starts **or ends** with a space (`" "`), it would be almost impossible to notice it in the output.
To avoid confusion, the program wraps results inside **single quotes `' '`** — this helps you clearly see where the text begins and ends.

Example:

```
Decrypted text (exclude outer ''): ' Hello '
```

Without the quotes, you wouldn’t know there are spaces before and after!

---

### 2. Can I use spaces, symbols, and numbers in my text or key?

✅ Yes!
The cipher supports:

```
A–Z, a–z, 0–9, and symbols like ! @ # $ % ^ & * ( ) etc.
```

Anything within the defined `char_list` can be encrypted or decrypted.

---

### 3. Is this encryption secure enough for real-world use?

🔐 **No, it’s meant for educational purposes.**
K-Cipher demonstrates how basic encryption and decryption logic works — it’s not intended for serious cryptographic use.

---

### 4. What happens if I use the wrong password for decryption?

You’ll get meaningless output.
Only the exact same key that was used for encryption can correctly decrypt the text.

---

## 🧑‍💻 Author

[**Muhammad Kamran**](https://github.com/realmkdev)

💡 Simple ideas, secure results.

---

## ⭐ Support

If you like this project, give it a star on GitHub ⭐ to show your support!
