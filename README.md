# add_logo_to_images
## Description
Add logo to all images in specific folder.

You can indicate the size and position of the logo. 

## Install modules
``` bash
$ pip install Pillow
```


**Formats sorported: .png, .jpg .webp .bmp .jpeg***
## How to use
The main.py file, have the parameters to run the program. Modify this script. 

* **height:** Exact number of pixels (like 500) or percentage (like '10%')
* **width:** Exact number of pixels (like 500) or percentage (like '10%')
* **pos_x:** Exact position (like 250) or keywords: 'right', 'left', 'center'
* **pos_y:** Exact position (like 250) or keywords: 'up', 'down', 'middle'
* **logo_file:** Replace logo_path with logo path
* **imgs_dir:** the path of rimages dir

## Use example
```python
height = "20%" 
width = "20%" 
pos_x = 'right' 
pos_y = 'down'  
logo_file = '/home/my_user/Documentos/logo.png' 
imgs_dir = '/home/my_user/Documentos/my_images'

add_logo (logo_file, width, height, pos_x, pos_y, imgs_dir)
```

## Screenshots
### Logo
!(logo)[]
### Original files
!(img1)[]
!(img2)[]
!(img3)[]
!(img4)[]
### result files
!(img1_logo)[]
!(img2_logo)[]
!(img3_logo)[]
!(img4_logo)[]
