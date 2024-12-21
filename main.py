from new import Euclid as ek
from new import exchanges as ex
from new import Pascal as ps 


def main():
    user_choes = input("Для вызова функции по нахождению НОК введите 1 \nЕсли вам нужно посмотреть перестановки в определённом списке введите 2 \nЕсли хотите помтроить треугольник паскаля введите любую другую клавишу ")
    if user_choes.lower() == "1" :
        user_temp = input("")
        user_temp  = user_temp.split()
        a,b = int(user_temp[0]),int(user_temp[1])
        print("", ek.gcd(a, b))
    elif user_choes.lower() == "2" :
         print("", ex.spis())   
    else:
        print(ps.pascal(int(input())))
        main()
    


if __name__ == "__main__":
    main()