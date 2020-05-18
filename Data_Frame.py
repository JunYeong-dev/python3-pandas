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