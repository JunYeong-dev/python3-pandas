import pandas as pd

# 데이터 프레임의 그룹화 4

df = pd.DataFrame([
    ['Apple', 3, 5, 'Fruit'],
    ['Banana', 2, 6, 'Fruit'],
    ['Beef', 7, 2, 'Meal'],
    ['Pork', 5, 8, 'Meal']],
    columns=["Name", "Frequency", "importance", "Type"])

# get_group() : 특정 그룹의 데이터만 가져옴
df = df.groupby("Type").get_group("Fruit")
print(df)