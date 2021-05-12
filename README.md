# SSAI

SSAI is AI/ML toolkit for social scientists. 

SocialScienceAI (SSAI), as a platform, has been developed to achieve two main goals: (i) To be approachable for social scientists with no prior knowledge in machine learning, by compelte doumentation and tutorials (see www.socialscience.ai/MOOC), and (ii) To be able to easily, rapidly, and flexibily apply different machine learning algorithms in the fields of social science (see www.pypi.org/project/socialscience.ai/). We will constantly update on our process, but currently the package performs the following operations.  

    (i) Simple (univariate) Linear Regression
    (ii) Multiple (univariate) Linear Regression 
    (iii) Simple Multivariate Linear Regression 
    (iv) Multiple Multivariate Linear Regression  
    (v) Polynomial Regression (tbd) 

(*2021-01-15 : While our initial idea was to provide tutorials with the main focus on the applications of SSAI package, we realised that many students with a social science background lack mathematical foundations - namely Linear Algebra and Matrix Calculus - to understand such applications. For that reason, we decided to focus on producing introductory resources on essential math topics for the first half of 2021. Before any further updates, the package will only provide Supervised Learning for Linear Regression.)

<Supervised Learning: Simple Linear Regression>
--------------
linreg.generate()
--------------
Generate M random samples of a dependent variable (y) and N independent variables (x), that follows some linear regression defined. For multiple linear regression, assumes ... 
--------------
regression : function, default=1/2x+1

low,high : int, default=1,10

n_features : int, default=1

m_samples : int, default=100 

noise : float, default=0.1

noise_dist : string, default='Normal'

--------------

```
import ssai.generate 

SLR = generate.SimpleLinReg()

X = 

```
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
