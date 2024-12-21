#Функция для построения треугольника Паскаля
def pascal(k, tr=None):
    if tr is None:
        tr = [[1]]
    if k == 1:       #Проверка на единичное значение
        return tr
    else:            #Нахождение элементов до i-того значения
        prev_tr = tr[-1]
        new_tr = [1] + [sum(i) for i in zip(prev_tr, prev_tr[1:])] + [1]
        return pascal(k - 1, tr + [new_tr])
    



if __name__=='__main__':
   pascal()
   inp = int(input("Введите значение, до которого должен быть построен треугольник Паскаля "))    
   print("Вот итог: ")    
   print(pascal(inp))
   