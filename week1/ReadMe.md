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











