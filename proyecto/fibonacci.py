def serie(n):
    array=[0,1]
    i=0
    while i<n:
        subindice=array[-1]+array[-2]
        array.append(subindice)
        i=subindice
    return array
print(serie(377))