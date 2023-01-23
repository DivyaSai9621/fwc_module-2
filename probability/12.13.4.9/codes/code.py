import matplotlib.pyplot as plt

def probabilities():
    k = 1/(1+2+3)
    P_X_less_2 = k + 2 * k # P(X < 2) = P(X = 0) + P(X = 1)
    P_X_less_equal_2 = k + 2 * k + 3 * k # P(X <= 2) = P(X = 0) + P(X = 1) + P(X = 2)
    P_X_greater_equal_2 = 3 * k # P(X >= 2) = P(X = 2)
    return k, P_X_less_2, P_X_less_equal_2, P_X_greater_equal_2

k, P_X_less_2, P_X_less_equal_2, P_X_greater_equal_2 = probabilities()
print(k) 
print(P_X_less_2) 
print(P_X_less_equal_2) 
print(P_X_greater_equal_2) 

#Plotting the results
x = [0, 1, 2]
y = [k, 2*k, 3*k]

plt.stem(x, y,markerfmt='o')
plt.xlabel('x')
plt.ylabel('P(X)')
plt.title('Probability Distribution of X')
plt.savefig('/home/divya/fwc-2/probability/12.13.4.9/codes/fig.pdf')
plt.show()


