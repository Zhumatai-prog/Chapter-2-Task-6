num = input("Enter a digit: ")

count = 1

for i in range(11):
	for j in num:
		if count == 10:

			print (j)
			break
		else:
			count = count + 1

	if count == 10:
		break