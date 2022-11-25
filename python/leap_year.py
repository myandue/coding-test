import string


year=int(input())
x=False

if year%4==0:
    if year%100==0:
        if year%400==0:
            x=True
        else:
            pass
    else:
        x=True

year=str(year)

if x:
    print(year+"년은 윤년입니다.")
else:
    print(year+"년은 평년입니다.")