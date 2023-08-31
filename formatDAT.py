import pandas as pd

def main():
    # Get the data from the text and put it into a list
    with open('ABSORPTI.DAT', 'r') as f:
        input_data = f.readlines()
    
    # the list that contains the entire absorption.txt file
    absorption_raw = []
    for i in input_data:
        absorption_raw.append(i)

    absorption = []
    
    # Just to get the wavelengths into the first row of the 2D Array
    for i in range(len(absorption_raw)):
        if (absorption_raw[i] == "[DATA]\n"):
            dummy = []
            dummy.append("DateTime")
            i += 2
            while(absorption_raw[i] != "[END] of [DATA]\n"):
                currentLine = absorption_raw[i].split()
                dummy.append(currentLine[0])
                i+=1
            absorption.append(dummy)
            break
    
    # Inputting all the data entries into the 2D array
    for i in range(len(absorption_raw)):
        if ("DateTime" in absorption_raw[i]):
            dummy = []
            dateTime = absorption_raw[i].split()
            dummy.append(dateTime[2] + " " + dateTime[3])
        if (absorption_raw[i] == "[DATA]\n"):
            i += 2
            while(absorption_raw[i] != "[END] of [DATA]\n"):
                currentLine = absorption_raw[i].split()
                dummy.append(currentLine[1])
                i+=1
            absorption.append(dummy)
    
    df=pd.DataFrame(absorption)
    print(absorption)
    df.to_csv("20190101.CSV",index=0, header=False)
    
if __name__ == "__main__":
    main()
    