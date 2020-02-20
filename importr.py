import random
start = input('請輸入數字範圍起始值：')
end = input('請輸入數字範圍結束值：')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1 # = count + 1
	num = input('請從1-100猜一個數字')
	num = int(num)
	if num == r:
		print('恭喜！你會通靈')
		print('這是你猜第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜第', count, '次')
