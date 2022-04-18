
#Задание 1


with open('nginx_logs.txt') as f:
    data = []
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(data)

#Задание 2
with open('nginx_logs.txt') as f:
    data = []
    spam_dict = {}
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam_dict.setdefault(splitted[0], 0)
        spam_dict[splitted[0]] += 1

spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
print(spam_dict[:5])  # Not only one spamer

#Задание 3
from itertools import zip_longest
import json
out_dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        num_lines_users = sum(1 for line in users)
        num_lines_hobby = sum(1 for line in hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(users, hobby):
            out_dict[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f, ensure_ascii=False)
print(out_dict)

#Задание 4
from itertools import zip_longest
with open('task4.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', encoding='utf-8') as users:
        with open('hobby.csv', encoding='utf-8') as hobby:
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for line in hobby)

            if num_lines_users < num_lines_hobby:
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobby):
                f.write(f'{line_user.strip()}: '
                        f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')
# Задание 6
import sys

price = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')

# python add_sale.py 100


# show_sales.py
import sys

nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    elif len(nums) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(nums[0])
        end_idx = sum(1 for line in f)
        f.seek(0)

    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())