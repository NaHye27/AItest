{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2019c0e8-2952-4b1b-bc23-d6585047e574",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5! = 120\n",
      "120\n"
     ]
    }
   ],
   "source": [
    "def factorial(n): # n!의 재귀적 구현\n",
    "    if n <= 1 : # 종료조건이 반드시 필요하다\n",
    "        return 1\n",
    "    else :\n",
    "        return n * factorial(n-1) # n * (n-1)! 정의에 따른 구현! 펙토리얼 반복함.\n",
    "n = 5                             # 1보다 작아지면 0을 곱하게 돼서 불가능\n",
    "print('{}! = {}'.format(n, factorial(n)))\n",
    "print(factorial(5)) # 교수님이 짜신거."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cc97a4eb-ad01-425d-807d-c6d107925dd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "#for문으로 작성하는 법\n",
    "def factorial2(n):\n",
    "    tmp = 1\n",
    "    for i in range(n):\n",
    "        tmp *= (i+1)\n",
    "    return tmp\n",
    "\n",
    "print(factorial2(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8c8d5ae-ff84-440f-9ea6-e47dae73ba07",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fibonacci(n): # 피보나치 함수의 재귀적 구현\n",
    "    if n <= 1: # 피보나치 함수의 종료조건, 0까지 1,0이면 n으로 끝남.\n",
    "        return n\n",
    "    else:\n",
    "        return(fibonacci(n-1) + fibonacci(n-2)) # F_n = F_(n-1) + F_(n-2)\n",
    "        #2를 넣어도 1이 나옴.\n",
    "print(fibonacci(10)) #숫자 바꿔 넣어봐유!\n",
    "#nterms = int(input(\"몇 개의 피보나치수를 원하세요? \")) #수업피피티."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d1e65ef-ad97-43e8-ae94-3902013f045c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
