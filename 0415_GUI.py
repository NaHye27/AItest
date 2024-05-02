# 1)느림, 그러나 친화적
# tkinter 프로그래밍 연습
from tkinter import*
window=Tk() #윈도우라는 인터페이스 GUI코딩의 시작

window.title("윈도우창 연습")
window.geometry("400x100")
window.resizable(width = TRUE, height = FALSE)
#TRUE로 할 경우 크기가 조절가능

window.mainloop() #field.behavior 것중 하나 GUI코딩의 마지막
# event를 루프함.마우스와 키보드로 형성됨.

#2)라벨 
from tkinter import*
window=Tk()

label1= Label(window, text = "COOKBOOK~~Python을")
label2= Label(window, text = "열심히", font = ("굴림", 30), fg = "blue")
label3= Label(window, text = "공부 중입니다.", bg = "magenta", width =20, height = 5, anchor =SE)
#텍스트의 정렬은 남동쪽(SE, South-East)

label1.pack()
label2.pack()
label3.pack()
#위치를 쌓는 것.(기본은 위에서 아래로 쌓는다는 의미)

window.mainloop()

#import tkinter as tk는 부를때 window = tk.Tk()
#from tkinter import*는 부를 때 window = Tk()

#3)포토 불러와서 저장
from tkinter import*
window=Tk()

window.title("GUI Ewercise")

photo1 = PhotoImage(file="SSSS.gif")
label1= Label(window, image=photo1)
photo2 = PhotoImage(file="SSSS.gif")
label2= Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)
#LEFT, RIGHT, UP ,DOWN

window.mainloop()


#4)버튼 이벤트 처리
from tkinter import*
window=Tk()

button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)
#quit은 내부 명령어.

button1.pack()

window.mainloop()

# 5)윗부분 종합 버튼을 이미지로.
from tkinter import*
from tkinter import messagebox

#함수 선언
def myFunc():
    messagebox.showinfo("심슨 버튼", "심슨이 이상하죠~!^^")

#메인코드 부분 정의된 변수는 함수에서 볼 수 있음.
window=Tk()

photo1 = PhotoImage(file="SSSS.gif")
button1 = Button(window, image = photo1, command=myFunc)
#버튼을 누르면 myFunc이 실행됨.

button1.pack()

window.mainloop()

# 6)체크버튼 변수 필요
from tkinter import*
from tkinter import messagebox
window=Tk()

def myFunc():
    if chk.get()==0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")

    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요.")


chk = IntVar()
cb1= Checkbutton(window, text="클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()


# 7)Radiobutton
from tkinter import*
window=Tk()

def myFunc():
    if var.get()==1:
        label1.configure(text="파이썬")
    elif var.get()==2:
        label1.configure(text="C++")
    else:
        label1.configure(text="Java")

var = IntVar()
rb1= Radiobutton(window, text = "파이썬", variable=var, value = 1, command=myFunc)
rb2= Radiobutton(window, text = "C++", variable=var, value = 2, command=myFunc)
rb3= Radiobutton(window, text = "Java", variable=var, value = 3, command=myFunc)

label1 = Label(window, text = "선택한 언어 : ", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()


# 8) Widget(Horizontal) alignment and resizing
#첫번째
from tkinter import*
window=Tk()

button1 = Button(window, text = "버튼1")
button2 = Button(window, text = "버튼2")
button3 = Button(window, text = "버튼3")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)

window.mainloop()

#두번째 
from tkinter import*
window=Tk()

#리스트에 담아서 생성, 리스트 3개 연달아 생성
btnList = [None]*3

for i in range(0, 3):
    btnList[i] = Button(window, text = "버튼" + str(i+1))

for btn in btnList:
    btn.pack(side = TOP, fill = X)
#TOP, BOTTOM도 있다.fill = X는 빈공간 없게.

window.mainloop()
