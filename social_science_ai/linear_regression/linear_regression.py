import numpy as np 

class affine_function: 
    
    def __init__(self): 
        self.w, self.b = None, None 
        self.y_hat = None 
    
    def forward(self, w, b, x): 
        self.w, self.b, self.x = w, b, x  
        self.y_hat = self.w*self.x + self.b
        return self.y_hat 
    
    def backward(self, dvoi): 
        dw = self.x * dvoi 
        db = dvoi
        return dw, db 

class loss_function: 
    
    def __init__(self): 
        self.y, self.y_hat = None, None 
        self.loss = None 
    
    def forward(self, y, y_hat): 
        self.y, self.y_hat = y, y_hat 
        self.loss = (self.y - self.y_hat)**2 
        return self.loss 
    
    def backward(self, dvoi): 
        dy_hat = dvoi * -2(self.y - self.y_hat)
        return dy_hat

class cost_function: 
    
    def __init__(self): 
        self.loss = None 
        self.cost = None 
        
    def forward(self, loss): 
        self.loss = loss 
        self.cost = np.mean(loss)
        return self.cost 
    
    def backward(self, dvoi):
        dloss = dvoi * 1/self.x.shape
        return dloss
