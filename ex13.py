from sys import argv
# read the WYSS section for how to run this
script, first, second, third, = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("Fourth input?:", end=' ')
print(f"Your fourth input is {input()}")

# must be run as 'python first 2nd 3rd'