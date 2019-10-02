import os
import cv2
import csv
import math
import random
import shutil


def move(filepath,destpath):
	pathdir=os.listdir(filepath)
	ranpath=random.sample(pathdir,int(0.1*len(pathdir)))
	print(ranpath)
	for alldir in ranpath:
		child=os.path.join(filepath,alldir)
		dest=os.path.join(destpath,alldir)
		shutil.copy(child,dest)
		os.remove(child)



def move_label(imgpath,labelpath,testpath):
	imgs=os.listdir(imgpath)
	for img in imgs:
		with open(labelpath,'r') as f:
			lines=f.readlines()
			for line in lines:
				name=line.strip('\n').split(',')[0]
				if name==img:
					with open(testpath,'a') as f:
						f.write(line)

def move_img(labelpath,imgpath,testpath):
	labels=os.listdir(labelpath)
	for label in labels:
		imgdir=os.listdir(imgpath)
		for img in imgdir:
			if label.strip('.txt')==img.strip('.jpg'):
				img_path=os.path.join(imgpath,img)
				test_path=os.path.join(testpath,img)
				shutil.copy(img_path,test_path)
				#os.remove(img_path)

				
if __name__ == "__main__":
	#move('/data2/ggp/MNist/flower/DF/images/train','/data2/ggp/MNist/flower/DF/images/test')
	#move('./train','./test')
	#move_label('/data2/ggp/MNist/flower/DF/tsr_test/images','/data2/ggp/MNist/flower/DF/train_20to0.csv','/data2/ggp/MNist/flower/DF/test.txt')
	#move_img("/data2/ggp/MNist/flower/DF/labels/train/",'/data2/ggp/MNist/flower/DF/Train_fix/','/data2/ggp/MNist/flower/DF/train/')
	move("/data2/ggp/MNist/flower/tanke/images/train","/data2/ggp/MNist/flower/tanke/images/test")