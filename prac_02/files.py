#1.
# out_file = open('name.txt', 'w')
# name = input('Name: ')
# print(name, file=out_file)
# out_file.close()

#2.
# out_file = open('name.txt', 'r')
# print('Your name is', out_file.read())
# out_file.close()

#3.

# out_file = open('numbers.txt', 'r')
# for lines in range(1):
#     line = float(out_file.readline())
#     line2 = float(out_file.readline())
#     calulate = line + line2
#     print(calulate)
# out_file.close()

#4.

file_name = input('File Name: ')
out_file = open(file_name, 'r')
out_file.close()