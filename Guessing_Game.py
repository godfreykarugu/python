'''
secret = 'passion'
guess = ''

while guess != secret:
    guess = input('Enter a Guess: ')
print('You Won!')
'''

secret = 'passion'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter a Guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print('You are out of guesses')
else:
    print('Congratulations, You Won!')