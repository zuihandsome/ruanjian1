from elevator import *

import threading

e1 = Elevator(1,0,10,800)
e2 = Elevator(2,1,10,800)
e3 = Elevator(3,2,10,800)
e4 = Elevator(4,0,20,2000)

# 创建线程
t1  = threading.Thread(target=e1.run)
t2  = threading.Thread(target=e2.run)
t3  = threading.Thread(target=e3.run)
t4  = threading.Thread(target=e4.run)
t1.start()
t2.start()
t3.start()
t4.start()



