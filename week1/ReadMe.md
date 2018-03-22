# 세미콜론 스터디 1주차

## 1. Python 설치 및 PyCharm 설치

### 1.1. [윈도우에서의 Python 3.x 설치](http://flowarc.tistory.com/entry/파이썬Python-343-윈도우에-설치-무작정-따라하기)

### 1.2. [맥에서의 Python 3.x 설치](https://medium.com/@psychet_learn/python-기초-2장-python-설치-및-환경설정-mac-os-x-ver-9e7e6d46eb2c)

### 1.3. [Pycharm 설치](http://techdaddy.tistory.com/12)
***
## 2. Python의 큰 특징

### 2.1. Python은 인간다운 언어이다.

### 2.2. Python은 문법이 쉬어 빠르게 배울 수 있다.

### 2.3. Python은 간결하다.
***
## 3. Python의 자료형

### 3.1. Python의 숫자형

* Python은 Java와 달리 변수를 선언할때 *int, float, double*을 사용하지 않고 선언한다.


* `a = 123` , `a = 567` , `a = -178`-> 정수형으로 선언
* `a = 1.2`, `a = 3.141592`, `a = -3.5` -> 실수형으로 선언
* `a = 0x8ff`, `a = 0xABC` -> 16진수로 선언

***

### 3.2. 숫자형의 연산자

```python
# -*- coding:utf-8 -*-
a = 3
b = 2
print (a + b) # 결과는 5
print (a ** b) # '**'연산자는 a의 b제곱을 나타내는 연산자이다. 따라서 결과는 9이다.
print (a % b) # '%'연산자는 a를 b로 나눈 나머지의 값을 나타내는 연산자이다. 따라서 결과는 1이다.
```

***

### 3.3. Python의 문자열 자료형

* 문자열을 만드는 방법은 4가지가 있는데, 큰 따옴표, 작은 따옴표, 큰 따옴표 3개 연속, 작은 따옴표 3개를 연속으로 써서 하는 방법이 있다.

```python
# -*- coding:utf-8 -*-
a = "Hello World"
b = 'Python is fun'
c = "Python's favorite food is perl" # 문자열 안에 작은 따옴표가 있어 큰 따옴표로 선언
d = '"Python is very easy." he says.' # 문자열 안에 큰 따옴표가 있어 작은 따옴표로 선언 
e = """
Python's favorite food is
perl
"""

f = '''
Life is too short, 
You need Python
''' # 줄바꿈이 있는 문자열일 경우에는 큰, 작은 따옴표 3개를 연속해서 사용한다.
```

***

### 3.4. 문자열 연산하기

```python
# -*- coding:utf-8 -*-
a = "Hello"
b = " World!"
print (a + b) # a와 b가 '+' 연산자에 의해 문자열이 연결해진다. 따라서 결과는 'Hello World!' 이다.
print (a * 2) # a가 '*' 연산자에 의해 2번 곱해졌으니 a란 문자열이 2번 반복된다. 따라서 결과는 'HelloHello' 이다.
```

***

### 3.5. 문자열 인덱싱(Indexing)과 슬라이싱(Slicing)

* *인덱싱(Indexing)* 이란 무엇인가를 *"가르킨다"* 는 의미이고 *슬라이싱(Slicing)* 은 무엇인가를 *"잘라낸다"* 는 의미이다.


#### 문자열 인덱싱(indexing) 

```python
# -*- coding:utf-8 -*-
a = "Life is too short, You need Python" # 첫 번째 자리부터 숫자를 매기는데, 이 숫자는 0부터 시작한다.
#    0123456789...

print (a[3]) # 네 번째 문자열인 e를 출력한다.
print (a[-1]) # 뒤에서 첫 번째 문자열인 n을 출력한다.
print (a[0]) # 첫 번째 문자열인 L을 출력한다.
```

#### 문자열 슬라이싱(Slicing)

