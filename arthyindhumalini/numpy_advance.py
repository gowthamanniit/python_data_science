import numpy
k=[11,11,22,11,44,55,22,9,12,13,0,0,0,14]
print("sum:",numpy.sum(k))
print("max:",numpy.max(k))
print("min:",numpy.min(k))
print("mean:",numpy.mean(k)) #29.3
print("median:",numpy.median(k)) # 22
print("count with zero:",numpy.size(k)) # 14
print("count without zero:",numpy.count_nonzero(k)) # 11
print("sort:",numpy.sort(k))
print("sort:",numpy.sort(k)[::-1])




