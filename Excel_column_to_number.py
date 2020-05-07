alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def excelColumnToNumber(n):
    list=[]
    n-=1
    while n>=0:
        if n==0:
            list.append(0)
            break
        a=n%26
        n=round((n-a)/26)
        list.append(a)
        n-=1
    print("".join(map(lambda i:alphabet[i],list)))