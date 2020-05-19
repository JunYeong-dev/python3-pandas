import pandas as pd

word_dict = {
    'Apple': '사과',
    'Strawberry': '딸기',
    'Banana': '바나나'
}

frequency_dict = {
    'Apple': 3,
    'Strawberry': 7,
    'Banana': 5
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency
})

# 엑셀 내보내기
summary.to_csv("summary.csv", encoding="utf-8-sig")
# 엑셀 불러오기
saved = pd.read_csv("summary.csv", index_col=0)
print(saved)