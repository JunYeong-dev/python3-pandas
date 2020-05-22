import numpy as np
import pandas as pd

# 피벗 테이블의 기초
# 열과 행을 서로 바꾸는 등 다양한 처리가 가능하게 만들어줌

df = pd.DataFrame([
    ['Apple', 3, 5, 'Fruit'],
    ['Banana', 2, 6, 'Fruit'],
    ['Strawberry', 5, 6, 'Fruit'],
    ['Rice', 2, 6, 'Meal'],
    ['Beef', 7, 2, 'Meal'],
    ['Pork', 5, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])

print(df)

# aggfunc : 같은 index에서 어떤 값을 표시할 것인지 설정
df = df.pivot_table(
    index="Importance", columns="Type", values="Frequency",
    aggfunc=np.max
)

print(df)