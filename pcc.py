from itertools import product
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
matrix =pd.read_csv('RNASeq expresion.csv', index_col=0)
fh = open('PCC AND PVALUE.txt', 'w')
            
l = matrix.values.tolist()


i=0

while i<=44616:

   x=  l[i]
   y=  l[i+1]
   
   z=pearsonr(x,y)

   print>>fh, z 
   i+=2



