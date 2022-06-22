#!pip install datatable
# or
#!pip install git+https://github.com/h2oai/datatable

'''
3기가 짜리 데이터로 성능 테스트 해본 결과
m1으로 확인 해봤을때는 별 차이가 없음
ubuntu workstation으로 결과 확인했을때 2배 빠름
아마 c++로 짜져있는 코드라 clang 관련해서 차이가 나는듯
'''

import time
now = time.time()
pd.read_csv("mynavi.csv")
time.time() - now
# 43초 

import time
now = time.time()
dsk_Df = dt.fread("mynavi.csv")
dsk_Df = dsk_Df.to_pandas()
time.time() - now
# 23초
