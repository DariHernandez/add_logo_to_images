#! python3
# Add logo to images folder. 
# Select the position and logo size
# Using terminal interfaz to request information

import os
from add_logo_images import add_logo

# Information
height = "20%" # Exact number or percentage
width = "110"  # Exact number or percentage
pos_x = 'center'  # Exact number or keywords: 'right', 'left', 'center'
pos_y = 'middle'  # Exact number or keywords: 'up', 'down', 'middle'
logo_file = os.path.join ('logo_path') # Replace logo_path with logo path
imgs_dir = os.path.join ('my_imags_folder') # Replace my_imags_folder with the path of rimages dir

add_logo (logo_file, width, height, pos_x, pos_y, imgs_dir)
