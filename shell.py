import C0w

while True:
	text = input('C0w >> ')
	result, error = C0w.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)