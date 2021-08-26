import re
import requests
import csv
s=set()
try:
    # file_path=input("enter complete file path and replace '\' with '/' : ")
    f=open("d://work.csv","r")
    z=[]
    
    def Csv_file_reader():
        reader=csv.reader(f)
        field= next(reader)
        for i in reader:
                email_finder(i[0])
        f.close()

    def email_finder(i):
        s=set()
        url=i
        Email_Regex=r"[\w\.-]+@[\w\.-]+"
        r=requests.get(url)
        for re_match in re.findall(Email_Regex, r.text):
            s.add(re_match)
        csv_file_writer(list(s)+[" "])

    def csv_file_writer(s):
        print(s)
        f=open("d://result.csv","a")
        writer=csv.writer(f)
        writer.writerow(s)
        f.close()
    Csv_file_reader()

except EOFError:
    pass