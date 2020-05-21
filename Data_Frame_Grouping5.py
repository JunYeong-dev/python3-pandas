import pandas as pd

# 데이터 프레임의 그룹화 5

df = pd.DataFrame([
    ['Apple', 3, 5, 'Fruit'],
    ['Banana', 2, 6, 'Fruit'],
    ['Beef', 7, 2, 'Meal'],
    ['Pork', 5, 8, 'Meal']],
    columns=["Name", "Frequency", "importance", "Type"])

df["Gap"] = df.groupby("Type")["Frequency"].apply(lambda x: x - x.mean())
print(df)