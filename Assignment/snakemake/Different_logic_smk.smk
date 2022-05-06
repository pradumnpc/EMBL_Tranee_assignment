data_no = [1,2,3,4,5,6,7,8,9,10]


rule MA_plot:
    input:
        f_name = expand("data/dataset{sample}.",sample=data_no)
    output:
        "result/ma/{input.f_name}.png"
    script:
        "/mnt/c/Python_files/Snakemake_practice/Assignment/src/MA.py"

rule Volcano_plot:
    input:
        f_name = expand("data/dataset{sample}.",sample=data_no)
    output:
        "result/volcano/{input.f_name}.png"
    script:
        "/mnt/c/Python_files/Snakemake_practice/Assignment/src/Volcano.py"