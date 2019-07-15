import math

# compute_mean(list) -> float
def compute_mean(l):
    mean = 0.0
    N=len(l)
    for i in l:
        mean+=i
    mean=mean/N
    return mean


# compute_median(list) -> float
def compute_median(l):
    N=len(l)
    l.sort()
    if N%2!=0:
        med_index=N//2
        median=l[med_index]
    if N%2==0:
        a=N//2
        b=N//2+1
        median=(l[a-1]+l[b-1])/2
    return median


# compute_variance(list) -> float
def compute_variance(l):
    variance = 0.0
    sum=0.0
    N=len(l)
    for i in l:
        sum+=i
    mean=sum/N
    for i in l:
        diff=(i-mean)**2
        variance+=diff
    variance=variance/N
    return variance


# compute_standard_deviation(list) -> float
def compute_standard_deviation(l):
    deviation = 0.0
    variance = 0.0
    sum=0.0
    N=len(l)
    for i in l:
        sum+=i
    mean=sum/N
    for i in l:
        diff=(i-mean)**2
        variance+=diff
    variance=variance/N
    deviation=math.sqrt(variance)
    return deviation


