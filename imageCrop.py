import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader

import numpy as np
import glob
from PIL import Image
import matplotlib.pyplot as plt

def center_crop(img_path, key):        
    im = Image.open(img_path)
    width, height = im.size
    
    if height != width:
        new_size = min(height, width)
        left = (width - new_size)/2
        top = (height - new_size)/2
        right = (width + new_size)/2
        bottom = (height + new_size)/2
        cropped_img = im.crop((left, top, right, bottom))
        cropped_img.save("succulents_raw/train/tmp/img"+str(key)+'.png')
    else:
        im.save("succulents_raw/train/tmp/img"+str(key)+'.png')

for (i,image_file) in enumerate(glob.iglob('succulents_shape/*/*/*.jpg')):
        center_crop(image_file, i)
        
        
transform = transforms.Compose([
    transforms.Resize((512, 512)),
    transforms.ToTensor(),
    ])
    
dataset = datasets.ImageFolder(root='succulents_raw', transform=transform)

num_img = 0
for img, label in dataset:
    save_image(img, 'succulents/img'+str(num_img)+'.png')
    num_img += 1