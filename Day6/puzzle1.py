with open('input6.txt', 'r') as f:
    string = f.read()

for letter in range(len(string)-3):
    letter_list = list(string[letter:letter+4])
    counter = 0

    for i in range(len(letter_list)-1):
        if letter_list[i] in letter_list[i+1:]:
            counter = 0
            break
        else:
            counter +=1
    
    if counter == 3:
        print(letter+4)
        break
    