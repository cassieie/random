import random
ans = random.randint(1,100)
while True:
	g = input('請猜數字:')
	g = int(g)
	if g == ans:
		print('答對')
		break
	elif g > ans:
		print('猜錯了,比答案大')
	else:
		print('猜錯了,比答案小')