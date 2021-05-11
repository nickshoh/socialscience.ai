# SSAI
AI/ML toolkits for social scientists

SocialScienceAI (SSAI) has been developed to achieve two main goals: (i) To be approachable for social scientists with no prior knowledge in machine learning, with compelte doumentation and tutorials (see socialscience.ai), and (ii) To be able to easily, rapidly, and flexibily apply different machine learning algorithms in the fields of social science. 
    
    (i) Single-Variable Linear Regression
    (ii) Multi-Variable Linear Regression 
    (iii) Polynomial Regression 
    (iv) Classification 
    (v) 
    (vi)
    (vii)
    (viii)
    (ix)
    (x)


<<Linear Regression>>

<Function & Parameters>
--------------
linreg.generate() 
(For n_features = 1 at the moment)
--------------
Generate M random samples of a dependent varibale (y) and N independent variables (x), that follows some linear regression defined. For multiple linear regression, assumes multivariate normality


--------------
regression : function, default=1/2x+1

low,high : int, default=1,10

n_features : int, default=1

m_samples : int, default=100 

noise : float, default=0.1

noise_dist : string, default='Normal'

--------------
linear_regression.batch() 
--------------
X : Matrix (n_features x m_samples)

Y : Row Vector (1 x m_samples)

batch_size : int, default=int(m_records/10)

--------------
linear_regression.affine(weight, bias, x) 
--------------

--------------
linear_regression.loss(y, y_hat) 
--------------

--------------
linear_regression.cost(loss) 
--------------

--------------
visualize.linreg()
--------------

--------------
visualize.loss(epoch = int, sample = int, feature = int) 
--------------

--------------
visualize.cost() 
--------------

--------------
visualize.neuralnet()
--------------

<Code Example>

```
batches = batch(X, Y, size = int)

weight, bias = initialize(weight, bias)
epochs = int 
lr = float 

weight_update = [] 
bias_update = [] 
batch_cost_update = [] 
epoch_cost_update = [] 

for epoch in (epochs): 
    for batch in (batches):
        X,Y = xbatch, ybatch
        y_hat = affine.forward() 
        loss = loss.forward() 
        cost = cost.forward() 
        
        dloss = cost.backward()
        dy_hat = loss.backward()
        dw, db = affine.backward() 
        
        weight -= lr*dw 
        bias -= lr*db 
        
        weight_update.append(weight)
        bias_update.append(bias)
        batch_cost_update.append(cost)
        
    epoch_cost_update.append(cost)
    
visualize.cost() 
visualize.linreg()
```
