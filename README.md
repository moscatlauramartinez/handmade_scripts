## **plot_sbe_data.R** 

Function: Profiles of all measured variables from a station. It does not consider values of -9.99E-29, which have been considered erroneous during processing.

Input: CSV data from a station. (can be done with to_csv.py)

Output: Profile of each measured variable.

Operation: Input the path of the CSV file and run the script.

## **to_csv.py**

Convert a file outputted by SBE data processing to CSV (comma-separated) format for easy manipulation in both R and Excel.

It's necessary to specify at the end of the file the path of the input file and the path of the output file.

## **to_csv_all_stations.py**

### **ONE STATION**
Converts a file outputted by SBE data processing to CSV (comma-separated) format for easy manipulation in both R and Excel.

It's necessary to specify at the end of the file the path of the input file and the path of the output file.

### **MULTIPLE STATIONS**

Performs the same task as "ONE STATION" but for all files in a folder.

Only provide the input directory and the output directory.

CAUTION: it cannot create folders, it must be run with the output folder already created.


