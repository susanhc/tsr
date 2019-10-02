import os
import cv2
import csv
import math

#print(math.floor(3.2))
#print(math.ceil(3.2))



def crop(filepath,labelpath):
	pathdir=os.listdir(filepath)
	for alldir in pathdir:
		child=os.path.join(filepath,alldir)
		#dest=os.path.join(destpath,alldir)
		if os.path.isfile(child):
			image=cv2.imread(child)
			sp=image.shape
			sz1=int(sp[1])# width-x
			sz2=int(sp[0])# height-y

			#with open('./alter.csv','r') as f:
			with open("/home/hc/eriklindernoren/tiny-yolov3-master/train2.csv",'r') as f:
				lines=csv.reader(f)
				for line in lines:
					name=line[0].split(' ')[0]
					if name==alldir:
						na=name.strip('.jpg')+'.txt'
						path=labelpath+na
						nomalized2(path,line,sz1,sz2)

						'''
						w,name,x1,y1,x2,y2,x3,y3,x4,y4,x_cen,y_cen,cla=center(line)
						a,b,c,d=right_crop(x1,y1,x2,y4)
						x1=x1-a
						y1=y1-c
						x2=x3-a
						y2=y3-c
						x_cen=round(((x2-x1)/2+x1)/416,6)
						y_cen=round(((y2-y1)/2+y1)/416,6)
						width=round((x2-x1)/416,6)
						height=round((y2-y1)/416,6)
						#with open('./4.txt','a') as f:
							#f.write('%s %s %s %s %s\n'%(name,x_cen,y_cen,width,height))
						na=name.split('.')[0]+'.txt'
						na='/data2/ggp/MNist/flower/DF/label/test/%s'%(na)
						na='/home/hc/eriklindernoren/data/demo/label/test/%s'%(na)
						write_label(na,x_cen,y_cen,width,height,cla)

						#cropImg=image[c:d,a:b]
						#cv2.imwrite(dest,cropImg)'''

def right_crop(x1,y1,x2,y4):
	if x1<3200-x2:
		a=math.floor(4/5*(x1))
		b=a+416
	else:
		b=math.floor(3200-4/5*(3200-x2))
		a=b-416
	if y1<1800-y4:
		c=math.floor(4/5*(y1))
		d=c+416
	else:
		d=math.floor(1800-4/5*(1800-y4))
		c=d-416
	return a,b,c,d



def write_label(na,x_cen,y_cen,width,height,cla):
	with open(na,'w') as f:
		f.write('%s %s %s %s %s'%(cla,x_cen,y_cen,width,height))
		f.write('\n')
		f.close()


def center(line):
	name=line[0]
	x1=int(line[1])
	y1=int(line[2])
	x2=int(line[3])
	y2=int(line[4])
	x3=int(line[5])
	y3=int(line[6])
	x4=int(line[7])
	y4=int(line[8])
	cla=line[9]
	w=x2-x1
	x_cen=(x2-x1)/2+x1 
	y_cen=(y3-y2)/2+y2
	return w,name,x1,y1,x2,y2,x3,y3,x4,y4,x_cen,y_cen,cla

def nomalized(path,line):
	f=open(path,'w+')
	name=line[0]
	x1=int(line[1])
	y1=int(line[2])
	x2=int(line[3])
	y2=int(line[4])
	x3=int(line[5])
	y3=int(line[6])
	x4=int(line[7])
	y4=int(line[8])
	cla=line[9]
	x=round(((x2-x1)/2+x1)/3200,6)
	y=round(((y3-y2)/2+y2)/1800,6)
	w=round((x2-x1)/3200,6)
	h=round((y3-y2)/1800,6)
	f.write('%s %f %f %f %f\n'%(cla,x,y,w,h))

def nomalized2(path,line,sz1,sz2):
	f=open(path,'w+')
	name=line[0].split(' ')[0]
	x1=int(line[0].split(' ')[1])
	y1=int(line[1])
	x2=int(line[2])
	y2=int(line[3])

	cla=line[4]
	x=round(((x2-x1)/2+x1)/sz1,6)
	y=round(((y2-y1)/2+y1)/sz2,6)
	w=round((x2-x1)/sz1,6)
	h=round((y2-y1)/sz2,6)
	f.write('%s %f %f %f %f\n'%(cla,x,y,w,h))







if __name__ == "__main__":
	path='/data2/ggp/MNist/flower/DF/'
	#crop('./images/test','./train')
	#crop(path+'images/test/',path+'labels/test/')
	#crop('/data2/flower/DF/Test_fix','/data2/flower/DF/images/test')
	crop("/home/hc/eriklindernoren/tiny-yolov3-master/test/","/data2/ggp/MNist/flower/tanke/labels/test2/")