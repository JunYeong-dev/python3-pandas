import pandas as pd

# 데이터 프레임의 개별연산 2

df = pd.DataFrame([
    ['Apple', 'Apple', 'Strawberry', 'Banana'],
    ['Grape', 'Banana', 'Apple', 'Blueberry']],
    index=[0, 1],
    columns=["A", "B", "C", "D"])

print(df)
# 특정 데이터를 찾아 변경
df = df.replace({"Apple": "Cherry"})
print(df)