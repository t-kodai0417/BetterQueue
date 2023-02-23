# BetterQueue
標準ライブラリ`queue`で関数を実行するときの自分用のやつ。

Example:
```python
from queue import Queue
import time
from BetterQueue import BetterQueue

q = BetterQueue(Queue())

def print_data(data,data2):
    print(data+data2)

def thread_queue():
    while True:
        if not q.empty():
            data = q.get()
            q.run(data)
        time.sleep(5)

if __name__ == "__main__":
    q.put([print_data,("Hello! ","How are you?")])#tuple
    q.put([print_data,{"data":"See ","data2":"you!"}])#dict
    BetterQueue.start(thread_queue)
```
