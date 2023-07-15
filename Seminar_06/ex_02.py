import module_ex_02

def main():
    a, b, nr_tries = map(int, input("Insert the limits and the number of tries: ").split())
    if module_ex_02.find_number(a, b, nr_tries):
        print('Your guess')
    else:
        print('You have no more tries')


