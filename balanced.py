open_list = ["[","{","("]
close_list = ["]","}",")"]

def is_balance(my_str):

	stack = []
	
	for i in my_str:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return False
	if len(stack) == 0:
		return True
	else:
		return False


def main():
	inp = input('Please Enter Tags : ')

	print(is_balance(inp))

if __name__ == '__main__':
  main()
