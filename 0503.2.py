2. #Спросить человека размеры поля (х * у), 
#получить их ОДНИМ вводом '7x8', "нарисовать" поле буковками о без использования цикла.
field_size = input("Введите размеры поля (W * H): ")
W, H = field_size.split('*')
W = int(W)
H = int(H)
field = ('o' * W + '\n') * H
print(field)
