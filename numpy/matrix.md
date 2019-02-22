{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]] * [[1 2]\n",
      " [3 4]\n",
      " [5 6]] = [[22 28]\n",
      " [49 64]]\n"
     ]
    }
   ],
   "source": [
    "# matrix 线性代数\n",
    "\n",
    "import numpy as np\n",
    "X=np.array([[1,2,3],[4,5,6]])\n",
    "Y=np.array([[1,2],[3,4],[5,6]])\n",
    "\n",
    "# 乘\n",
    "print(\"X*Y=\",X,Y,\"=\",X.dot(Y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1., 1., 1.])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.ones(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.25427166  1.05310393  0.20343896  0.56710681]\n",
      " [ 0.01145377 -0.3856959   0.49488124  0.95896147]\n",
      " [-0.8356794  -0.10296023  1.72081078 -0.36213806]\n",
      " [ 1.93160704  0.63517308 -0.47585336 -0.05153049]]\n",
      "[[ 0.25427166  0.01145377 -0.8356794   1.93160704]\n",
      " [ 1.05310393 -0.3856959  -0.10296023  0.63517308]\n",
      " [ 0.20343896  0.49488124  1.72081078 -0.47585336]\n",
      " [ 0.56710681  0.95896147 -0.36213806 -0.05153049]]\n",
      "[[ 4.49425109  1.57630336 -2.29981079  0.35827756]\n",
      " [ 1.57630336  1.67183487 -0.45605562  0.23190993]\n",
      " [-2.29981079 -0.45605562  3.473921   -0.00870646]\n",
      " [ 0.35827756  0.23190993 -0.00870646  1.3750166 ]]\n",
      "inv是矩阵求逆 [[ 0.51475532 -0.39761529  0.2884168  -0.06523795]\n",
      " [-0.39761529  0.94276548 -0.13960493 -0.05628696]\n",
      " [ 0.2884168  -0.13960493  0.46034798 -0.04868995]\n",
      " [-0.06523795 -0.05628696 -0.04868995  0.75344754]]\n",
      "QR分解 [[-0.8478132   0.1369992  -0.50504856 -0.08584846]\n",
      " [-0.29736006 -0.91464553  0.26365553 -0.07406961]\n",
      " [ 0.43384535 -0.37172075 -0.81822773 -0.06407249]\n",
      " [-0.06758689 -0.08048886 -0.07690971  0.99148296]] \n",
      " [[-5.30099213 -2.04707939  3.59315558 -0.46942355]\n",
      " [ 0.         -1.16232483 -1.18857073 -0.2704688 ]\n",
      " [ 0.          0.         -1.80051434 -0.21843149]\n",
      " [ 0.          0.          0.          1.31592832]]\n"
     ]
    }
   ],
   "source": [
    "from numpy.linalg import inv,qr\n",
    "import numpy.random\n",
    "X=numpy.random.randn(4,4)\n",
    "print(X)\n",
    "print(X.T)\n",
    "print(X.T.dot(X))\n",
    "print(\"inv是矩阵求逆\",inv(X.T.dot(X)))\n",
    "q,r=qr(X.T.dot(X))\n",
    "print(\"QR分解\",q,\"\\n\",r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
