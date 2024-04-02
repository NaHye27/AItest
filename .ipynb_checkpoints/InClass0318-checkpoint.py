'''# 이재진.
name = input('당신의 이릉은? : ')

if name=='김나혜':
    print('바보디!!!')
elif name=='나해' or name=='김나해' or name=='나혜':
    print('여기도 바보다/11')
elif name=='이재진':
    print('재진이 최고!!')
else:
    print('오옹 그래??')

# for 설명
for i in range(10):
	print(i)

# Q 답 1)
iend=20
total=0
for i in range(iend):
    print(i)
    i+1 #없어도 값이 제대로 나오긴 해,,
    total=total+i+1
print(total)

# Q 답 2) 수정 필요 40 까지 2,4,6...
iend=20
total=0
for i in range(iend):
    print(i)
    i+1 #없어도 값이 제대로 나오긴 해,,
    total=total+2*(i+1)
print(total)

#for문
for m in ["사과", "배", "복숭아", "자몽"]:
    print("나는",m,"을 좋아합니다.")

#for문리스트에서 한가지 제외
for m in ["사과", "배", "복숭아", "자몽","캐슈넛"]:
    if m not in["캐슈넛"]:
        print("나는",m,"을 좋아합니다.")

# while문 일 경우
i=0
total=0
while i<20:
    i=i+1
    total=total+i
print(total)

#i like you 100번
for m in range(100): #m이 안쓰이는경우 _만 써도 됨
    print("I like you")

#for문과 리스트
numbers = [11, 22, 33, 44, 55, 66]

for n in numbers:
    print(n, end= '\n') #end=' ' 줄 바꾸지말고 빈칸으로 띄워라.

for ch in 'Hello':
    print(ch, end = ' ')'''

