import random, string
x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
print(x)
file_name = r'C:\Users\anura\Desktop\Test.txt'
with open(file_name, 'w') as file_object:
    file_object.write(x)