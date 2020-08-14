def twoNumberSum(array, targetSum):
	obj = {}
    for i in array:
		targetNumber = targetSum - i
		if targetNumber in obj:
			return [i, targetNumber]
		else:
			obj[i] = True
	return []
