
# --------------------------------- Q1(A) ---------------------------------

str = str(input('請輸入一個字串：'))
ans = ''.join(reversed(str))
print('Q1(A)-Answer:', ans)

# --------------------------------- Q1(B) ---------------------------------

str1 = input('請輸入字串(可含空格)：')
a = str1.split()

temp = []
for i in a:
    r_s = ''.join(reversed(i))
    temp.append(r_s)

ans_2 = ' '.join(temp)
print('Q1(A)-Answer:', ans_2)




