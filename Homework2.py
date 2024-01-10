# Ввести число, вивести усі його дільники.

n = int(input("Enter your number: "))
i = 1
while i <= n:
    if not n % i:
        print(i, end=' ')
    i += 1

print("\n")

# Ввести число, вивести його розряди та їх множники

number = int(input("Enter your number: "))
temp = number
multipliers = []

if not number:
    print("Розряди: 0, Множники: немає")
else:
    position = 1
    while temp > 0:
        digit = temp % 10
        if digit != 0:
            multiplier = digit * position
            multipliers.append((digit, multiplier))
        temp //= 10
        position *= 10

    print(f"Розряди and their Множники {number}:")
    for digit, multiplier in multipliers[::-1]:
        print(f"Розряди: {digit}, Множники: {multiplier}")

print("\n")

# Перший рівень ("if"): Набрати всі приклади посимвольно і змусити їх працювати, розібратися у роботі.


# print("Give it to me!")

number = int(input("Enter your number: "))

if (number >= 100):
    print("Thanks, man!")
elif ((number > 10) and (number < 100)):
    print("OK :(")
else:
    print("WHAAAAT????")

if (number > 1000):
    print("!!!!WOOOOWWWW!!!")


print("\n")


# Другий рівень ("if-elif-else"): Придумати власні приклади на альтернативні варіанти if і активне використання булевої алгебри.


light = "red"
if light == "red":
    print("Stop")
elif light == "Yellow":
    print("Wait")
elif light == "Green":
    print("Go")
else:
    print("Crash")

age = int(input("How old are you: "))
if age >= 18:
    print("Welcome")
else:
    print(f"You age is {age}, miss {18 - age}")

time = 13
if time < 12 or time > 14:
    print("Open")
else:
    print("Close")

time = 13
day = "mo"
if time >= 8 and  day != "mo":
    print("Open")
else:
    print("Close")


print("\n")


# Третій рівень ("Містер Буль. Джордж Буль!"):


fizz = int(input("Enter Fizz number :"))
buzz = int(input("Enter Buzz number :"))
x = int(input("Enter another number :"))

for i in range(1, x+1):
    if i % fizz and i % buzz:
      print (i, end=" ")
    elif not i % fizz and not i %buzz:
      print ("FB", end= " ")
    elif not i % fizz and i % buzz:
      print ("F", end=" ")
    elif i % fizz and not i % buzz:
        print ("B", end=" ")
    else:
      print(i)