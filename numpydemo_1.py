from scipy import stats
import numpy
print(numpy.sum([11,22,33,44,55,66,77]))
k=[11,22,33,44,55,66,77,0,0]
print("count without zero",numpy.count_nonzero(k))
print("count including zero",numpy.size(k))
arr=numpy.array(k)
print("array types",arr)
print("list types:",k)
print("List zero index:",k[0])
print("Array zero index:",arr[0])
print("List last index:",k[-1])
print("Array last index:",arr[-1])
print("list max : ",numpy.max(k))
print("arr max : ",numpy.max(arr))
print("arr min : ",numpy.min(arr))
print("list min : ",numpy.min(k))
print("mean value :",numpy.mean([10,20,20,50]))
print("mean value :",numpy.mean(arr))
k=[11,22,33,44,55,66,77,0,0,34,99]
print("sort value:",numpy.sort(k))
print("median value:",numpy.median(k))
k=[11,22,33,44,55,66,77,0]
print("sort value:",numpy.sort(k))
print("reverse sort value:",numpy.sort(k)[::-1])

print("median value:",numpy.median(k))
k=[11,22,33,44,55,66,77,0,0,34,99,34,34,34,8]
print("mode :(maximum no. of apperance): ",stats.mode(k))


