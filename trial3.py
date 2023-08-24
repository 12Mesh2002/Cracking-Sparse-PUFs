import numpy as np

def l(w, X, y):
    n = len(X)
    loss = np.sum((np.dot(X, w) - y)**2) / (2*n)
    return loss

def gradient(w, X, y):
    n = len(X)
    grad = np.dot(X.T, np.dot(X, w) - y) / n
    return grad

def update_weights(w, eta, grad):
    new_w = w - eta * grad
    return new_w

# def project_weights(w, S):
#     new_w = np.clip(w, -S, S)
#     return new_w

def convergence(w, new_w, tol):
    diff = np.linalg.norm(w - new_w)
    return diff <= tol
    
def HT( v, k ):
    t = np.zeros_like( v )
    if k < 1:
        return t
    else:
        ind = np.argsort( abs( v ) )[ -k: ]
        t[ ind ] = v[ ind ]
        return t

def my_fit( X_trn, y_trn ):
#def fit(X, y, eta, S, tol):
    n, d = X_trn.shape
    w = np.zeros(d)  # Initialize w0
    t = 0
    eta = 0.01  # Learning rate
    S = 512  # Constraint value for weight projection
    tol = 1e-6  # Tolerance for convergence
    while True:
        grad = gradient(w, X_trn, y_trn)  # Compute gradient
        z = update_weights(w, eta, grad)  # Update weights
        w_new = HT(z, S)  # Project weights onto feasible set
        t += 1
        
        if convergence(w, w_new, tol):  # Check for convergence
            break
        
        w = w_new  # Update current weights

    return w

