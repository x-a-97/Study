# the while loop
def look_for_key(main_box):
	pile = main_box.make_a_pile_to_look_through()
	while pile is not empty:
		box = pile.grab_a_box()
		for item in box:
			if item.is_a_box():
				pile.append(item)
			elif item.is_a_key():
				print("found the key!")
# 递归recursive
def look_for_key(box):
	for item in box:
		if item.is_a_box():
			look_for_key(item)
		elif item.is_a_key():
			print("found the key!")

‘’‘
如果使用循环, 程序的性能可能更高
如果使用递归, 程序可能更容易理解
‘’‘

# 每个递归函数有两部分: 基线条件(base case) 和递归条件(recursive case)

def countdown(i):
	print i
	if i <= 0:	# 基线条件
		return
	else:
		countdown(i-1) # 递归条件
‘’‘
调用栈
’‘’
def greet(name):
	print("hello, " + name + "!")
	greet2(name)
	print("getting ready to say bye...")
	bye()

def greet2(name):
	print("how are you, " + name + "?")

def bye():
	print("ok bye!")

# 计算阶乘的递归函数

def fact(x):
	if x == 1:
	    return 1
	else:
		return x * fact(x-1)

