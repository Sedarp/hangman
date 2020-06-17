import random

print('H A N G M A N')

selection = ''
while selection != 'exit':
    selection = input('Type "play" to play the game, "exit" to quit: ')
    if selection == 'play':
        # choose random word from the list
        
        word_list = ['python', 'java', 'kotlin', 'javascript']
        word = random.choice(word_list)
        mask = '-' * len(word)
        l_mask = list(mask)

        dic_letters = set()
        lives = 8
        while lives > 0 and mask != word:  # keep asking for letters untils lifes = 0 or word guessed
            while True:
                print(f'\n{mask}')
                char = input("Input a letter: ")
                if len(char) != 1:
                    print('You should input a single letter')
                elif char.isupper() or not char.isalpha():
                    print('It is not an ASCII lowercase letter')
                elif char in dic_letters:
                    print("You already typed this letter")
                else:
                    dic_letters.add(char)
                    break
            if char in word:  # is the char in the word?
                index = 0
                for letter in word:  # look for input letter in word to refresh mask
                    if letter == char:
                        l_mask[index] = char
                        mask = ''.join(l_mask)
                    index += 1
            else:
                lives -= 1
                print("No such letter in the word")
        if mask == word:
            print('''You guessed the word!
            You survived!''')
        else:
            print("You are hanged!")
