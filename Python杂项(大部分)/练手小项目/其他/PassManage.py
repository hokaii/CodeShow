import random
import pyperclip
import csv


def get_password(password='', num=16):
    count = input("please enter the account: ")
    password_list = ['a']
    for i in range(int(num/2)):
        password_list.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"))
    for i in range(num-int(num/2)):
        password_list.append(random.choice("1234567890#$%^&*,.!@"))
    random.shuffle(password_list)
    password_list[0] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    password = ''.join(password_list)
    pyperclip.copy(password)
    try:
        input_file = open('password.csv')
        file_reader = csv.reader(input_file)
        csv_list = list(file_reader)
        if count in str(csv_list):
            print("The account already exists!")
            for i in range(len(csv_list)):
                if csv_list[i][0] == count:
                    pyperclip.copy(csv_list[i][1])
                    break
            quit()
        else:
            pass
    except FileNotFoundError:
        pass
    password_list_a = [count, password]
    with open('password.csv', 'a', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(password_list_a)
        output_file.write('\r')
        output_file.close()
