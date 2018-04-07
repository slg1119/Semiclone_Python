# 세미콜론 스터디 2주차

## 1. Python의 List

### 1.1. 리스트 (List)란?

* Python에서의 리스트(List)란, 순서가 있는 값들의 나열이라고 할 수 있다.
* 리스트(List)를 구성하는 값을 요소 혹은 원소라고 부르며 Java의 Array와 다르게 **어떠한 타입** 의 값이든 리스트의 요소로 올 수 있다.

***

### 1.2. 리스트 사용법

```python
# -*- coding:utf-8 -*-

sample1 = [] # 원소가 없는 빈 리스트
sample2 = [1, 2, 3, 4, 5] # 원소가 숫자인 리스트
sample3 = ['Life', 'is', 'short'] # 원소가 문자열인 리스트
sample4 = [1, 2, 'Life', 'is'] # 두 가지 타입이 들어간 리스트
sample5 = [1, 2, 3, 4, ['Life', 'is', 'short']] # 이중 리스트

# 리스트를 출력하는 방법
print (sample2) # [1, 2, 3, 4, 5]
print (sample2[0]) # 0번째 원소를 출력하니 1이 출력된다.
print (sample2[-1]) # -1 번째 원소 즉, 뒤에서 첫 번째의 원소를 호출하니 결과값은 5이다.
print (smaple2[1:3]) # 첫 번째 원소부터 세 번째 원소 미만까지 출력하기 때문에 출력은 [2, 3]이다.
print (sample2[:3]) # String과 같이 앞에 0을 생략 가능하다. 출력은 [1, 2, 3] 
print (sample5[4]) # sample5는 이중 리스트이고, 네 번째 원소는 리스트이기 때문에 출력은 ['Life', 'is', 'short'] 이다.
print (sample5[4][0]) # sample5의 네 번째의 있는 리스트 '['Life', 'is', 'short']'를 호출하고, 이 리스트의 0 번째인 'Life'를 호출하기 때문에 출력은 'Life'이다.
print (sample2[0] + sample2[1]) # sample2의 0번째 원소인 1과 2번째 원소인 2를 더하여 결과는 3이 나온다.
```

***

### 1.3. 리스트 연산자

```python
# -*- coding:utf-8 -*-

a = [1, 2, 3]
b = [4, 5, 6]

print (a + b) # a와 b를 더하면 각 원소들이 더해지는 것이 아닌, 리스트 자체가 더해진다. 결과는 [1, 2, 3, 4, 5, 6]이다.
print (a * 3) # a를 3을 곱하면 a 리스트가 3번 반복된다. 따라서 결과는 [1, 2, 3, 1, 2, 3, 1, 2, 3]
# -나, / 등의 연산자를 쓰면 오류가 발생한다.
```

***

### 1.4. 리스트의 수정, 변경과 삭제

```python
# -*- coding:utf-8 -*-

# 하나의 값 변경
a = [1, 2, 3]
a[2] = 4
print (a) # a의 두 번째 값인 '3'을 4로 수정했으므로 출력은 [1, 2, 4]가 된다.

# 연속된 범위의 값 수정하기
print (a[1:2]) # a[1:2]는 a[1]부터 a[2]까지를 말하는데, a[2]는 포함되지 않으므로 a[1]의 값인 2만 의미한다. 
a[1:2] = ['a', 'b', 'c']
print (a) # a[1]의 값인 2를 값을 대신해 a, b, c로 바꾸었으므로 2라는 값 대신에 a, b, c가 들어간다. 따라서 출력 값은 [1, 'a', 'b', 'c', 3]이다.

# del 함수를 사용해 리스트 요소 삭제하기
print (a) 
del a[0]
print (a) # del 함수를 이용해서 a 리스트의 0번째 값인 1을 삭제하므로 출력 값은 ['a', 'b', 'c', 3]이다.
```

***

### 1.5. 리스트 관련 함수들

```python
# append 함수
a = [1, 2, 3]
a.append(4) # append 함수는 리스트 마지막에 값을 추가한다.
print (a) # 출력값은 [1, 2, 3, 4]이다.
a.append([5, 6]) # append 함수를 사용하여 값을 넣는다면, 리스트 자체가 들어간다.
print (a) # 출력값은 [1, 2, 3, 4, [5, 6]]이다.

# sort 함수
a = [1, 4, 3, 2]
a.sort() # sort 함수는 리스트의 요소들을 순서대로 정렬해주는 함수이다.
print (a) # 출력값은 [1, 2, 3, 4]
a = ['a', 'c', 'b', 'd'] 
a.sort()
print (a) # 문자도 가능하므로 출력값은 ['a', 'b', 'c', 'd'] 이다.

# reverse 함수
a = [1, 4, 3, 2]
a.reverse()
print (a) # sort 함수와 달리 reverse 함수는 리스트 자체를 뒤집어 주는 함수로써 출력값은 [2, 3, 4, 1]이다.

# index 함수
a = [1, 2, 3, 4]
print (a.index(3)) # index 함수는 리스트에 x라는 값이 있으면 x의 위치값을 리턴하는 함수이다. 여기서 3이 두 번쨰 자리에 있으므로 2를 출력한다.
print (a.index(0)) # 하지만 index 함수는 x가 리스트 안에 없으면 오류를 출력한다.

# insert 함수
a = [1, 2, 3]
a.insert(0, 4) # insert 함수는 a의 자리에 b를 넣는 함수이다. 여기서 a == 0이고, b == 4이니, a라는 리스트의 0번째 자리에 4를 넣는다.
print (a) # [4, 1, 2, 3]

# remove 함수
a = [1, 2, 3, 1, 2, 3]
a.remove(3) # remove 함수는 제일 첫 번째로 오는 x를 삭제하는 함수이다. 여기서 x ==  3이니, 제일 첫 번째로 오는 3이 삭제된다.
print (a) # [1, 2, 1, 2, 3]

# count 함수
a = [1, 2, 3, 1, 1, 1]
print (a.count(1)) # count 함수는 리스트 안에 x가 몇개 있는지 돌려주는 함수이다. a에서 1은 4개 있으니 출력값은 4가 된다.

# extend 함수
a = [1, 2, 3]
a.extend([4, 5]) # append 함수와는 다르게 extend 함수는 리스트만 올 수 있고 리스트 안의 원소들을 더해준다.
print (a) # [1, 2, 3, 4, 5]
```
