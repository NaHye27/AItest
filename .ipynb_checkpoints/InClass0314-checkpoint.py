#3/14 수업 내용.

a=100
print(type(a))

print(input("Insert"))

print(input("Insert").split())

print("11 22 33".split())

func1().behavier1().behavier2().behavier3()

#map 사용 
a,b=map(int,input("두 개의 정수를 입력하세요 :").split())
if a%b == 0:
    print("{0:d}은(는) {1:d}의 배수입니다.".format(a,b))
    
else:
    print("{0:d}은(는) {1:d}의 배수가 아닙니다.".format(a,b))

#윤년 계산
a=int(input("연도를 입력하세요 :"))
if a%4 == 0 and a%100!=0 or a%400==0:
    print(a,"년은 윤년입니다.")
else:
    print(a,"년은 윤년이 아닙니다.")

a=int(input("연도를 입력하세요 :"))
b= ((a%400==0) or (a%4==0 and a%100!=0))
print(a,"년은 윤년이",b)

#반복문
numbers=[10,20,30,40,50]
total=0
for m in numbers:
    total=total+m
    print(total)

#1번 식
total=0
for i in range(10):
    total+=i
print(total)

#2번 식
total=0
i=0
while i<10:
    total+=i
    i+=1
print(total)

# 여기에 조건을 더 추가하는 법
total=0
i=0
while True:
    total+=i
    i+=1
    if (i>=10): break
print(total)

#continue문 조건에 해당이 되면 위로 다시 올려라 계속돌아가는 식
total=0
i=0
while i<10:
    if i%3==0:continue
    total+=i
    i+=1
print(total)

#예진이가 수정한 식
total=0
i=0
while i<10:
    if i%3==0:
        i+=1
        continue
    total+=i
    i+=1
print(total)

#교수님이 수정한 식
total=0
i=0
while i<9:
    i+=1
    if i%3==0:continue
    total+=i
print(total)
