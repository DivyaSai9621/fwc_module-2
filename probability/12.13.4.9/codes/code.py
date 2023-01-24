import numpy as np
import matplotlib.pyplot as plt 
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


