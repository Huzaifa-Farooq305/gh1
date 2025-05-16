def decimal_to_binary(n):
    s=""
    while n>0:
        a=n%2
        n=int(n/2)
        s=f"{a}{s}"
    return s
print(decimal_to_binary(141))


def binary_to_decimal(b):
    d=0
    p=0
    while b>0: 
        m=b%10
        b=int(b/10)
        m=m*(2**p)
        p=p+1
        d=d+m
    return d
print(binary_to_decimal(1010110))
def decimal_to_hexadecimal(d):
	h=0
	s=""
	while d>0:
		m=d%16
		h=(h*10)+m
		d=int(d/16)
		if m==10:
			m="A"
		elif m==11:
			m="B"
		elif m==12:
			m="C"
		elif m==13:
			m="D"
		elif m==14:
			m="E"
		elif m==15:
			m="F"
		s=f"{m}{s}"
	return s
print(decimal_to_hexadecimal(978214))

def hexadecimal_to_decimal(h):
	p=0
	d=0
	for i in range(len(h)-1,-1,-1):
		x=h[i]
		if x=="A":		
			x="10"
		if x=="B":
			x="11"
		if x=="C":
			x="12"
		if x=="D":
			x="13"
		if x=="E":
			x="14"		
		if x=="F":
			x="15"
		x=int(x)
		m=x*16**p
		p=p+1
		d=d+m
	return d
print(hexadecimal_to_decimal("23ACCBDEF"))

def hexadecimal_to_binary(s):
	stri=""
	string=""
	for x in s:
		if x=="A":		
			x="10"
		if x=="B":
			x="11"
		if x=="C":
			x="12"
		if x=="D":
			x="13"
		if x=="E":
			x="14"		
		if x=="F":
			x="15"
		x=int(x)
		d=decimal_to_binary(x)
		d=str(d)
		if len(d)==1:
			d=f"0{d}"
		if len(d)==2:
			d=f"00{d}"
		if len(d)==3:
			d=f"0{d}"
		if len(d)==4:
			d=f"{d}"
		string=f"{string}{d}"
	return string
	
print(hexadecimal_to_binary("A1B2C3"))

def binary_to_hexadecimal(b):
    s=""
    while b>0:
        a=b%10000
        b=int(b/10000)
        m=binary_to_decimal(a)
        if m==10:
           m="A"
        elif m==11:
           m="B"
        elif m==12:
           m="C"
        elif m==13:
           m="D"
        elif m==14:
          m="E"
        elif m==15:
          m="F"
        s=f"{m}{s}"
    return s
print(binary_to_hexadecimal(11111111))