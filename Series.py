import pandas as pd

# Pandas란?
# 데이터를 효과적으로 처리하고, 보여줄 수 있도록 도와주는 라이브러리
# Numpy와 함께 사용되어 다양한 연계적인 기능을 제공
# 인덱스(Index)에 따라 데이터를 나열하므로 사전(Dictionary) 자료형에 가까움
# 시리즈(Series)를 기본적인 자료형으로 사용
# 엑셀(Excel)과 거의 똑같음

# Series란?
# 시리즈는 인덱스과 값으로 구성됨

array1 = pd.Series(['사과', '딸기', '바나나'], index=['a', 'b', 'c'])

print(array1)
print(array1['a'])

data = {
    'd': '귤',
    'e': '포도',
    'f': '수박',
}

# Dict 자료형을 Series로 바꾸기
array2 = pd.Series(data)
print(array2)
print(array2['d'])