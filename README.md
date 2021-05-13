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


```
import numpy as np 
from ssai import generate 

SLR = generate.SimpleLinReg()

X = SLR.random_sampling()
Y = SLR.random_treatment(X)
```

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

--------------
### 2. Supervised Learning  

```
from ssai import propagate 

n_features = 1 
m_samples = 25

"""Hyperparameter"""
weight = np.random.randn(n_features, 1)
bias = np.random.randn(1) 
lr = 0.001 

"""Propagation"""
affine = propagate.LinReg.affine()
loss = propagate.LinReg.loss()
cost = propagate.LinReg.cost()


for _ in range (10000): 
        """Forward Propagation"""
        y_hat = affine.forward() 
        loss = loss.forward() 
        cost = cost.forward() 
        
        """Backward Propagation"""
        dloss = cost.backward()
        dy_hat = loss.backward()
        dw, db = affine.backward() 
        
        """Parameter Update"""
        weight -= lr*dw 
        bias -= lr*db     
```
--------------
#### propagate.LinReg.affine(weight, bias, x) 
--------------

Performs forward and backward propagation of Affine Function (y_hat). Affine forward propagation calculates affine function, given weight (w), bias (b) and input (x). Given dJ/dy_hat from the previous loss back propagation, affine back propogation calculates dJ/dw and dJ/db, with dy_hat/dw and dy_hat/db. dJ/dw = (dJ/dL)(dL/dy_hat)(dy_hat/dw) & dJ/db = (dJ/dL)(dL/dy_hat)(dy_hat/db)  

--------------

Forward Propagation

w : float 

b : float

x : Matrix (np.array) 


Backward Propagation  

dvoi : Vector (np.array)  

--------------
#### propagate.LinReg.loss(y, y_hat) 
--------------

Performs forward and backward propagation of Loss Function (L). Loss forward propagation calculates loss function, given y_hat (from the affine forward propagation) and y. Provided with dJ/dL from the previous cost back propagation, loss back propagation calculates dJ/dy_hat, with dL/dy_hat. dJ/dy_hat = (dJ/dL)(dL/dy_hat)  

--------------

Forward Propagation

y : Vector (np.array)  

y_hat : Vector (np.array)  


Backward Propagation  

dvoi : Vector (np.array)  

--------------
#### propagate.LinReg.cost(loss) 
--------------

Performs forward and backward propagation of Cost Function (J). Cost forward propagation calculates cost function, given loss (from the loss forward propagation). Cost back propagation calculates dJ/dL, given the sample size. 

--------------

Forward Propagation

loss : Vector (np.array)


Backward Propagation  

sample_size = int 

dvoi : int, default = 1  

--------------
