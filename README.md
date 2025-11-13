# B210-Assignment_7
# a. What is the purpose of this program(s)?
The purpose of this program is to write a function that sorts the songs by album into lists, then sorts the lists by duration, and writes the results to a new CSV file.
# b. What does the program do, include what it takes for input, and what it gives as output?
The code grouped songs by album from the taylor_discography CSV, sorted each album's tracks by duration (largest first), and wrote a new CSV with the same columns (rows grouped by album).
The input file is taylor_discography.csv and the output file is taylor_by_album_sorted.csv. It also returns the total number of albumns and rows within the sorted file (20,434).
# c. How do you use the program
Create or open the file in VS Code.
Please select all of the code from the python file and copy and paste it into the editor.
Save the file as:
C:\Users\jinas\Downloads\Assignment 7 Lists.py
Run the script in PowerShell:
& C:/Users/jinas/anaconda/python.exe "C:/Users/jinas/Downloads/Assignment 7 Lists.py"
If you previously ran Python by full path, use the same form. Example:
python "C:/Users/jinas/Downloads/Assignment 7 Lists.py"
Expected printed output:
c:\Users\jinas\Downloads\taylor_by_album_sorted.csv (clickable link)
Albums: <N> Total rows: <M>
