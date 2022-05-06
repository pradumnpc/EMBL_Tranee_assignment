for i in glob.glob("data\*.csv"):
    df = pd.read_csv(i)
    df = df.dropna()
    name = re.search("data\\\(.*)\.csv",str(i))
    name = name.group(1)
    upregulated_gene = df.loc[(df['log2FoldChange']>1) & (df['pvalue']< 0.05),"Unnamed: 0"]
    print("for {} upregulated gene count is = {}".format(name,len(upregulated_gene)))
    down_regulated_gene = df.loc[(df['log2FoldChange']<1) & (df['pvalue']> 0.05),"Unnamed: 0"]
    print("for {} downregulated gene count is = {}".format(name,len(down_regulated_gene)))