```python
# -*- coding:utf-8 -*-
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3] # 첫 번째 자리부터 세 번째 자리까지 더한다.
print (b) # 결과값은 Life

b = a[0:4] # 첫 번째 자리부터 네 번째 자리 미만까지 슬라이싱한다.
b = a[:4] # 첫 번째 자리부터 뽑아낼때엔 0을 생략해도 된다. 따라서 b는 Life
print (b) # 결과값은 Life

b = a[19:34] # 19 번째 자리부터 34 번째 자리 미만까지 슬라이싱한다. 
b = a[19:] # 19 번쨰 자리부터 끝자리 미만까지 슬라이싱한다. 따라서 b는 You need Python
print (b)
```

***

### 3.6. 문자열 포메팅

* 문자열에서 또 하나 알아야 할 것으로는 *문자열 포매팅(Formatting)* 이 있다. 
* 설명하기에 앞서 문자열 포맷 코드부터 설명하겠다.

| 코드 | 설명                      |
| ---- | ------------------------- |
| %s   | 문자열 (String)           |
| %c   | 문자 1개 (character)      |
| %d   | 정수 (Integer)            |
| %f   | 부동소수 (floating-point) |
| %o   | 8진수                     |
| %x   | 16진수                    |
| %%   | Literal % (문자 `%` 자체) |

```python
# -*- coding:utf-8 -*-
apple = 3
print ("I have %d apples" %apple) # apple이 정수이기 때문에 포맷 코드를 %d로 사용
print ("I have %s apples" %apple) # 또한 String으로도 넣을 수 있기 때문에 %s도 사용이 가능하다.

#아래는 list, for문과 포맷 코드를 이용해서 출력하는 코드이다.
fav_fruit = ['apple', 'banana', 'melon']
for fruit in fav_fruit:
    print ("I like a %s" %fruit)
"""
결과:
I like a apple
I like a banana
I like a melon
"""

name = 'RokHyungSon'
for i in range(3): # -> 3번 반복하는 for문
    print ("%s %d") %(name, (i + 1)) # 포맷 코드를 2개 이상 쓸 경우
"""
결과 :
RokHyungSon 1
RokHyungSon 2
RokHyungSon 3
"""
```

***

### 3.7. 문자열 관련 함수들

```python
# 문자 개수 세기 (count)
a = "apple"
print (a.count('p')) # apple안에 p가 2개 들어가니 출력값은 2이다.

#위치 알려주기 1 (find) -> 입력한 문자의 자릿값을 출력한다. 또한 이 함수는 대소문자를 구분한다.
a = "Python is best choice"
print (a.find('b')) # b가 11번째 자리에 있으니 10을 출력한다.
print (a.find ('k')) # k는 a란 문자열에 없으니 -1을 출력한다.

#자리 값이 어디인지 찾아주는 코드 
a = "Python is best choice"
user = input()
if a.find(user) == -1:
    print("찾으시는 %s의 문자를 찾을 수 없습니다." %user)
else:
    print ("찾으시는 %s는 %d 자리에 위치하고 있습니다." %(user, a.find(user)))
"""
결과:
P
찾으시는 P는 0 자리에 위치하고 있습니다.

p
찾으시는 p의 문자를 찾을 수 없습니다.
"""

#위치 알려주기 2 (index)
a = "Life is too short"
print (a.index('t')) # t가 9번째 자리에 위치하고 있으니 8을 출력한다.
print (a.index('k')) # index 함수는 find와 다르게 없는 문자를 찾으면 오류를 출력한다.

#문자열 삽입 (join) 
a = ","
print (a.join('abcd')) # abcd란 문자열 사이에 a, 즉 ',' 을 삽입한다.
# 결과 : a,b,c,d

#소문자에서 대문자로, 대문자에서 소문자로 바꾸기 (upper, lower)
a = "hi"
print (a.upper()) # 결과 : HI
a = "HI"
print (a.lower()) # 결과 : hi

#왼쪽 공백 , 오른쪽 공백, 양쪽 공백 지우기 (lstrip, rstrip, strip 함수)
a = "   hi"
print (a.lstrip()) # 결과 : "hi"

a = "hi     "
print (a.rstrip()) #결과 : "hi"

a = "     hi      "
print (a.strip()) #결과 : "hi"

#문자열 바꾸기 (replace)
a = "Life is too short"
print (a.replace("Life", "Your leg")) # a란 문자열 안에서 "Life"란 문자열을 "Your Leg"로 바꾼다.
#결과 : Your leg is too short
```









