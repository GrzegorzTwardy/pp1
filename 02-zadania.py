from math import pi

# 1

# type(50)
# type(12.4)
# type(4 * 7)
# type(4.0 * 6)
# type("test")
# type(True)
# type(2 > 5)

# 1 + 2 % 3 ** 4 * 5

# 65
#   1 + 2**3 * 5 = 11
#   

# 8
print(8)

#n1 = int(input('Number 1: '))
n1 = 2
#n2 = int(input('Number 2: '))
n2 = 8
result = n1 + n2

print('The result of summation: ', result)

# 9
print(9)
n1 = 5
n2 = 1
n3 = 8
n4 = 6
n5 = 3

print(n1 + n2 + n3 + n4 + n5)
print(n1**2 + n2**2 + n3**2 + n4**2 + n5**2)
print(n3 / n5)
print(n3 == n4, '\n')


# 10
print(10)
name = 'Grzegorz'
age = 13
height = 183.5

print(f'My name is {name} I am {age} years old, and my height is {height} cm. In 6 years I will be {age + 6} years old. \n')


# 11
print(11)
f_income = 6000
m_income = 9000
total = f_income + m_income
members = 4
per_person = round(total / members, 2)

print(f'Income per person: {per_person} zl.\n')


# 12
print(12)
#first = input('First name: ')
first = 'Grzegorz'
#surname = input('Surname: ')
surname = 'Twardy'
full_name = first + ' ' + surname
print(f'Your fullname is {full_name}\n')


#13
print(13)
#side = int(input('Enter cube side: '))
side = 6
print(f'The surface area of a cube with side {side} is {6 * side ** 2}\n')


# 14
print(14)
radius = 5
area = pi * radius ** 2
circum = 2 * pi * radius

print(f'Area of a circle: {area}\nCircumference of a circle: {circum}\n')


# 15
print(15)
#celsius = int(input('Temperature in celsius: '))
celsius = 24
kelvin = 273.15 + celsius
fahren = 2 * celsius + 32

print(f'Celsius: {celsius}')
print(f'Kelvin: {kelvin}')
print(f'Fahrenheit: {fahren}')


# 18
print(18)

x = 7
y = 8

x, y = y, x

print(x, y, '\n')


# 19
print(19)
a = 4
print(f'Cube volume: {a ** 3}, Cube area: {6 * a ** 2}\n')


# 20
