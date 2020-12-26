# Way 1
# f_obj = open('text1.txt', mode='w')
# f_obj.write("hello everyone, Marry Christmas")
# f_obj.close()

# f_obj = open('text2.txt', mode='w')
# for i in range(1, 11):
#     f_obj.write(f"hello everyone, Marry Christmas {i} \n")
# print(f_obj.closed)
# f_obj.close()
# print(f_obj.closed)

# Way 2
with open('text3.txt', mode='w') as f_obj:
    for i in range(1, 11):
        f_obj.write(f"5 * {i} = {5 * i}\n")