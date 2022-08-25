# user_find = input("Enter ur username : ")
# user_input = input(": ")
# banned_user = []

prohibited_words = ["shit"]  # add ur prohibited words


def split_words(user):
    return user.split(" ")


def user_ban(username):
    with open("User_banned.txt", "a") as f:
        f.write(f"\n{str(username)} is banned")


words_count = 0


def check_word_is_prohibited(word, username):
    global words_count
    ind = -1
    for words in range(1, len(word) + 1):
        ind += 1
        if word[ind] in prohibited_words:
            print("Do not enter prohibited words")
            words_count = words_count + 1
            if words_count == 3:
                user_ban(username)
                print("User is banned")
                words_count = 0
                exit()
    return "-Logged in Message_text.txt"


def send_log(text, username):
    with open("Message_text", "a") as f:
        f.write(f"\n{username}: {text}")



