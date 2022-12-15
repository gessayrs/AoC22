with open('input6.txt', 'r') as f:
    string = f.read()

#print(string)
counter = 0
previous_counter = 0

#example = "bvwbjplbgvbhsrlpgdmjqwftvncz"
#example = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
example = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
letters = [ i for i in example ]
#print(len(example))

for letter in range(len(letters)-3):
    #letter_check = list(letters[letter:letter+7])
    #print(letter)
    #print(letter_check)
    #if (letter_check[0] == letter_check[1]) or (letter_check[0] == letter_check[2]) or (letter_check[0] == letter_check[3]):

    if letter < 4:
        letter_check = letters[0:letter+4]
        print(letter_check)
    else:
        letter_check = letters[letter-3:letter+4]
        #print(letters[letter])
        print(letter_check)

    if len(letter_check) < 7:
        if letter == 0:
            if (letter_check[letter] in letter_check[letter+1:]):
                counter +=1
                print("Count from 0")
        elif letter == 1:
            if (letter_check[letter] in letter_check[:letter]) or (letter_check[letter] in letter_check[letter+1:]):
                counter +=1
                print("Count from 1")
        elif letter == 2:
            if (letter_check[letter] in letter_check[:letter]) or (letter_check[letter] in letter_check[letter+1:]):
                counter +=1
                print("Count from 2")
    else:
        if (letter_check[3] in letter_check[:3]) or (letter_check[3] in letter_check[4:]):
            counter += 1
            print("Count from else")
    '''
    if letter <4 and ((letters[letter] == letters[letter+1]) or (letters[letter] == letters[letter+2]) or (letters[letter] == letters[letter+3])):
        counter +=1
    elif (letters[letter] == letters[letter-3]) or (letters[letter] == letters[letter-2]) or (letters[letter] == letters[letter-1]):
        counter +=1
    elif (letters[letter] == letters[letter+1]) or (letters[letter] == letters[letter+2]) or (letters[letter] == letters[letter+3]):
        counter +=1
    '''
    #print(counter)
    #else:
        #counter +=1
    
    #print(letter)
    #letter_check = [ i for i in example[letter:letter+4] ]
    #counter +=1
    #print(letter_check)

    #if len(letter_check) < 4:
    #for i in range(len(letter_check)-3):
        #print(letter_check[i])
        #if (letter_check[i] == letter_check[i+1]) or (letter_check[i] == letter_check[i+2]) or (letter_check[i] == letter_check[i+3]):
            #letter_check = []
            #counter += 4
            #previous_counter = counter - 4
    
    #if counter
    
    #else:
        #letter_check.append(letter)
    #counter +=1
    #break
    
    #print(counter)
    #letter_check = example[letter:letter+4]

    #print(letter_check)
    
    '''
    if len(letter_check) == 4:
        print("Marker Found!")
        break
    '''
    #for i in range(len(letter_check)-1):
        #if (letter_check[i] == letter_check[i+1]) or 

print(counter)



