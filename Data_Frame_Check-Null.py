import pandas as pd
import numpy as np

# 데이터 프레임의 Null 여부 확인

word_dict = {
    'Apple': '사과',
    'Strawberry': '딸기',
    'Banana': '바나나',
    'Grape': '포도'
}

frequency_dict = {
    'Apple': 3,
    'Strawberry': 7,
    'Banana': np.nan,
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
# notnull() : 값이 null인 경우 false, 아닌 경우 true
print(summary.notnull())
# isnull() : 값이 null인 경우 true, 아닌 경우 false
print(summary.isnull())
# fillna('문자') : null인 데이터를 해당하는 문자로 바꿔줌
summary['frequency'] = summary['frequency'].fillna('데이터 없음')
print(summary)