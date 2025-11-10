char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']

def change_length(string, length):
  output = []
  char_index = 0
  for _ in range(length):
    if char_index >= len(string):
      char_index = 0
    output.append(string[char_index])
    char_index += 1
  return "".join(output)

def get_indexes(text):
  output = []
  for char in range(len(text)):
    output.append(char_list.index(text[char]))
  return output


def encrypt(text, key):
  output = []
  char_list_len = len(char_list)
  text_len = len(text)
  key_len = len(key)
  text_indexes = get_indexes(text)
  key_indexes = get_indexes(change_length(key, text_len))
  for x in range(text_len):
    char_index = text_indexes[x] + key_indexes[x] + key_len + 1
    if char_index >= char_list_len:
      char_index -= char_list_len
    output.append(char_list[char_index])
  return "".join(output)

def decrypt(text, key):
  output = []
  char_list_len = len(char_list)
  text_len = len(text)
  key_len = len(key)
  text_indexes = get_indexes(text)
  key_indexes = get_indexes(change_length(key, text_len))
  for x in range(text_len):
    char_index = text_indexes[x] - key_indexes[x] - key_len - 1
    if char_index < 0:
      char_index += char_list_len
    output.append(char_list[char_index])
  return "".join(output)

def main():
  is_running = True

  print("-----------------")
  print("Author: M.Kamran ")
  
  while is_running:
    
    print("-----------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("-----------------")
    option = input("Enter your option (1-3): ")
    if option == "1":
      text = input("Enter text for encryption: ")
      key = input("Enter the password: ")
      encrypted_text = encrypt(text, key)
      print("-----------------")
      print(f"Encrypted text (exclude outer ''): '{encrypted_text}'")
    elif option == "2":
      text = input("Enter encrypted text: ")
      key = input("Enter the password: ")
      decrypted_text = decrypt(text, key)
      print("-----------------")
      print(f"Decrypted text (exclude outer ''): '{decrypted_text}'")
    elif option == "3":
      is_running = False
    else:
      print("-----------------")
      print("Invalid choice")
  
  print("-----------------")
  print("Thanks for using!")
  print("-----------------")

if __name__ == "__main__":
  main()
