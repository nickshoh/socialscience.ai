def f(x): 
    return 0.5*x + 1  

def generate(equation=f(x), low=1, high=10, n_features=1, m_samples=25, noise=0.1, noise_dist='Normal'):
    
    y = np.empty([n_features, m_samples])
    y_hat = equation
    
    for i in range (0, m_samples):
        y_rvs = sp.stats.norm(loc=y_hat[0,i], scale=noise).rvs(size=(1,100))
        y[0][i] = np.random.choice(y_rvs[0], 1)
    
    return x, y