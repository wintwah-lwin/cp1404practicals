#1
name = input("Enter your name: ")
out_file = open('name.txt', 'w')
out_file.write(name)
out_file.close()

#2
in_file = open('name.txt', 'r')
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

#3
with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    total = first_number + second_number
    print(f"Total: {total}")

#4
with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(f"Total: {total}")