input=""" """

list = []
for i in input.split("\n"):
    list.append(i.split("\t"))

for i in list:
    print("||".join(i)[:-2])

#Made by LongTo
#Xuất Từ điển của GBoard
#Giải nén
#Copy toàn bộ
#Chạy chương trình Python này và paste vào
#Copy kết quả (ghi thêm 2 kí tự vào từ cuối tại file chạy bị sót :)) và Paste vào file mẫu từ điển của EVKey (Xuất Dictionary của EVKey là có file mẫu nha)
#Reload từ điển EVKey
