import numpy as np 

class affine_function: 
    
    def __init__(self): 
        self.w, self.b = None, None 
        self.y_hat = None 
    
    def forward(self, w, b, x): 
        self.w, self.b, self.x = w, b, x  
        self.y_hat = np.dot(self.w.T, self.x) + self.b
        return self.y_hat 
    
    def backward(self, dvoi):  
        self.dw = np.dot(dvoi, self.x.T) 
        
        self.db = np.ones((self.x.shape[1],1))
        self.db = np.dot(dvoi,self.db) 
        return self.dw, self.db 

class loss_function: 
    
    def __init__(self): 
        self.y, self.y_hat = None, None 
        self.loss = None 
    
    def forward(self, y, y_hat): 
        self.y, self.y_hat = y, y_hat 
        self.loss = (self.y - self.y_hat)**2 
        return self.loss 
    
    def backward(self, dvoi): 
        self.dy_hat = -2 * (self.y - self.y_hat)
        self.dy_hat = np.diag(self.dy_hat[0])
        self.dy_hat = np.dot(dvoi,self.dy_hat)
        return self.dy_hat

class cost_function: 
    def __init__(self): 
        self.loss = None 
        self.cost = None 
        
    def forward(self, loss): 
        self.loss = loss 
        self.cost = np.mean(loss)
        return self.cost 
    
    def backward(self, sample_size, dvoi): 
        self.dloss = 1/sample_size * np.ones((1,sample_size))
        self.dloss = dvoi * self.dloss
        return self.dloss
