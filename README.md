# Succulent-Generator
Generating fake succulent images using ProGAN.

[Generative adversarial network](https://en.wikipedia.org/wiki/Generative_adversarial_network)

## Usage
The pre-trained models are `generator.pth` and `critic.pth` in the [google drive](https://drive.google.com/drive/folders/1qxup4DrslHZfO0LAHTRfEU3fyHNPG8v5?usp=sharing), to generating fake images simply run 

> python3 train.py
  
It will generate 100 fake succulents images with size 512x512 inside the `saved_examples` folder.

If you wish to train your own model using your own dataset, you will need to have cuda downloaded in your machine and pytorch setup etc. Then in the [config.py](https://github.com/Ifan24/Succulent-Generator/blob/main/config.py), change the *dataset* to the path of your dataset and adjusting the hyperparameters based on your VRAM. If you wise to load or not load existing model, set *LOAD_MODEL* to True or False.

## Generated Images
fake images
![fake image](fake.jpg)

***

real images
![real images](real.jpg)


check the [google drive](https://drive.google.com/drive/folders/1qxup4DrslHZfO0LAHTRfEU3fyHNPG8v5?usp=sharing) for more examples

## Potential improvements
1. The quality of the images can definitely be improved by training more epochs, one epoch for training the model on 512x512 images takes about ~2hr in google colab. 
2. The dataset I gether has about 9000 images, I believed if more good images are added the quality can also be improved, and some of the images in the dataset are not very suitable to be included as the size of original images are more than 2000x2000 and center crop it to 512x512 makes it looks less like a succulent. Additionally, the shape of different succulents vary a lot, I think it might result in generating more strange images, it might be better to have all the images to have some common features.
3. Maybe ProGAN is not the best model for generating plant, seek other options like autoencoder or diffusion based network
4. Automated the process of collecting data, use a scraper to collect the images and then process the images using an image classifier or something

## Credit
Implementing the ProGAN based on this video

<a href="https://www.youtube.com/watch?v=nkQHASviYac
" target="_blank"><img src="https://img.youtube.com/vi/nkQHASviYac/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

The succulents images I used in this project are mostly downloaded from shopping website, since most open source datasets I found for succulent are either has blurring images or just too small for this project.

The raw images are ranges from 800x800 to 2400x2400, torchvision is used to center crop the image to 512x512.
Then I manually deleted some images from the dataset that are either too close to the camera or lose some features of succulent due to cropping.
