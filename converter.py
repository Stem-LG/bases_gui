def convert(n,base1,base2) -> str:
    n = int(n,get_base(base1))
    n = dec2base(n,get_base(base2))
    return n

def dec2base(n,base) -> str:
    res = ""
    while n!=0:
        res = "0123456789ABCDEF"[n%base] + res
        n=n//base
    return res

def get_base(n) -> int:
    match n:
        case 0:
            return 10
        case 1:
            return 2
        case 2:
            return 8
        case 3:
            return 16
        case _:
            exit("Invalid base")    

if __name__ == "__main__":
    print(convert("13",0,3))