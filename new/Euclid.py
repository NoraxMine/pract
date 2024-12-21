#Функция для вычисления НОД
def gcd(x, y):
    if x == 0 or y == 0:  #Проверка на ненулевое значение
         return max(x, y)
    else:
     if x > y:                 #Проверка на наибольшее из заданных значений и вычисление НОД
        return gcd(x - y, y)
     else:
        return gcd(x, y - x)




if __name__=='__main__':
   gcd(56, 98)
   print("НОД чисел 56 и 98 = " + str(gcd(56, 98))) #Выводим значение