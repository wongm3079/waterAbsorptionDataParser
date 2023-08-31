import pandas as pd
import os
import matplotlib.pyplot as plt
import glob

def main():
    #Defining location of CSVs
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "*.csv"))

    for x in csv_files:
    #read every csv in this folder
        df = pd.read_csv(x, header=None)
    #Deleting everything but datetime + wavelength
        df.drop(df.iloc[:, 212:223], axis=1, inplace=True)
        df.drop(df.iloc[:, 0:13], axis=1, inplace=True)

    #Wavelength values
        df_x = df.iloc[[0]].values.tolist()
    #plotting all data entries for the whole day 
        for i in range(1,len(df.index)):
            df_y = df.iloc[[i]].values.tolist()
            plt.plot(df_x[0], df_y[0]) 
    #Plot properties
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance')
    plt.title('Sandy Creek Wavelength v Absorbance')
    #Show graph
    plt.show()
   
if __name__ == "__main__":
    main()