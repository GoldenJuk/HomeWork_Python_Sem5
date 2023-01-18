from my_function import coding, decoding

path = r'RLE\text.txt'
with open(path,'r',encoding='utf8') as data:
    my_string = data.read()

if my_string.isalpha():
    result = (coding(my_string))
    print(f'\nРезультат сжатия данных ({my_string}): {result}\n')
else:
    result = (decoding(my_string))
    print(f'\nРезультат восстановления данных ({my_string}): {result}\n')
 
with open(path,'w',encoding='utf8') as data:
    data.write(result)