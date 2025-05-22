import art as a

while True:
    user_input = input('Please enter a short text to convert to ASCII: ')
    if len(user_input.split()) < 3:
        print(a.text2art(user_input))
        print('Here\'s your art!' + '\n' + '=' * 30 + '\n')
        new_input = input('Just for fun, enter another, go on!: ')
        if len(new_input.split()) <= 3:
            print(a.text2art(new_input,font="rand"))
            print('Thanks for making art with me!' + '\n' + 'See ya!' + '\n' + '=' * 30 + '\n')
            break
        else:
            print("Please enter a shorter text.")
    else:
        print('Please enter a shorter text.')
