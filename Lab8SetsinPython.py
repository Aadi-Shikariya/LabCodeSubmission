# Program Number 1
def set1():
    sentence = input("Enter the sentence: ").split()
    print("Original words:", sentence)
    s = {x.upper() for x in sentence}
    print("Set with uppercase words:", s)

set1()

# Program Number 2
import random

def set2():
    s = set()
    while len(s) != 10:
        x = random.randint(15, 45)
        s.add(x)
    print("Initial set:", s)

    d = {x for x in s if x > 35}
    c = sum(1 for x in s if x < 30)
    
    s = s - d

    print("No. of elements < 30:", c)
    print("After deleting all the values > 35:", s)

set2()

# Program Number 3
def set3():
    s = set()
    for i in range(5):
        s.add(input(f"Enter name {i + 1}: "))
    print("Initial set of names:", s)

    nm = input("Enter a name to modify: ")
    if nm in s:
        newnm = input("Replace it with: ")
        s.remove(nm)
        s.add(newnm)
    else:
        print(f"{nm} not found in set.")

    if len(s) >= 2:
        print(s.pop(), "is deleted")
        print(s.pop(), "is deleted")
    elif len(s) == 1:
        print(s.pop(), "is deleted")
    else:
        print("Set is empty. Nothing to delete.")

    print("The final set:", s)

set3()

# Program Number 4
def set4():
    s = {'vidhi', 'naiyya', 'swaroopa', 'vruti', 'krissa'}
    sa = {nm for nm in s if nm.startswith('a')}
    sb = {nm for nm in s if nm.startswith('b')}

    print("Names starting with 'a':", sa)
    print("Names starting with 'b':", sb)

set4()
