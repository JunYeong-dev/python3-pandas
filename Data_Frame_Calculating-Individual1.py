import pandas as pd

# 데이터 프레임의 개별연산 1

df = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index=[0, 1], columns=["A", "B", "C", "D"])
print(df)

# apply() : 함수를 적용시킴
df = df.apply(lambda x: x + 1)
print(df)

def addOne(x):
    return x + 1

df = df.apply(addOne)
print(df)