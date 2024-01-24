#def count_letters(word):                               # Без множенств, буквы повторяются 
    #for letter in word:
       # counter = 0
        #for let in word:
            #if letter == let:
                #counter += 1
        #print(letter,counter)
#word = 'мама'
#count_letters(word)   

#def count_letters(word):                                # Со множествами, буквы не повторяются 
    #for letter in set(word):
        #counter = 0
        #for let in word:
            #if letter == let:
                #counter += 1
        #print(letter,counter)
#word = 'мама'
#count_letters(word)   

# Классическая схема подчета чего-то через словарь
def count_letters(word): # линейная сложность
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1       #Если буквы(ключа) еще нет в словаре, ей присваивается дефолтное значение "0" +1, если же
    for key, value in count.items():                   # буква есть в словаре то ей присваивается новое значение "значение" +1 
        print(key, value)                                               
word = input()
count_letters(word)