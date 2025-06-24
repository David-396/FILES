from pycparser.c_ast import Return

# 2
print("question 2: ")
with open(r"C:\Users\User\OneDrive\Desktop\my_text.txt", 'w') as f:
    f.write('''Hello world
It’s the first exercise in I/O
That mean it is number 1
Not 2
Not three
It is exciting
And i am all 4 it''')


# 3

def if_has_digit(text):
    for letter in text:
        if letter.isdigit():
            return True
    return False
print("question 3: ")
with open(r"C:\Users\User\OneDrive\Desktop\my_text.txt", 'r') as f:
    txt = f.readline()
    while txt:
        if if_has_digit(txt):
            print(txt)
        txt = f.readline()


# 4
print("question 4: ")
with open(r"C:\Users\User\OneDrive\Desktop\my_text.txt", 'r') as f:
    txt = f.readline()
    even_words_rows = []
    sum_words = 0
    sum_letters = 0
    most_common_word = {}
    i=0
    while txt:
        words_lst = txt.lower().strip().split(' ')
        sum_words += len(list(map(lambda word: not word.isdigit(), words_lst)))
        sum_letters += len([letter for letter in txt if letter not in ['\n']])

        words_dict = dict((word,words_lst.count(word)) for word in words_lst)
        most_common_word.update(words_dict)


        if len(words_lst) % 2 == 0:
            even_words_rows.append(i)

        txt = f.readline()
        i+=1

    most_word = ""
    max_number = 0
    for k,v in most_common_word.items():
        if max_number<v:
            most_word = k

    print("the indexes of rows that has the even words : ", even_words_rows)
    print("summary number of all words in the file : " ,sum_words)
    print("summary number of all letters in the file : "  , sum_letters)
    print("the most common word : ", most_word)


# 5
print("question 5: ")
with open(r"C:\Users\User\OneDrive\Desktop\my_text.txt", 'r') as rfile, open(r"C:\Users\User\OneDrive\Desktop\summary.txt", 'w') as wfile:
    txt = rfile.readline()
    while txt:
        wfile.write(f"{txt[:-1]} ({len(txt.split(' '))} words)\n")
        txt = rfile.readline()
