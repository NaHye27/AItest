{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "14798b17-9d50-4679-a1b2-f8656d935bb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "세 개의 숫자를 입력해 주세요:  1 2 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3\n"
     ]
    }
   ],
   "source": [
    "a,b,c=map(int,input(\"세 개의 숫자를 입력해 주세요: \").split())#스플릿 안에 ,든 공간이든 넣어.\n",
    "print(a,b,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "17b39104-c0d2-4ffb-964a-e70fa7bfc7af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "세 개의 숫자를 입력해 주세요:  1 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n",
      "[1, 2]\n"
     ]
    }
   ],
   "source": [
    "#세 개의 숫자를 리스트로 변환\n",
    "a_list=list(map(int,input(\"세 개의 숫자를 입력해 주세요: \").split(',')))\n",
    "print(type(a_list))\n",
    "print(a_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1d2e0102-8384-42b3-ac93-ba05c635c56f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1', '2', '3']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"1,2,3\".split(',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "35f14b11-bbde-41c6-a24a-02adc74bc7e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "세 개의 숫자를 입력해 주세요:  1,2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n",
      "[1.0, 2.0]\n"
     ]
    }
   ],
   "source": [
    "a_list=list(map(float,input(\"세 개의 숫자를 입력해 주세요: \").split(',')))\n",
    "# float는 함수를 각각의 요소에 넣어줌.map은 앞,뒤 잘 매치함,list를 넣으면 구분할 필요가없다.\n",
    "print(type(a_list))\n",
    "print(a_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93b0f4a0-3e1c-4feb-abaa-7ca89e5282d7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "19794526-ab3d-429c-a8e6-8cfd141fe9ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO\n"
     ]
    }
   ],
   "source": [
    "a= 'hello'\n",
    "b=a.upper()#대문자로 변환, lower는 소문자로!\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9b0b02d7-fc10-4841-b196-53b120ec62e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'10 Test'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#문자열과 관련된 함수 {}안에\n",
    "'{} Test'.format(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3f9b42d4-250f-46ba-b1bc-cfe085ae7e42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'400 my 100 Test'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{2} {0} {1} Test'.format(\"my\",100,400)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "10dc4cd0-39f0-452a-9a03-88ac0eb837da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 번째 손님은 오늘의 101 번째 손님입니다.\n",
      "2 번째 손님은 오늘의 102 번째 손님입니다.\n",
      "3 번째 손님은 오늘의 103 번째 손님입니다.\n",
      "4 번째 손님은 오늘의 104 번째 손님입니다.\n",
      "5 번째 손님은 오늘의 105 번째 손님입니다.\n",
      "6 번째 손님은 오늘의 106 번째 손님입니다.\n",
      "7 번째 손님은 오늘의 107 번째 손님입니다.\n",
      "8 번째 손님은 오늘의 108 번째 손님입니다.\n",
      "9 번째 손님은 오늘의 109 번째 손님입니다.\n",
      "10 번째 손님은 오늘의 110 번째 손님입니다.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "for i in range(10):\n",
    "    a= '{} 번째 손님은 오늘의 {} 번째 손님입니다.'.format(i+1,i+101)\n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccdee5ed-a03b-405c-9c11-de825da78c38",
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
