# 3.1
'''a=100>200
print(a)

b=100>=200
print(b)

c=100<200
print(c)

d=100<=200
print(d)

e=100==200
print(e)

f=100!=200
print(f)

g=200==200
print(g)

h=200!=200
print(h)

i=True or True
print(i)

j=True or False
print(j)

k=True and False
print(k)

l=True and True
print(l)

m=True or True and False
print(m)

n=True and True or False
print(n)

o='Morning'<'morning'
print(o)

p='A'>'B'
print(p)

# 3.3
a=int(input("나이를 입력하시오 :"))
b=int(input("키를 입력하시오(단위 cm) :"))
if a>=19 and b>=150:
    print("입장할 수 있습니다.")
else:
    print("입장할 수 없습니다.")

# 3.5
a,b=map(int,input("두 개의 정수를 입력하세요 :").split())
if a>b:
    print(b,a)
else:
    print(a,b)

# 3.7
game_score=int(input("게임점수를 입력하시오 :"))
if game_score>=1000:
    print("고수입니다.")
else:
    print("입문자입니다.")

# 3.9
a=int(input("정수를 입력하시오 :"))
if a%2==0:
    print(a,"는(은) 2(으)로 나누어집니다.")
else:
    print(a,"는(은) 2(으)로 나누어지지 않습니다.")
if a%3==0:
    print(a,"는(은) 3(으)로 나누어집니다.")
else:
    print(a,"는(은) 3(으)로 나누어지지 않습니다.")
if a%2==0 and a%3==0:
    print(a,"는(은) 2와(과) 3 모두로 나누어집니다.")
else:
    print(a,"는(은) 2와(과) 3 모두로 나누어지지 않습니다.")

# 3.11
b,o,k=map(int,input("세 복권번호를 입력하시오 :").split())
numbers=[2,3,9]
total=0
for m in [b,o,k]:
    if m in numbers:
        total=total+1
if total==3:
    print("상금 1억 원")
if total==2:
    print("상금 1천만 원")
if total==1:
    print("상금 1만 원")
if total==0:
    print("다음 기회에...")


# 3.13
num1,num2=map(int,input("점의 좌표 x, y를 입력하시오 :").split())
if num1==13 or num1==-7 and num2==4:
    print("원의 내부에 있음")
elif num1==3 and num2==14 or num2== -6:
    print("원의 내부에 있음")
elif -7<=num1<=13 and -6<=num2<=14:
    print("원의 내부에 있음")
else:
    print("원의 외부에 있음")

# 3.15
# 1) for 문 사용
for i in range(1,10):
    print("2*",i,"=",2*i)

# 2) while문 사용
i=0
while i<10:
    print("2*",i,"=",2*i)
    i+=1

# 3.17
#1) 아마 셋 다 세번
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')
#2) 위에 두개만 세번 나오고 마지막은 한 번 
for i in range(3):
    print('Python ')
    print('is ')
print('FUN! ')
#3) 첫 번째만 세번 나머지는 마지막에 한번씩.
for i in range(3):
    print('Python ')
print('is ')
print('FUN! ')

# 3.19
b='햄버거'
c='치킨'
p='피자'
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("-햄버거(입력 b)\n-치킨(입력 c)\n-피자(입력 p)")
i=input("메뉴를 선택하세요(알파벳 b, c, p 입력) :")
while i not in ['b', 'c', 'p']:
    i=input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) :")
if i=='b':
    print("햄버거를 선택하였습니다.")
elif i=='c':
    print("치킨을 선택하였습니다.")
elif i=='p':
    print("피자를 선택하였습니다.")

# 3.21
num=int(input("숫자를 입력하세요 :"))
if num % 2!=0 and num % num-1!=0:
      print(num,"는 소수입니다.")
else:
      print(num,"는 소수가 아닙니다.")

# 3.23
num=-1
while num<=0:
      num=int(input("숫자를 입력하세요 :"))
total=0
for i in range(1,num+1):
      total=total+i**2
print('결과는 {0:d}입니다'.format(total))

# 3.25
day = 0
height = 0
while True:
    day += 1
    height += 7
    print('day : {}  달팽이의 위치 : {} 미터'.format(day, height))
    if height >= 30:
        print('우물을 달출하는 데 걸린 날은 {}일 입니다.'.format(day))
        break
    height -= 5

# 3.27
print('세 자리의 암스트롱 수 :', end = ' ')
for i in range(100, 1000):
    f = i // 100
    s = (i - f * 100) // 10
    t = (i - f * 100 - s * 10) // 1
    if i == (f**3 + s ** 3 + t ** 3):
        print(i, end =' ')

# 3.29
oil=500
while oil >=500:
    add_oil=int(input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오:'))
    oil+=add_oil
    print('현재 탱크양은 {0:d} 입니다.'.format(oil))
if oil <= 500*0.1:
    print('경고 : 연료가 10% 미만이니 충전하세요!')

# 3.31
for n in range(1, 20001):
    divisors_n = []
    for i in range(1,n):
        if n % i == 0:
            divisors_n.append(i)
    sum_divisors_n=sum(divisors_n)

    divisors_sum =[]
    for i in range(1, sum_divisors_n):
        if sum_divisors_n % i == 0:
            divisors_sum.append(i)
        
    if sum(divisors_sum) == n:
        print(n, "의 친화수", sum_divisors_n)
    if sum_divisors_n == n:
            print(n,"은 완전수 입니다.")'''
