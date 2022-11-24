import time
def timing_val(func):
	def wrapper(*arg,**kw):
		t1=time.time()
		res=func(*arg,**kw)
		t2=time.time()
		return (t2-t1), res, func.__name__
	return wrapper

@timing_val
def testing():
	if __name__ == '__main__':
		print("success")


