import threading
import time
import queue


class Produce(threading.Thread):
    def run(self):
        # 把queue转化为全局变量,使得可以改变的队列的数量
        global queue
        # 此为生产数量
        count = 0
        while True:
            # qsize返回queue的长度
            if queue.qsize() < 1000:
                # 生产者每次制造100个产品
                for i in range(100):
                    # 每制造一个加1
                    count = count + 1
                    # 每制造一个产品,把产品的名称放入msg保存
                    msg = '生成产品' + str(count)
                    # put是往queue中放入一个值
                    queue.put(msg)
                    print(msg)
            # 如果产品大于了1000个后休息0.5秒
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            # 当库存大于100的时候执行
            if queue.qsize() > 100:
                # 每次消费3个
                for i in range(3):
                    # get是从queue中去除一个值
                    msg = self.name + '消费了 ' + queue.get()
                    print(msg)
            # 当库存小于100的时候,休息1秒
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品' + str(i))
    for i in range(2):
        p = Produce()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()