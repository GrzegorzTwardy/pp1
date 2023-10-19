# # 8
# speed_limit = 140
# car_speed = int( input('Enter car speed km/h: ') )

# if car_speed > speed_limit:
#     print('Warning: speed limit exceeded!!\n')


# # 9
# result = int(input('Enter test result: (%)') )
# condition = 50

# if result >= condition:
#     print('You passed\n')
# else:
#     print('You failed\n')

# 10
# n = int(input('Enter number: '))

# if n > 0:
#     print(n)
# else:
#     print(n * -1)

# # 11
# n = int(input('Enter number: '))

# if n % 2 == 1:
#     print('Number is odd')
# else:
#     print('Number is even')

# # 12
# first_name = input('Enter the name of the first person: ')
# first_age = int(input('Enter the age of the first person: '))
# second_name = input('Enter the name of the second person: ')
# second_age = int(input('Enter the age of the second person: '))

# if first_age >= 18 and second_age >= 18:
#     print(f'Both {first_name} and {second_name} are adults')

# # 13
# n1 = int(input('First number: '))
# n2 = int(input('Second number: '))

# if n1 < 0 or n2 < 0:
#     print(f'At least one of entered numbers {n1} and {n2} is negative')
# else:
#     print('Both numbers are >= 0')

# # 14
# i = 0
# while i <= 4:
#     print('Practice makes perfect!!')
#     i = i + 1

# # 15
# for i in range(5):
#     print('Practice makes perfect!')

# # 16
# sum = 0
# for i in range(1,6):
#     sum = sum + i
# print(f'Sum is {sum}')

# # 17
# i = 1
# result = 0

# while i < 6:
#     result += i

# print(result)

# # 18
# i = 2
# print('while:')
# while i < 11:
#     print(f'1/{i} = {1/i}')
#     i += 1


# print('\nfor:')
# for i in range(1, 11):
#     print(f'1/{i} = {1/i}')

# 19
# result = 0

# # for i in range(2, 11, 2):
# #     result += i

# for i in range(1, 11):
#     if i % 2 == 0:
#         result += i

# print(result)

# # 20
# sum = 0
# for i in range(1,6):
#     print(i)
#     sum = sum + i
# print(f'Sum is {sum}')

# # 21
# n1 = int(input('First number: '))
# n2 = int(input('Second number: '))

# if n1 > n2:
#     print(f'Numbers in ascending order: {n2}, {n1}\n')
# else:
#     print(f'Numbers in ascending order: {n1}, {n2}\n')


# #22
# name = input('Name: ')

# if name[-1] == 'a':
#     print(f'{name} - Polish female name')

# # 23
# age_h = int(input('Enter dog\'s age in human years: '))
# age_d  = 0

# for i in range(1, age_h + 1):
#     if i <= 2:
#         age_d += 10.5
#     else:
#         age_d += 4

# print(age_d)

# #  24
# previous_price = 200
# current_price = 140

# discount = 140/200 * 100

# print(f'Buy the product!!\nProduct price reduced by {100 - discount}%')

# # 25
# p_amount = int(input('Number of products: '))
# price = int(input('Price: '))
# total = 0

# for i in range(1, p_amount + 1):
#     if i <= 2:
#         total += price
#     else:
#         total += price * 0.75

# print(total) 

# # 26
# speed = int(input('Enter speed: '))
# max_s = 140
# min_s = 40
# if speed < min_s or speed > max_s:
#     print('Invalid speed')

# 27
facebook = True
twitter = False
instagram = True

