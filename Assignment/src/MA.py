import pandas as pd 
import glob
from bioinfokit import analys, visuz
import re 

mapath = "C:\Python_files\Snakemake_practice\Assignment\results\MA"
# C:\Python_files\Snakemake_practice\Assignment\data
# C:\Python_files\Snakemake_practice\Assignment\results\MA
for i in glob.glob("C:\Python_files\Snakemake_practice\Assignment\data\*.csv"):
    name = re.search("data\\\(.*)\.csv",str(i))
    print(i)
    name = name.group(1)
    df = pd.read_csv(i)
    df.head()
    df = df.dropna()
    visuz.GeneExpression.ma(df=df, lfc='log2FoldChange', ct_count='lfcSE', st_count='lfcSE', pv='pvalue',plotlegend=True,figname=r'C:\\Python_files\\Snakemake_practice\\Assignment\\results\\MA\\'+name)