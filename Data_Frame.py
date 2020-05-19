import pandas as pd

# Data Frame란?
# 다수의 시리즈(Series)를 모아 처리하기 위한 목적으로 사용
# 표 형태로 데이터를 손쉽게 출력하고자 할 때 사용

word_dict1 = {
    'Apple': '사과',
    'Strawberry': '딸기',
    'Banana': '바나나'
}

frequency_dict1 = {
    'Apple': 3,
    'Strawberry': 7,
    'Banana': 5
}

word1 = pd.Series(word_dict1)
frequency1 = pd.Series(frequency_dict1)

# 이름(Name): 값(Values) 형태로 변형
summary1 = pd.DataFrame({
    'word': word1,
    'frequency': frequency1
})

print(summary1)

# 시리즈의 연산
# 시리즈를 서로 연산하여 새로운 시리즈를 만들 수 있음

word_dict2 = {
    'Apple': '사과',
    'Strawberry': '딸기',
    'Banana': '바나나'
}

frequency_dict2 = {
    'Apple': 3,
    'Strawberry': 7,
    'Banana': 5
}

importance_dict1 = {
    'Apple': 5,
    'Strawberry': 3,
    'Banana': 1
}

word2 = pd.Series(word_dict2)
frequency2 = pd.Series(frequency_dict2)
importance = pd.Series(importance_dict1)

summary2 = pd.DataFrame({
    'word': word2,
    'frequency': frequency2,
    'importance': importance
})

score = summary2['frequency'] * summary2['importance']
summary2['score'] = score

print(summary2)

# 데이터 프레임의 슬라이싱

word_dict3 = {
    'Apple': '사과',
    'Strawberry': '딸기',
    'Banana': '바나나',
    'Grape': '포도'
}

frequency_dict3 = {
    'Apple': 3,
    'Strawberry': 7,
    'Banana': 5,
    'Grape': 1
}

importance_dict2 = {
    'Apple': 5,
    'Strawberry': 3,
    'Banana': 1,
    'Grape': 2
}

word3 = pd.Series(word_dict3)
frequency3 = pd.Series(frequency_dict3)
importance2 = pd.Series(importance_dict2)

summary3 = pd.DataFrame({
    'word': word3,
    'frequency': frequency3,
    'importance': importance2
})

print(summary3)

# 이름을 기준으로 슬라이싱
# Strawberry에서 Banana까지의 데이터를 가져오는데
# importance부터 오른쪽에 있는 데이터를 가져오겠다는 의미
print(summary3.loc['Strawberry':'Banana', 'importance':])

# 인덱스를 기준으로 슬라이싱
print(summary3.iloc[1:3, 2:])