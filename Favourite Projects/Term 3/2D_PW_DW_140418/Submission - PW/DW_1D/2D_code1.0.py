#Installed dependencies: pandas, xlrd
#import pandas as pd

#For pandas to open and print an excel file
#file_read = pd.ExcelFile(r"C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\temp_51.xlsx")

#sheet_1 = pd.read_excel(r"C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\temp_51.xlsx",sheet_name=0)


#For python to convert txt file into pandas
txt_file_open = open(r'/home/pi/Desktop/2D_Group8_PWandDW/test.txt', 'r')
txt_file_list = txt_file_open.readlines()
print(txt_file_list)
print(len(txt_file_list))



