#This code generates Pearson correlation coefficient (PCC) and p-value from expression data. 
#An example is shown with RNASeq expression data for cis miPs and their targets (which are shown in alternative rows in the csv file.
from itertools import product
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
matrix1  =pd.read_csv('Cis miPs_RNASeq expression.csv')
matrix2  =pd.read_csv('Cis miPs_RNASeq expression.csv', index_col=0)

fh = open('miPs_PCC.txt', 'w')          
print ("miPs\tTarget\tPCC\tp-val", file=fh)

l = matrix2.values.tolist()


i=0

while i<len(l)-1:


   x=  l[i]   
   y=  l[i+1]   
   z=pearsonr(x,y)  
   print(matrix1["Locus id"][i],matrix1["Locus id"][i+1],z[0], z[1],sep="\t", file=fh) 
   
   i+=2
