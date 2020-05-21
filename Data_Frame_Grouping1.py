import pandas as pd

# 데이터 프레임의 그룹화 1

df = pd.DataFrame([
    ['Apple', 3, 'Fruit'],
    ['Banana', 2, 'Fruit'],
    ['Beef', 7, 'Meal'],
    ['Pork', 5, 'Meal']],
    columns=["Name", "Frequency", "Type"])

print(df)
print(df.groupby(['Type']).sum())