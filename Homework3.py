# Кожен пише суму списку за допомогою for та while

l = [3, 5, 7, 9]

sum = 0
for i in l:
    sum += i

print("List sum:", sum)



l = [2, 3, 5, 8]

sum = 0
index = 0

while index < len(l):
    sum += l[index]
    index += 1

print("List sum:", sum)




# Написати програму, яка виводить сама себе
with open("text1.txt", "a") as my_file:
    my_file.write("Some text.Hello world")


with open("text1.txt", "r") as my_file:
    for line in my_file:
        print(line, end=" ")

# Написати програму, яка виводить саму себе задом наперед

with open("text1.txt", "r") as my_file:
    for line in my_file:
        print(line[::-1], end=" ")



print("\n")


# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. Читайте із файлу перший рядок з трьома числами, беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.
# Переробити другу задачу так, щоб результат писався в інший файл. Додаємо list comprehension, map та інші свіжеотримані знання до виконання завдання.
def fizzbuzz(fizz, buzz, x):
    fizzbuzz = ""
    for i in range(1, x + 1):
        # if i % fizz and i % buzz:
        #   print (i, end=" ")
        if not i % fizz and not i % buzz:
            fizzbuzz += "FB "
        if not i % fizz:
            fizzbuzz += "F "
        elif not i % buzz:
            fizzbuzz += "B "
        else:
            fizzbuzz += f"{str(i)} "
    return fizzbuzz

with open("fizzbuzz.txt", "r") as file:
    my_file = file.readlines()

clear_list = []

for i in my_file:
    clear_list.append(i.strip())

for i in clear_list:
    fbz = i.split()
    fizz = int(fbz[0])
    buzz = int(fbz[1])
    x = int(fbz[2])


    print(fizzbuzz(fizz, buzz, x))












