
import pdfplumber
import pandas as pd

with pdfplumber.open('北京大学信息科学技术学院2018年硕士.pdf') as pdf:
    master = [[]]
    for i in range(3):
        page = pdf.pages[i]
        table = page.extract_tables()[0]
        master += table

    df1 = pd.DataFrame(master[1:])


with pd.ExcelWriter('北京大学信息科学技术学院2018年硕士.xlsx') as writer:
    df1.to_excel(writer, sheet_name='master')
