# write your code here
import random


def check(result):
    try:
        user_input = int(input())
        if result == user_input:
            print('Right!')
            return 1
        else:
            print('Wrong!')
            return 0

    except ValueError:
        print('Incorrect format.')
        return check(result)


def level_check():
    try:
        print('Which level do you want? Enter a number:')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares of 11-29')
        user_input = int(input())
        if user_input == 1:
            return 1
        elif user_input == 2:
            return 2
        else:
            print("Incorrect format.")
            return level_check()
    except ValueError:
        print("Incorrect format.")
        return level_check()


def creation():
    first_number = random.randint(2, 9)
    second_number = random.randint(2, 9)
    operations = ['+', '-', '*']
    operant = random.choice(operations)
    if operant == '+':
        result = first_number + second_number
    elif operant == '-':
        result = first_number - second_number
    elif operant == '*':
        result = first_number * second_number
    print(first_number, operant, second_number)
    return result


def root_creation():
    number = random.randint(11,29)
    print(number)
    return number ** 2

# Program Starts Here
n = 0
check_first_answer = level_check()
for i in range(5):
    if check_first_answer == 1:
        f_o = 'level 1 (simple operations with numbers 2-9).'
        answer = creation()
        n += check(answer)
    elif check_first_answer == 2:
        f_o = 'level 2 (integral squares of 11-29).'
        answer = root_creation()
        n += check(answer)
print(f"Your mark is {n}/5. Would you like to save the result? Enter yes or no.")

save_results = input()
accepted = ['yes', 'y']
if save_results.lower() in accepted:
    name = input('What is your name? \n')
    with open('results.txt', 'a') as f:
        f.write(f"{name}: {n}/5 in {f_o}")
    print('The results are saved in "results.txt".')
# > yes
# What is your name?
# > Kate
# The results are saved in "results.txt".