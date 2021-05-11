
import numpy as np 

class add: 
    def __init__(self): 
        self.x, self.y = None, None 
        self.z = None 
    
    def forward(self, x, y):
        self.x, self.y = x, y 
        self.f = self.x + self.y 
        return self.f 
    
    def backward(self, dvoi): 
        dx = dvoi
        dy = dvoi
        return dx, dy 

class subtract: 
    def __init__(self): 
        self.x, self.y = None, None 
        self.z = None 
    
    def forward(self, x, y):
        self.x, self.y = x, y 
        self.f = self.x - self.y 
        return self.f 
    
    def backward(self, dvoi): 
        dx = dvoi 
        dy = -1*dvoi
        return dx, dy

class multiply:
    def __init__(self): 
        self.x, self.y = None, None 
        self.z = None 
    
    def forward(self, x, y):
        self.x, self.y = x, y 
        self.f = self.x * self.y 
        return self.f 
    
    def backward(self, dvoi):
        dx = dvoi*self.y
        dy = dvoi*self.x 
        return dx, dy 

class divide:
    def __init__(self): 
        self.x, self.y = None, None 
        self.z = None 
    
    def forward(self, x, y):
        self.x, self.y = x, y 
        self.f = self.x / self.y 
        return self.f 
    
    def backward(self, dvoi):
        dx = dvoi * 1/self.y
        dy = dvoi * -self.x/(self.y**2) 
        return dx, dy 

class square:
    def __init__(self): 
        self.x = None
        self.z = None 
    
    def forward(self, x):
        self.x = x 
        self.f = self.x**2 
        return self.f 
    
    def backward(self, dvoi):
        dx = dvoi * 2*self.x
        return dx

class mean:
    def __init__(self): 
        self.x = None
        self.z = None 
    
    def forward(self, x):
        self.x = x 
        self.f = np.mean(x) 
        return self.f 
    
    def backward(self, dvoi):
        dx = dvoi * (1/self.x.shape[0])
        return dx
