# with open('text3.txt', 'r') as f_obj:
#     data = f_obj.read()
#     print(data)

# with open('text3.txt') as f_obj:
#     data = f_obj.read()
#     print(data)

name = '1Gopi420'
count = 0
for i in name:
    if(ord(i) >= 48 and ord(i)<=57):
       count = count+1
print("total count of number", count)