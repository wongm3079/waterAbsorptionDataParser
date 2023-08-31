import pandas as pd
import xlsxwriter 

def addRowToX1s(self, data, row = 0):
    for colNum, value in enumerate(data):
        self.write(row, colNum, value)

def main():
    xlsxwriter.worksheet.Worksheet.addRow = addRowToX1s
    wbook = xlsxwriter.Workbook("reformat.xlsx")
    worksheet = wbook.add_worksheet()
    
    # 'r+' = reading and writing, 
    # 't' = text and not binary i.e. images
    with open('ABSORPTI.CSV', 'rt+') as Absorb_raw:  
        lines = Absorb_raw.readlines
    #If no headers are needed, rowsave = 0
        rowsave = 0
        for line in lines():
            worksheet.addRow(data = line.split(";"), row = rowsave)
            rowsave+=1

    wbook.close()

    reformat = pd.read_excel("reformat.xlsx")
    reformat.to_csv("reformat_20221113.CSV", index=None, header=True)


if __name__ == "__main__":
    main()


#No 20191105 - OPUS
#No 20191126 - OPUS
#No 20191202 - OPUS
#No 20191209 - OPUS
#20201227 missing values lab
#No 2021 OPUS data


    

