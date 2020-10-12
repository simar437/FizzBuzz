def foo(num, dic: dict):
	string = ''
	for i in dic:
		if num % i == 0:
			string += dic[i]
	return string if string else str(num)


dit = {3: 'Fizz', 5: 'Buzz'}
for i in range(1, 100):
	print(foo(i, dit))