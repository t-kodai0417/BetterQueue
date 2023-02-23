from threading import Thread

class BetterQueue:
    def __init__(self,q):
        self.q = q
    
    def run(self,data:list):
        func = data[0]
        try:
            args = data[1]
        except:
            args = None
        
        if type(args) == dict:
            func(**args)
        elif type(args) == tuple:
            func(*args)
        else:
            func()
    
    def get(self):
        return self.q.get()
    
    def empty(self):
        return self.q.empty()
    
    def put(self,action:list):
        self.q.put(action)
    
    @staticmethod
    def start(func):
        thread = Thread(target=func)
        thread.start()
