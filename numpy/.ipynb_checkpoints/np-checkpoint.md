{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(9,)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# ndarray的shape 和 dtype\n",
    "import numpy as np\n",
    "\n",
    "data1=[84,23,5,6,3,5,3,5,3]\n",
    "data2=[834,235,15,36,35,51,3,54,3]\n",
    "nda1=np.array(data1)\n",
    "\n",
    "nda1.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 按距离 随机生成\n",
    "r1=np.arange(20,dtype=np.int64)\n",
    "r1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1.00000000e+00, -9.00000000e-01, -8.00000000e-01, -7.00000000e-01,\n",
       "       -6.00000000e-01, -5.00000000e-01, -4.00000000e-01, -3.00000000e-01,\n",
       "       -2.00000000e-01, -1.00000000e-01, -2.22044605e-16,  1.00000000e-01,\n",
       "        2.00000000e-01,  3.00000000e-01,  4.00000000e-01,  5.00000000e-01,\n",
       "        6.00000000e-01,  7.00000000e-01,  8.00000000e-01,  9.00000000e-01])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "points=np.arange(-1,1,0.1)\n",
    "points"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 0, 0, 0],\n",
       "       [0, 1, 0, 0],\n",
       "       [0, 0, 1, 0],\n",
       "       [0, 0, 0, 1]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.eye(4,dtype=np.int64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.87342678, -1.03638483,  1.84730181,  0.31133215],\n",
       "       [ 0.30577882, -0.90293428,  0.79430347, -0.48578177],\n",
       "       [ 0.22830689,  0.86612594,  0.07503103,  0.28941002],\n",
       "       [ 1.2285727 , -0.07357942,  0.18062972,  0.23526329]])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r2=np.random.randn(4,4)\n",
    "r2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([11, 12, 13, 14, 15, 16, 17, 18, 19])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 过滤 索引\n",
    "r1[r1>10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# where 过滤\n",
    "ndaifa=np.array(['a','b','c','d','e'])\n",
    "ndaifb=np.array(['A','B','C','D','E'])\n",
    "ndaif=np.array([True,False,False,True,True])\n",
    "nadif_result=np.where(ndaif,ndaifa,ndaifb)\n",
    "nadif_result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 元素级数组函数\n",
    "\n",
    "numpy.square(r1)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 从一个坐标向量中返回一个坐标矩阵\n",
    "x,y=np.meshgrid(points,points)\n",
    "x"
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
