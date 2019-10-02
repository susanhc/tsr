import os





def make_path(trainpath,txtname):
	

	imgpath=os.listdir(trainpath)
	for img in imgpath:
		txtpath=path+txtname
		with open(txtpath,'a') as f:
			f.write(trainpath+'%s\n'%(img))
path='/data2/ggp/MNist/flower/tanke/images/'
#path='/home/hc/eriklindernoren/data/demo/images/'
make_path(path+'train/','trainvalno5k3.txt')
make_path(path+'test/','5k3.txt')
