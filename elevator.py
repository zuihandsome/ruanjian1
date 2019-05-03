import time
# 电梯走一层所需要的时间 /S
SPEED = 2

# 电梯类
class Elevator:
    def __init__(self,eNum,type,pMaxNum,weight):
        """
        :param eNum: 电梯编号
        :param type: 电梯类型 0 全部楼层 1 单层 2 双层
        :param pMaxNum: 最大载客量
        :param weight: 最大载重量
         pNum      : 现载客量
         direction : 电梯运行方向  1 上 0 下
         floor     : 电梯所在楼层
         list      : 记录电梯所有需要停下的楼层
         maxFloor  : 记录运行方向最远的楼层
         status    : 电梯状态 0 等待 1 运行 2 操作
        """
        self.eNum = eNum
        self.type = type
        self.pMaxNum = pMaxNum
        self.weight = weight
        self.pNum = 0
        self.direction = 1
        self.floor = 0
        self.list = []
        self.maxFloor = 0
        self.status = 0
        self.signal = 0
    # 电梯日志函数
    def log(self):
        if self.direction==0:
            print("电梯 " + str(self.eNum) + " 所在楼层 " + str(self.floor) +
                  " 电梯运行方向 " + "↓" )
        else:
            print("电梯 " + str(self.eNum) + " 所在楼层 " + str(self.floor) +
                  " 电梯运行方向 " +  "↑")

    # 电梯上下函数函数
    def operation(self):
        time.sleep(SPEED)
        self.floor += 1 if self.direction else -1
        if self.floor==20:
            if self.direction == 1:
                self.direction = 0
            else:
                self.direction = 1

    # 权值
    def weighT(self,num,direction):
        """
        算法尚不完备
        :param num: 所在楼层
        :param direction: 要去的方向
        :return: 权值 权值小的电梯接任务
        """
        if (num%2==0 and (self.type==0 or self.type==2)) or (num%2==1 and (self.type==0 or self.type==1)):
            if self.pNum<self.pMaxNum:
                if self.direction == direction:
                    if direction==1:
                        if self.floor>num:
                            return 2*self.maxFloor-num-self.floor
                        else:
                            return num-self.floor
                    else:
                        if self.floor<num:
                            return self.floor+num-2*self.maxFloor
                        else:
                            return self.floor-num
                else:
                    if direction==1:
                        if self.floor<num:
                            return self.floor+num-2*self.maxFloor
                        else:
                            if self.maxFloor<num:
                                return self.floor+num-2*self.maxFloor
                            else:
                                return self.floor-num
                    else:
                        if self.floor>num:
                            return 2*self.maxFloor-num-self.floor
                        else:
                            if self.maxFloor>num:
                                return 2*self.maxFloor-num-self.floor
                            else:
                                return num-self.floor

        return 999

    # 接 当乘客在外面按下按键
    def pickUp(self,num,direction):
        """
        :param num: 要接的乘客在几楼
        :return: None
        """
        self.list.append(num)
        self.maxFloor= max(self.maxFloor,num)
        if self.status==0:
            self.status = 1
            self.direction = direction
        print("电梯 " + str(self.eNum) + "接单了")

    # 乘客进入
    def comeIn(self,pNum):
        """
        :param pNum: 上电梯人数
        :return: None
        """
        #pNum = input("有几位乘客要进入电梯？")
        if pNum + self.pNum <= self.pMaxNum:
            self.pNum += pNum
            print("成功进入乘客 " + str(pNum) + " 位，电梯上共有乘客 " + str(self.pNum) + " 位。")
        else:
            self.pNum = self.pMaxNum
            print("进入乘客 " + str(self.pMaxNum-self.pNum) + " 位，因为电梯人数已满有 "
                  + str(pNum-self.pMaxNum+self.pNum) + " 位乘客没有进入电梯")

    # 送 乘客在轿厢内按下按键
    def send(self,num):
        """
        :param num: 去几楼
        :return: None
        """
        #num = input("请输入想要去的楼层")
        if not len(self.list):
            if self.floor>num :
                self.direction=0
            else:
                self.direction=1
        self.list.append(num)
        self.status = 1
        if self.direction==1:
            self.maxFloor = max(self.maxFloor,num)
        else:
            self.maxFloor = min(self.maxFloor,num)

    # 乘客下电梯
    def leave(self,num):
        # num = input("电梯上共有 " + str(self.pNum) + " 有几位乘客要在此楼层下电梯？")
        print(str(num) + " 位乘客在 " + str(self.floor) + " 下了电梯")
        self.pNum -= num
        if len(self.list):
            if self.floor==self.maxFloor:
                self.changeDirection()
        else:
            self.status = 0

    # 电梯改变方向
    def changeDirection(self):
        if self.direction==1:
            self.direction=0
            self.maxFloor = sorted(self.list)[0]
        else:
            self.direction=1
            self.maxFloor = sorted(self.list)[0]
    def run(self):
        while(1):
            while(self.status==1):
                self.operation()
                self.log()
                if(self.floor in self.list):
                    self.list.remove(self.floor)
                    self.status = 2
                    print("等待进行上下电梯选择楼层操作")
                    print(self.list)
                    while(self.signal<1):
                        x=1
                    self.signal = 0
                    # self.leave()
                    # self.comeIn()
                    # self.send()







