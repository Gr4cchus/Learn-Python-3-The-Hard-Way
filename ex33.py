# i = 0 # not sure why this cannot be accesses in a function
numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)

# def while_loop(input_range_number, input_increment_number):
#     i = 0
    
#     while i < input_range_number:
#         print(f"At the top i is {i}")
#         numbers.append(i)

#         i = i + input_increment_number
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")
#     for num in numbers:
#         print(num)

user_number_range = input("Choose your number range\n> ")
user_number_increment = input("Choose your number increment\n> ")

# while_loop(int(user_number_range), int(user_number_increment))

def for_loop(input_range_number, input_increment_number):
    for i in range(0, input_range_number, input_increment_number):
        print(f"Adding {i} to the list.")
        # append is a function that lists understand
        for_loop_numbers.append(i)
        print(for_loop_numbers)

for_loop_numbers = []

for_loop(int(user_number_range), int(user_number_increment))