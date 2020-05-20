import pandas as pd

# 시리즈 자료형의 연산
array1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])

# 같은 인덱스의 값을 더해줌
# fill_value : 같은 인덱스가 없는 경우 이 값을 더해줌; 이 옵션이 없는 경우 같은 인덱스가 없으면 NaN이 들어감
array_result1 = array1.add(array2, fill_value=0)
print(array_result1)
array_result2 = array1.add(array2, fill_value=1)
print(array_result2)
array_result3 = array1.add(array2)
print(array_result3)

