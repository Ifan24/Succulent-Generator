import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader

transform = transforms.Compose([
    # transforms.Resize((1024, 1024)),
    transforms.CenterCrop((512, 512)),
    transforms.ToTensor(),
    ])
    
dataset = datasets.ImageFolder(root='succulents_raw', transform=transform)

num_img = 0
for img, label in dataset:
    save_image(img, 'succulents/img'+str(num_img)+'.png')
    num_img += 1