# user_find = input("Enter ur username : ")
# user_input = input(": ")
# banned_user = []

prohibited_words = ["shit"]  # add ur prohibited words


def split_words(user):
    return user.split(" ")


def user_ban(username):
    with open("User_banned.txt", "a") as f:
        f.write(f"\n{str(username)} is banned")


def check_word_is_prohibited(word, username):
    ind = -1
    for words in range(1, len(word) + 1):
        ind += 1
        if word[ind] in prohibited_words:
            print("Do not enter prohibited words")
            user_ban(username=username)
