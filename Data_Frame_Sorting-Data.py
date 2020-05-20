import pandas as pd

# 데이터 프레임 정렬 함수

word_dict = {
    'Apple': '사과',
    'Strawberry': '딸기',
    'Banana': '바나나',
    'Grape': '포도'
}

frequency_dict = {
    'Apple': 3,
    'Strawberry': 7,
    'Banana': 5,
    'Grape': 1
}

importance_dict = {
    'Apple': 5,
    'Strawberry': 3,
    'Banana': 1,
    'Grape': 2
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

print(summary)
# ascending 옵션이 False : 내림차순, True : 오름차순
summary = summary.sort_values('frequency', ascending=False)
print(summary)