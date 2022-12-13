file = open('test.txt')

rows = int(file.readline())
for i in range(rows):
    row = file.readline().split(' ')
    if not(len(row) == 1 and row[0] == ''):
        print(row)




