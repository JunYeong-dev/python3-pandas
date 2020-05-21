import numpy as np
import pandas as pd

# 데이터 프레임의 마스킹

df = pd.DataFrame(np.random.randint(1, 10, (2, 2)), index=[0, 1], columns=["A", "B"])
# 데이터 프레임 출력하기
print(df)
# 컬럼 A의 각 원소가 5보다 작거나 같은지 출력
print(df["A"] <= 5)
# 컬럼 A의 원소가 5보다 작고, 컬럼 B의 원소가 8보다 작은 행 출력
print(df.query("A <= 5 and B <= 8"))