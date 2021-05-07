def int_func(word):
    print(word[0:1].upper() + word[1:len(word)])
    return

def int_multi_func(text):
    words= text.split()
    for i in words:
        int_func(i)

int_func(input("Введите слово: "))
int_multi_func(input("Введите текст разделенный пробелами"))
