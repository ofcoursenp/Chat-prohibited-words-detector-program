import Utilities
user_find = input("Enter ur username : ")

# check if user is banned
fh = open("User_banned.txt", "r")
word = user_find
s = " "
count = 1
while s:
    s = fh.readline()
    L = s.split()
    if word in L:
        print(f"{word} is banned from the chat As from line {count} of User_banned.txt")
        exit()
    count += 1

# check if word is prohibited,Library file used Utilities.py
user_msg = input("> ")
while user_find != "Quit_program":
    Utilities.send_log(text=user_msg, username=user_find)
    user_msg = input("> ").lower()
    user_msg_split = user_msg.split()
    print(Utilities.check_word_is_prohibited(user_msg_split, user_find))


# end

