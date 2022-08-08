# number = int(input("How many times do I have to tell you?"))
# for i in range(number):
#     print("Hello!\n")

# for i in range(1,21):
#     if i == 4 or i == 13:
#         print(f"{i} is unlucky")
#     elif i%2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

star = 1

while star < 11:
    output = ""
    for i in range(0, star):
        output += "*"
    print(output)
    star += 1
