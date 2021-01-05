
number_input = int(input('請輸入一個數字：'))

output = []
for i in range(1, number_input+1):

    if i % 3 != 0 and i % 5 != 0:
        output.append(i)
    if i % 15 == 0:
        output.append(i)

print('Q2-Answer:', len(output))
