tu = input('Nhập dữ liệu: ')

n = len(tu)
m = n//2
print('Từ "', tu, '" là ', sep='', end='')
for i in range(m):
    if tu[i] != tu[-1-i]:
        print('không phải ', end='')
        break
print('a palindrome')




