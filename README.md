# SSAI
AI/ML toolkits for social scientists

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
