def split_string(s):
	s2=""
	a=[]
	for i in range(len(s)-1,-1, -1):
		if s[i]==" ":
			a.append(s2)
			s2= ""
		else:
			s2=f"{s[i]}{s2}"
	a.append(s2)
	a.reverse()
	return a 
print(split_string("Go! Go! Go!"))