# # class Foo:
# #     answer = 42

# # f1 = Foo()
# # f2 = Foo()

# # print(f1.answer)
# # print(f2.answer)
# # # both will print 42

# # f1.answer = 84
# # Foo.answer = 21

# # print(f1.answer)  # 84
# # print(f2.answer) # 21



# class Foo:
#     def __init__(self):
#         self.answer = 42

# f1 = Foo()
# f2 = Foo()
# # f2.answer = 4000
# Foo.answer = 21
# # f1.answer = 2000

# print(f1.answer)
# print(f2.answer)
# # both will print 42 still

cmd = {
        'room1': room1,
        'room2': room2,
        'finished': finish
    }

while True:
    action = input("> ")
    if action in cmd:
    # if thescenes.cmd.get(action):
        print("success")
        # trying to test user input on calling a function from a list or dict.
        # thescenes.map_list[action]()
        thescenes.cmd[action]()
