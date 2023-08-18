ssimport numpy as np
import scipy as sp

fish_data = np.array([2,3,3,4,4,4,4,5,5,6])

N = len(fish_data)
sum_value = np.sum(fish_data)
mu = sum_value/N
print(np.mean(fish_data))
sigma_sq = np.sum((fish_data-mu)**2)/N
unbiased_sigma2 = np.var(fish_data,ddof =1) #불편분산 보정된 분산일때 1로 설정
sigma_sq2= np.var(fish_data,ddof =0) # 분산

sigma = np.sqrt(unbiased_sigma2)
sigma2 =np.std(fish_data, ddof =1)

Z_standard = fish_data - mu
Z_mean =np.mean(Z_standard)
Z_sigma = fish_data/sigma #unbiased_sigma

Z_sigma2 = np.std(fish_data/sigma, ddof=1) #sigma가 unbiased 이므로 ddof도 1로 설정

standard = (fish_data-mu)/sigma #표준화 평균을 빼고 표준편차로 나눔

