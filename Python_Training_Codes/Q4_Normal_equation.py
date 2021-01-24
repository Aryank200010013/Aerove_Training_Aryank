import numpy as np

x=np.random.normal(0,3.14,size=(20,20))

y=np.arange(20,dtype=np.int32)

y=y.reshape(20,1)

xt=np.matrix.transpose(x)

z=x*xt

zi=np.linalg.inv(z)

z2=zi*xt

z_final=z2.dot(y)

print(z_final)
