class visualize: 
    
    def __init__(self): 
        self.w = None
        self.b = None 
    
    def loss(self, epoch, sample, feature):
        self.epoch = epoch 
        self.sample = sample 
        self.feature = feature 
        
        def OLS(w,b): 
            y_hat = w*x[self.feature, self.sample] + b 
            loss = (y[self.feature, self.sample] - y_hat)**2
            return loss
        
        fig = plt.figure(figsize=(5,5))
        ax = plt.axes(projection='3d')
        
        w = np.linspace(-5,5,10)
        b = np.linspace(-5,5,10)
        w, b = np.meshgrid(w,b)
        
        ax.plot_surface(w, b, OLS(w,b), rstride=1, cstride=1,
                        cmap='winter', edgecolor='none', alpha=.5)
        ax.plot_wireframe(w, b, OLS(w,b), color='grey', alpha=.5)
        ax.scatter(weight, bias, OLS(weight,bias), color='red', marker ='o')
        
        return plt.show()