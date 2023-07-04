##import threading
##def one(name,lock):
##    lock.acquire()
##    new()
##    print(name,token)
##    lock.release()
##token = 0
##def new():
##    global token
##    token = token+1
##
##l1 = threading.Lock()
##t1 = threading.Thread(target = one,args = ["dhoni",l1])    
##t2 = threading.Thread(target = one,args = ["virat",l1])
####t3 = threading.Thread(target=one,args=["bharani",l1])
##
##t1.start()
##t2.start()
####t3.start()
##
##t1.join()
##t2.join()
####t3.join()



##import threading
##def one(name,lock):
##    lock.acquire()
##    new()
##    print(name,token)
##    
##token = 0
##def new():
##    global token
##    token = token+1
##
##l1 = threading.Lock()
##t1 = threading.Thread(target = one,args = ["dhoni",l1])    
##t2 = threading.Thread(target = one,args = ["virat",l1])
####t3 = threading.Thread(target=one,args=["bharani",l1])
##
##t1.start()
##t2.start()
####t3.start()
##
##t1.join()
##t2.join()
####t3.join()



import threading
 
lock = threading.RLock()
 
def funcA():
  print(" acquiring lock")
  lock.acquire()
   
  print(" lock acquired")
   
  print("acquiring lock again")
  lock.acquire()
   
  print("lock acquired again 2")
   
  print("releasing lock")
  lock.release()
   
  print(" lock released 2")
   
 
def funcB():
  print("In B, trying to acquire lock, but A released only once, so entering in deadlock state")
  lock.acquire()
  print("This statement won't be executed")
   

thread1 = threading.Thread(target=funcA)
thread2 = threading.Thread(target=funcB)
 
thread1.start()
thread2.start()
 
thread1.join()
thread2.join()



