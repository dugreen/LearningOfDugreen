import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res)

def multicore():	
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)

def normal():
	res = 0
	for i in range(1000000):
		res += i + i**2 + i**3
	for i in range(1000000):
		res += i + i**2 + i**3
def multithread():
	q = mp.Queue()
	t1 = td.Thread(target=job,args=(q,))
	t2 = td.Thread(target=job,args=(q,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	res1 = q.get()
	res2 = q.get()

if __name__ == "__main__":
	st = time.time()
	normal()
	st1 = time.time()
	print('normal time:',st1-st)
	multithread()
	st2 = time.time()
	print('multithreading time:',st2-st1)
	multicore()
	st3 = time.time()
	print('multcore time:',st3-st2)


