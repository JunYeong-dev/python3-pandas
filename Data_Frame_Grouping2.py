import numpy as np
import pandas as pd

# 데이터 프레임의 그룹화 2

df = pd.DataFrame([
    ['Apple', 3, 5, 'Fruit'],
    ['Banana', 2, 6, 'Fruit'],
    ['Beef', 7, 2, 'Meal'],
    ['Pork', 5, 8, 'Meal']],
    columns=["Name", "Frequency", "importance", "Type"])

print(df)
# aggregate() : 여러 개의 groupby를 한꺼번에 수행 가능
print(df.groupby(["Type"]).aggregate([min, max, np.average]))
