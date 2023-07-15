from module_ex_04_05_06 import my_secret

secret = input('Insert the secret: ')
variants = input('Insert 3 answers using comma: ').split(',')
attempts = int(input('Insert the number of attempts: '))


result = my_secret(secret, variants, attempts)
print(f'The result is: {result}')