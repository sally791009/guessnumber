import random
r = random.randint(1,100)
while True:
	num = input('請從1-100猜一個數字')
	num = int(num)
	if num == r:
		print('恭喜！你會通靈')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	
