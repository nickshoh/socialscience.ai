# SSAI

SSAI is AI/ML toolkit for social scientists. 

SocialScienceAI (SSAI), as a platform, has been developed to achieve two main goals: (i) To be approachable for social scientists with no prior knowledge in machine learning, by compelte doumentation and tutorials (see www.socialscience.ai/MOOC), and (ii) To be able to easily, rapidly, and flexibily apply different machine learning algorithms in the fields of social science (see www.pypi.org/project/socialscience.ai/). We will constantly update on our process, but currently the package performs the following operations.  

    (i) Simple (univariate) Linear Regression
    (ii) Multiple (univariate) Linear Regression 
    (iii) Simple Multivariate Linear Regression 
    (iv) Multiple Multivariate Linear Regression  
    (v) Polynomial Regression (tbd) 

(*2021-01-15 : While our initial idea was to provide tutorials with the main focus on the applications of SSAI package, we realised that many students with a social science background lack mathematical foundations - namely Linear Algebra and Matrix Calculus - to understand such applications. For that reason, we decided to focus on producing introductory resources on essential math topics for the first half of 2021. Before any further updates, the package will only provide Supervised Learning for Linear Regression.)

## Supervised Learning: Simple Linear Regression

### 1. Generating (Simulating) Data 

--------------
#### generate.SimpleLinReg.random_sampling()
--------------

Generates identically distributed M random samples (via np.random.uniform, drawing samples from a uniform distribution.)

--------------

low,high : int, default=1,10

n_features : int, default=1

m_samples : int, default=50

--------------

--------------
#### generate.SimpleLinReg.random_treatment()
--------------

Given the input generated from random_sampling(), simulates simple linear regression. Independent distribution of potential outcomes is ensured by randomly selecting the output from y ~ N(y_hat, noise), where y_hat = 1/2x + 1 by default. That is, we follow the assumption of Normality and Homoskedasticity, and the process prevents knowing about the potential outcome on another sample given the observed outcome of one sample. 

--------------

n_features : int, default=1

m_samples : int, default=50

noise : float, default=0.1

noise_dist : string, default='Normal'

--------------

```
import ssai.generate 

SLR = generate.SimpleLinReg()

"""Default"""
X = SLR.random_sampling()
Y = SLR.random_treatment(X)

"""Adjust"""
n_features = 1
m_samples = 100 
noise = 0.5 

X = SLR.random_sampling(1, 50, n_features, m_samples)
Y = SLR.random_treatment(X, n_features, m_samples, noise)
```
### 2. Supervised Learning  
--------------
propagate.LinReg.affine(weight, bias, x) 
--------------

Performs forward and backward propagation. Forward propagation calculates affine function, given weight (w), bias (b) and input (x). Backward propagation calculates , given dvoi

--------------

Forward Propagation  
w : float 
b : float
x : Matrix (np.array) 

Backward Propagation  
dvoi : Vector (np.array)  

--------------
propagate.LinReg.loss(y, y_hat) 
--------------

--------------
propagate.LinReg.cost(loss) 
--------------
forward 

backward 
sample_size = int 
dvoi : np.array, default = 1  

### 3. Application   

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
