import matplotlib.pyplot as plt

txt_file_open = open(r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\data_real.txt', 'r')
txt_file_list = txt_file_open.readlines()
txt_file_list_len = len(txt_file_list)
#print(txt_file_list_len)
#print(txt_file_list)



#take the first group of data
raw_list = txt_file_list[2][1:-2].split(', ')
data_list = raw_list[1:]
data_list_len = len(data_list)

time_list = []
temp_list = []
for j in range(1, int(data_list_len / 2)):
    time_list.append(data_list[j * 2 - 2])
    temp_list.append(data_list[j * 2 - 1])

plt.plot(time_list, temp_list, 'ro')
plt.show()






