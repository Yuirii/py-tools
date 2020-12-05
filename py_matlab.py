import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

## bernoulli
X = np.arange(0,4,1)
p = 0.1
pList = stats.bernoulli.pmf(X,p)
#get random_value probability
pList

#plot 默认绘制折线图 离散：lifestyle==none
plt.figure('Xtest1')
plt.plot(X, pList, 'o')
plt.vlines(X, 0, pList)#绘制竖线
plt.xlabel('X')
plt.ylabel('Probability')
plt.title('bernoulli: p=%.2f' % p)


## nibom二项分布
plt.figure('Ytest2')
nY = 5
pY = 0.5
Y = np.arange(0, nY+1, 1)
pListY = stats.binom.pmf(Y, nY, pY)
pListY

plt.plot(Y, pListY, 'o')
plt.vlines(Y, 0, pListY)
plt.xlabel('Y')
plt.ylabel('Probability')
plt.title('binom: n=%d, p=%.2f'%(nY, p))


## 几何分布


## 泊松分布

plt.show()