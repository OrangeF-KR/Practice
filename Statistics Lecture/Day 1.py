import seaborn as sns
import numpy as np
import matplotlib as plt
import pandas as pd
import scipy.stats as stats

'''
df = pd.DataFrame({'a': [1, 2, 3], 'b': [2, 4, 6]}) #딕셔너리
corr = df.corr() #df.corr()은 DaraFrame의 모든 열 간의 상관계수를 계산(correlation)
print(corr)
print(stats.pearsonr(df['a'],df['b'])) #피어슨의 상관계수(Pearson's Correlation coefficient)
'''
#<Tips Data set>
'''
#seaborn과 matplot 사용하여 시각화하기 
tips = sns.load_dataset('tips')
tips.head(6)
ax = sns.regplot(x='total_bill',y='tip',data=tips ) #regplot
joint = sns.jointplot(x='total_bill',y='tip',data=tips)
#jointplot : 산점도와 히스토그램을 함께 표현한 그래프
#히스토그램을 통해 자료가 어느 구간에 집중되어 있는지 확인, 산점도를 통해 두 변수의 선형관계 확인

sns.pairplot(data = tips) #pairplot : 주어진 데이터의 각 feature간의 관계를 표시 / 데이터 간의 관계를 한 눈에 알아볼 수 있음.
'''

#heatmap이란 정사각형 그림에 데이터간의 관계를 색상으로 구분하여 표현
raw = sns.load_dataset('titanic')
raw.corr()
df = raw.corr()
sns.clustermap(df,
               annot = True,
               cmap = "RdYlBu_r",
               vmin = -1, vmax = 1,) #clustermap : 비슷한 변수들을 묶어서 표현 / 같이 묶일수록 연관성이 높음
#heatmap mask : 히트맵 그래프 중 한쪽을 보이지 않도록 만드는 것
df = raw.corr()
fig, ax = plt.subplots( figsize=(7,7) )

# 삼각형 마스크를 만든다(위 쪽 삼각형에 True, 아래 삼각형에 False)
mask = np.zeros_like(df, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# 히트맵을 그린다
sns.heatmap(df,
            cmap = 'RdYlBu_r',
            annot = True,   # 실제 값을 표시한다
            mask=mask,      # 표시하지 않을 마스크 부분을 지정한다
            linewidths=.5,  # 경계면 실선으로 구분하기
            cbar_kws={"shrink": .5},# 컬러바 크기 절반으로 줄이기
            vmin = -1,vmax = 1   # 컬러바 범위 -1 ~ 1
           )
plt.show()