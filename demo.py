#  调用random、string模块
import random, string

src_digits = string.digits  # string_数字
src_uppercase = string.ascii_uppercase  # string_大写字母
src_lowercase = string.ascii_lowercase  # string_小写字母
count = int(input("请输入密码生成个数"))
for i in range(count):
    #  随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）
    digits_num = random.randint(1, 6)
    uppercase_num = random.randint(1, 8 - digits_num - 1)
    lowercase_num = 8 - (digits_num + uppercase_num)

    #  生成字符串
    password = random.sample(src_digits, digits_num) + random.sample(src_uppercase, uppercase_num) + random.sample(
        src_lowercase, lowercase_num)

    #  打乱字符串
    random.shuffle(password)

    #  列表转字符串
    new_password = ''.join(password)

    print(new_password)
