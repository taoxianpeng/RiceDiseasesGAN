from PIL import Image
import matplotlib.pyplot as plt
from random import random
import numpy as np
import os

def imageRandomCrop(image):
    image_w = image.size[0] #原始图像的宽度
    image_h = image.size[1] #原始图像的高度
    w = 224 #剪裁后图像的宽度
    h = 224 #剪裁后图像的高度
    b1 = int(random()*(image_w - w)) #剪裁的宽度起始点
    b2 = b1+w #剪裁的宽度终结点
    a1 = int(random()*(image_h - h))
    a2 = a1+h

    return image.crop([b1,a1,b2,a2])
def saveImage(image,name,dirname):
    try:
        os.makedirs(dirname)
    except Exception as e:
        pass

    try:
        path='./'+dirname
        image.save(path+'/'+name+'.jpg')    
    except Exception as e:
        print(e)
if __name__ == "__main__":
    root_path = './rice_leaf_diseases/'
    blb_path = root_path+'Bacterial leaf blight'
    bs_path = root_path+'Brown spot'
    ls_path = root_path+'Leaf smut'
    for path in (blb_path,bs_path,ls_path):
        for root,dirs,files in os.walk(path):
            # print(files)
            for file in files:
                # print(root.findall('/'))
                # print(root.insert(root.find('/'),)+'/'+file)
                im  = Image.open(root+'/'+file)
                r = imageRandomCrop(im)
                for i in range(100):
                    r = imageRandomCrop(im)
                    saveImage(r,'image-{}'.format(i),'./imageCrop/'+root[2:]+'/'+file)
                    print('完成 : {} {}'.format('./imageCrop/'+root[2:]+'/'+file, 'image-{}'.format(i)))
    