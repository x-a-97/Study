'''
D&C策略包含两个步骤:
1. 找出基线条件, 这种条件必须尽可能简单
2. 不断将问题分解(缩小规模), 直到符合基线条件
‘’‘

‘’‘
诸如Haskell等函数式编程语言没有循环,
因此只能使用递归来编写这样的函数
'''

'''
快速排序
1. 选择基准值
2. 将数组分未两个子数组: 小于基准值的数组的元素 + 大于基准值的元素
3. 对这两个子数组进行快速排序
'''

def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [ i for i in array[1:] if i > pivot]

		return quicksort(less) + [pivot] + quicksort(greater)

    print quicksort([10, 5, 2, 3])
    		
