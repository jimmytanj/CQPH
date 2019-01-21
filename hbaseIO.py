# -*- coding: utf-8 -*-

import happybase
conn = happybase.Connection("192.168.0.201")
pic=open('/home/jianming_tan/Pictures/1.png','rb')
print()
table = happybase.Table("file",conn)
#data={"basic_info:content":pic.read()}
#table.put("1",data)
cell = table.cells("1",'basic_info:content')
print(cell)
#opic=open('/home/jianming_tan/Desktop/1.png','wb')
#opic.write(row['basic_info:content'])
#opic.flush()
#opic.close()