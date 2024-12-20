from new import Euclid as ek
from new import exchanges as ex
from new import Pascal as ps 


def main():
    user_choes = input("In ")
    if user_choes.lower() == "t" :
        user_temp = input("")
        user_temp  = user_temp.split()
        a,b = int(user_temp[0]),int(user_temp[1])
        print("", e = ek.gcd(a, b))
    elif user_choes.lower() == "k" :
         print("", ex.spis())   
    else:
        p = ps.pascal(int(input()))
        print(p)
        main()
    


if __name__ == "__main__":
    main()