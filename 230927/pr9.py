import pandas as pd
from itertools import combinations


l = [['100','ryan','music','2'],
     ['200','apeach','math','2'],
     ['300','tube','computer','3'],
     ['400','con','computer','4'],
     ['500','muzi','music','3'],
     ['600','apeach','music','2']]

colname = range(len(l[0]))

data = pd.DataFrame(l)
data_ = pd.DataFrame()

유일성만족리스트 = []
모든이름의조합 = []

for 조합수 in range(1, len(colname)+1):
    컬럼이름의조합 = combinations(colname, 조합수)
    모든이름의조합.append(list(컬럼이름의조합))
    
for 이름조합 in 모든이름의조합:
    for 컬럼명 in 이름조합:
        #print(컬럼명)
        if len(컬럼명) == 1:
            data_[f'data[{컬럼명[0]}]'] = data[컬럼명[0]]
        elif len(컬럼명) == 2:
            data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}]'] = data[컬럼명[0]] + data[컬럼명[1]]
        elif len(컬럼명) == 3:
            data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}] + data[{컬럼명[2]}]'] = data[컬럼명[0]] + data[컬럼명[1]] + data[컬럼명[2]]
        elif len(컬럼명) == 4:
            data_[f'data[{컬럼명[0]}] + data[{컬럼명[1]}] + data[{컬럼명[2]}] + data[{컬럼명[3]}]'] = data[컬럼명[0]] + data[컬럼명[1]] + data[컬럼명[2]] + data[컬럼명[3]]
        
인덱스 = data_.columns

for i in 인덱스:
    if len(data_[i]) == len(data_[i].value_counts()):
        유일성만족리스트.append(i)

for i in range(len(유일성만족리스트)):
    for j in range(i+1, len(유일성만족리스트)):
        if 유일성만족리스트[i] in 유일성만족리스트[j]:
            유일성만족리스트[j] = '!'
            
len(유일성만족리스트) - 유일성만족리스트.count('!')