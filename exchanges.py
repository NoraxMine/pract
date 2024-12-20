#Функция для вычисления списка
def permutation(p): 
    if len(p) == 1:  #Проверка на единичное значение
        return [p]

    free_list = []  #Создание самого списка 
    for t in p:
        elements = [m for m in p if m != t]
        z = permutation(elements) 

        for t in z:                    #Изменение списка
            free_list.append([t] + t)

    return free_list


#Функция для создания перестановок в списке
def spis():
    n = int(input('Введите желаемый размер списка:'))
    array = [i+1 for i in range(n)]
    print('Возможные перестановки элементов списка: ')
    for line in permutation(array):
        print(line)



if __name__=='__main__':
   spis()
   spis() 