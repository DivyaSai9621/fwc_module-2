import numpy as np
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

x=np.arange(0,3)
y=[0.166,0.33,0.5]
cdf=np.cumsum(y)

plt.stem(x,y,label="PMF")
plt.plot(x,cdf,marker="o",label="CDF",color="red")
plt.xlim(0,7)
plt.ylim(0,1.5)
plt.xlabel("X")
plt.ylabel("Probability Values")
plt.title("CDF for discrete distribution")
plt.legend()
plt.savefig('/home/divya/fwc-2/probability/12.13.4.9/codes/fig.pdf')
plt.show()


