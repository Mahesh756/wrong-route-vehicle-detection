
import glob
import cv2
import torch
from matplotlib import pyplot as plt  
import numpy as np 
import imutils
import easyocr
import os
import mysql.connector
import smtplib
from mypro import *

def check(img):
	try:
		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))
		bfilter=cv2.bilateralFilter(gray,11,17,17)
		edged=cv2.Canny(bfilter,30,200)
		plt.imshow(cv2.cvtColor(edged,cv2.COLOR_BGR2RGB))
		keypoints=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		contours=imutils.grab_contours(keypoints)
		contours=sorted(contours,key=cv2.contourArea,reverse=True)[:10]
		location=None
		for contour in contours:
			approx=cv2.approxPolyDP(contour,10,True)
			if(len(approx)==4):
				location=approx
				break
		mask=np.zeros(gray.shape,np.uint8)
		new_image=cv2.drawContours(mask,[location],0,255,-1)
		new_image=cv2.bitwise_and(img,img,mask=mask)
		plt.imshow(cv2.cvtColor(new_image,cv2.COLOR_BGR2RGB))
		(x,y)=np.where(mask==255)
		(x1,y1)=(np.min(x),np.min(y))
		(x2,y2)=(np.max(x),np.max(y))                                                                     
		cropped_image=gray[x1:x2+1,y1:y2+1]
		plt.imshow(cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB))
		reader=easyocr.Reader(['en'])
		result=reader.readtext(cropped_image)
		text=result[0][-2]
		font=cv2.FONT_HERSHEY_SIMPLEX
		res=cv2.putText(img,text=text,org=(approx[0][0][0],approx[1][0][1]+60),fontFace=font,fontScale=1,color=(0,255,0),thickness=2,lineType=cv2.LINE_AA)
		res=cv2.rectangle(img,tuple(approx[0][0]),tuple(approx[2][0]),(0,255,0),3)
		plt.imshow(cv2.cvtColor(res,cv2.COLOR_BGR2RGB))
		os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
		return text
	except:
		return None



plates = []
s=set()
for img in glob.glob("C:/Users/gayat/sub_final1/*.jpg"):
    n= cv2.imread(img)
    p=check(n)
    if p!=None:
    	l=[]
    	#s=set()
    	if(len(p)==8 and p not in s):
    		l.append(p)
    		print("recougnized number plate is :",p)
    		l.append("geethahainith@gmail.com")
    		s.add(p)
    		plates.append(l)

# print(plates)

print("extracting information using that vehicle number..!")
mydb=mysql.connector.connect(host="localhost",user="karthik",passwd="Karthik123@",database="vehicledb")
mycursor=mydb.cursor()
# -------------
#mycursor.execute("CREATE DATABASE vehicledb")
#mycursor.execute("SHOW DATABASES")
#print('Databases are : ')
#for db in mycursor:
    #print(db)

#mycursor.execute("create table vinfo(vno varchar(255))")
#mycursor.execute("show tables")
#for tb in mycursor:
    #print(tb)
#mycursor.execute("alter table vinfo add email varchar(100)")
#mydb.commit()
# ----------
sqlformula = "insert into vinfo(vno,email) values(%s,%s)"
mycursor.executemany(sqlformula,plates)
#mycursor.execute("select * from vinfo")
mydb.commit()
#mycursor.execute("alter table vinfo drop column def")
#mycursor.execute("truncate table vinfo")
#mydb.commit()
mycursor.execute("select email from vinfo")

#to send message to particular email
for c in mycursor:
	v1=str(c[0])
	s=smtplib.SMTP_SSL("smtp.gmail.com",465)
	s.login("gskarthik2000@gmail.com","sankar2000karthik")
	s.sendmail("gskarthik2000@gmail.com",v1,"you are violating the traffic rules drive carefully  You are fined with 300rs")
	print("warning message sent successfully to respected email")
	s.quit()
	break


