def dec2base(n,base):
    n=int(n)
    res = ""
    while n!=0:
        res = str(n%base) + res
        n=n//base
    return res

def base2dec(n,base):
    res = 0
    j=len(n)-1
    for i in range(len(n)):
        res += int(n[i])*(base**j)
        j-=1
    return str(res)

def get_base(n):
    match n:
        case 0:
            return 10
        case 1:
            return 2
        case _:
            exit("Invalid base")

def convert(n,base1,base2):

    return base2dec(dec2base(n,get_base(base1)),get_base(base2))


if __name__ == "__main__":
    #testing
    #0 is base 10
    #1 is base 2
    print(convert('100',1,0))
    print(convert('100',0,1))