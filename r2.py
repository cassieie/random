import random
ans = random.randint(1,100)
x = 0
while True:
	g = input('請猜數字:')
	g = int(g)
	x += 1
	if g == ans:
		print('答對')
		print('猜第', x, '次')
		break
	elif g > ans:
		print('猜錯了,比答案大')
	else:
		print('猜錯了,比答案小')
	print('猜第', x, '次')