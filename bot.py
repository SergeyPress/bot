def correct_answer(correct_answer_number):
    if int(correct_answer_number) == int(input()):
        pass
    else:
        print('Please, try again.')
        correct_answer(correct_answer_number)


number_counter = 0
print('Hello! My name is Botty.')
print('I was created in 2023.')
print('Please, remind me your name.')

name = input()

print('What a grate name, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

final_number = int(input())

while number_counter <= final_number:
    print(f'{number_counter} !')
    number_counter += 1

print("Let's test your programming knowledge.")
print('Why do we use methods?')
print('1. To repeat a statement multiple times.')
print('2. To decompose a program into several small subroutines.')
print('3. To determine the execution time of a program.')
print('4. To interrupt the execution of a program.')

correct_answer(2)

print('Congratulations, have a nice day!')
