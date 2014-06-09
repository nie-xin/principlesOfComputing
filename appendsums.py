def appendsums(list):
	# Repeatedly append the sum of  of the current last three elements of list to list
	loops = 25
	while loops > 0:
		l_list = len(list)
		l_sum = list[l_list - 1] + list[l_list - 2] + list[l_list - 3]
		list.append(l_sum)
		loops = loops - 1

	return list

sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]