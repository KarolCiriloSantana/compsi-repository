dic = {}
lsta = []
while True:
	inputs = input()
	if inputs == "9999":
		break
	else:
		inputs = inputs.split()
		n, m = map(int,inputs)
		lsta.append(n)
		dic[n] = m
while True:
    inputs = input()
    if inputs == "9999":
        break
    else:
        inputs = inputs.split()
        i, j, k = map(int,inputs)
        if dic[j] >= k:
            print("OK")
            valor = dic[j] - k
            dic[j] = valor
        else:
            print("ESTOQUE INSUFICIENTE")
            
for i in range(len(lsta)):
    print(f"{lsta[i]} {dic[lsta[i]]}")
