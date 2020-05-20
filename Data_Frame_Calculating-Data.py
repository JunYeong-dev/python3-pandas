import pandas as pd

# 데이터 프레임의 연산

array1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])

print(array1)
print(array2)

# 데이터가 양쪽에 전부 없을 경우 -> NaN
array = array1.add(array2, fill_value=0)
print(array)

print("컬럼 1의 합: ", array[1].sum())
print(array.sum())