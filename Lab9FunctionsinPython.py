# Program Number 1
def lower_upper(x):
    upper = 0
    lower = 0
    for i in x:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
    return upper, lower

# Program Number 2
def input_1():
    c = input("Enter the string: ")
    g, h = lower_upper(c)
    print({'upper': g, 'lower': h})

input_1()

# Program Number 3
def create_array(x, y, z, v):
    result = []
    for _ in range(z):
        layer = []
        for _ in range(y):
            row = [v for _ in range(x)]
            layer.append(row)
        result.append(layer)
    return result

def input_2():
    x = int(input("x = "))
    y = int(input("y = "))
    z = int(input("z = "))
    v = int(input("value = "))
    a = create_array(x, y, z, v)
    print("Generated 3D array:", a)

input_2()

# Program Number 4
def sum_(a, b, c, d, e):
    return a + b + c + d + e

def avg_(a, b, c, d, e):
    return (a + b + c + d + e) // 5

def input1():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    d = int(input("Enter 4th number: "))
    e = int(input("Enter 5th number: "))
    g = sum_(a, b, c, d, e)
    h = avg_(a, b, c, d, e)
    print("The sum of 5 numbers:", g)
    print("The average of 5 numbers:", h)

input1()

# Program Number 5
def pangram(s):
    a = set('abcdefghijklmnopqrstuvwxyz')
    s = set(s.lower())
    return a <= s

s = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
print("Is pangram?", pangram(s))

# Program Number 6
def tuple_in_list(x):
    l = []
    for i in range(1, x + 1):
        l.append((i, i * i, i * i * i))
    return l

x = int(input("Enter a number: "))
print(tuple_in_list(x))

# Program Number 7
def is_palindrome(x):
    return x == x[::-1]

x = input("Enter the string: ")
print("Is palindrome?", is_palindrome(x))

# Program Number 8
def convert(s1):
    unique_chars = set(s1)
    sorted_chars = "".join(sorted(unique_chars))
    return sorted_chars

s1 = input("Enter a string: ")
print("Converted string:", convert(s1))

# Program Number 9
def count_alpha_digits(s):
    a = 0
    n = 0
    for i in s:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            n += 1
    return a, n

s = input("Enter a string: ")
a, n = count_alpha_digits(s)
print({'alpha': a, 'number': n})

# Program Number 10
def freq(s):
    word_list = s.split()
    freq_dict = {}
    for word in word_list:
        word = word.lower()
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return dict(sorted(freq_dict.items()))

s = input("Enter a string: ")
r = freq(s)
print("Word frequencies:", r)

# Program Number 11
def create_list(l1, l2):
    inter = list(set(l1) & set(l2))
    return inter

l1 = [1, 2, 3, 4, 5]
l2 = [2, 5, 6, 7, 8]
r = create_list(l1, l2)
print("Common elements:", r)
