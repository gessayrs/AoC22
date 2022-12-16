with open('input6.txt', 'r') as f:
    string = f.read()

string = string.strip('\n')

for letter in range(len(string)-13):
    letter_list = list(string[letter:letter+14])
    print(letter_list)
    counter = 0
    
    for i in range(len(letter_list)-1):
        if letter_list[i] in letter_list[i+1:]:
            counter = 0
            break
        else:
            counter +=1
            print(counter)
    
    if counter == 13:
        print(letter+14)
        break
        
        