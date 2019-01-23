# -*- coding: utf-8 -*-

import happybase
import time
stime=time.time()
conn = happybase.Connection("192.168.0.201")
pic=open('/home/jianming_tan/Pictures/其余征订.tar.gz','rb')
table = happybase.Table("file",conn)
data={"basic_info:content":pic.read()}
table.put("2",data)

#cell = table.cells("1",'basic_info:content')
#print(cell)
#opic=open('/home/jianming_tan/Desktop/1.png','wb')
#opic.write(row['basic_info:content'])
#opic.flush()
#opic.close()
etime=time.time()
print("一共消耗时间%d"%(etime-stime))