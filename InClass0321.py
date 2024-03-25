'''def plus(a,b):
    c=a+b
    return print(c)

d= plus(3,4) #이부분이 7이 되어서 d가 7이 됨.


a=3  # d=pius(4,7)로 대체가 가능함.
b=4
c=a+b
d=c

#진약수의 합을 계산하는 식

def hyacsu(a):#a라는 숫자를 받아 약수를 더하는 함수
    hap=0
    for m in range(1,a):
        if a%m==0:
            hap+=m
    return hap #반드시 해야 값이 나옴.

d= hyacsu(18) #print(hyacsu(18))로 바꿀 수 있다.
print(d)'''

# 두개의 값 return 다시해~~~~~~~~~~~~~
import numpy as np
np.pi #원주율

def circle_area_circum(radius):
    a=radius*radius*np.pi
    b=2*np.pi*radius
    return a,b

a,b= circle_area_circum(10)
print(a,b)

#아니면
def circle_area_circum(radius):
    return np.pi*radius**2, 2*np.pi*radius

'''#여러개의 인풋 코드
def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result
print(sum_nums(10, 20, 30)) # 10, 20, 30 인자들의 합을 출력
print(sum_nums(10, 20, 30, 40, 50))

def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result += n
        mean=result/len(numbers)
    return result,mean
a,b=sum_nums(10,20,30)
print('3 개의 인자 ', [10,20,30]) #,뒤에 numbers써도 오류뜨는 이유는 밖에 있어서!
print("합계 :",a,"평균 :",b)

c,d=sum_nums(10,20,30,40,50,)
print('3 개의 인자 ', [10,20,30,40,50])
print("합계 :",c,"평균 :",d)'''

