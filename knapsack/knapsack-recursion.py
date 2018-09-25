def ks(n, c, w, v): 
	if n == 0 or c == 0:
		result = 0
	elif w[n-1] > c:
	    result = ks(n-1, c, w, v)
	else:
	    tmp1 = ks(n-1, c, w, v)
	    tmp2 = v[n-1] + ks(n-1, c - w[n-1], w, v)
	    result = max(tmp1, tmp2)
	return result
	
w = [10, 20, 30]
v = [60, 100, 120]	
n = len(v)
	
print ks(n, 50, w, v)	