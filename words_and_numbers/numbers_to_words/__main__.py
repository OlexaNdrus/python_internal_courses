"""Main body for application. Greets, converts and asks if the user wants to continue."""

from numbers_to_words import ask_number, greet

if __name__ == '__main__':
    user_name = greet.greet_user()

    print('Greetings, {name}!'.format(name=user_name))

    while True:
        converted_number = ask_number.number_to_convert(user=user_name)

        if converted_number is not None:
            print('Your`e converted number is:    {}'.format(converted_number))
        else:
            print(
            'Sorry {}, but your number is impossible to convert.' \
            '\nYour number should be any integer or float value' \
            ' (Use point as delimiter).'.format(user_name)
            )

        go_next = input('Do you want to enter another number: y/n?\n')
        if go_next not in ('yes', 'y'):
            break

    print('Goodbye, {name}!'.format(name=user_name))

