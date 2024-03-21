3. #Нарисовать только границу поля и пустую серединку.

field_size = input("Введите размеры поля (ширина * высота): ")
W, H = field_size.split('*')
W = int(W)
H = int(H)
print('o' * (W+2))
field = ('o' + " "* W + 'o'+'\n') * (H-2)
print(field)
print('o' * (W+2))
