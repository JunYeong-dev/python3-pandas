import pandas as pd

# 데이터 프레임의 그룹화 3

df = pd.DataFrame([
    ['Apple', 3, 5, 'Fruit'],
    ['Banana', 2, 6, 'Fruit'],
    ['Beef', 7, 2, 'Meal'],
    ['Pork', 5, 8, 'Meal']],
    columns=["Name", "Frequency", "importance", "Type"])

def my_filter(data):
    # mean() : 평균 값
    return data["Frequency"].mean() >= 5


print(df)
df = df.groupby("Type").filter(my_filter)
print(df)