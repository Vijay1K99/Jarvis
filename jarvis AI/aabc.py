import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

# pass_len=random.randint(8,13)  #without User INput
pass_len = int(input("Enter Password Length : "))

# length of password by 50-30-20 formula
alpha_len = pass_len // 2
num_len = math.ceil(pass_len * 30 / 100)
special_len = pass_len - (alpha_len + num_len)

password = []


def generate_pass(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)


# alpha password
generate_pass(alpha_len, alpha, True)
# numeric password
generate_pass(num_len, num)
# special Character password
generate_pass(special_len, special)
# suffle the generated password list
random.shuffle(password)
# convert List To string
gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)


# from tkinter import *
# from tkinter.ttk import *
# from time import strftime
# root = Tk()
# root.title('Clock')
# def time():
#     string = strftime('%H:%M:%S %p')
#     lbl.config(text = string)
#     lbl.after(1000, time)
# lbl = Label(root, font = ('franklin gothic', 40, 'bold'),
#             background = 'black',
#             foreground = 'white')
# lbl.pack(anchor = 'center')
# time()
# mainloop()


# Encoding Data into Quick  Response Code(QR Code)

# import qrcode

# # Data to encode
# data = input('Enter the Data: ')

# version = int(input('Enter the version (complexity): '))  # maxvalue  15
# box_size = int(input('Enter the Box size: '))  # max value 10
#
# # Creating an instance of QRCode class
# qr = qrcode.QRCode(version, box_size, border=5)

# # Adding data to the instance 'qr'
# qr.add_data(data)

# qr.make(fit=True)
# img = qr.make_image(fill_color='black', back_color='white')

# f = input("name it as: ")  # image name
# img.save(f'{f}.png')

# print('qr code generated and saved in the gallery')