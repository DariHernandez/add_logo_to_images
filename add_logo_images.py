#! python3
# Add logo to images folder. 
# Select the position and logo size

import os
from PIL import Image


def add_logo (logo_file, width, height, pos_x, pos_y, imgs_dir):
    """ add logo to folder images"""
    
    # Temporal logo
    temporal_logo_file = os.path.join(os.path.dirname (logo_file), 'temporal' + os.path.basename(logo_file))

    # Make destination dir¿
    destination_dir = imgs_dir + '_with_logo' 
    os.makedirs(destination_dir, exist_ok=True)

    # Loop over all files in the working directory.
    for filename in os.listdir(imgs_dir): 
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') \
            or filename.lower().endswith('.webp') or filename.lower().endswith('.bmp')
            or filename.lower().endswith('.jpeg')):
            continue # skip non-image files and the logo file itself
        im = Image.open( os.path.join (imgs_dir, filename))
        width_img, height_img = im.size

        # change vars
        height_logo = height
        width_logo = width
        pos_x_logo = pos_x
        pos_y_logo = pos_y

        # Calculate width and height
        if str(height_logo).endswith ('%'): 
            height_logo = int(round (height_img * int(height_logo[:-1]) / 100, 0))
        if str(width_logo).endswith ('%'): 
            width_logo = int(round (width_img * int(width_logo[:-1]) / 100))
        
        # Calculate position
        if pos_x_logo == 'right':
            pos_x_logo = width_img - width_logo
        elif pos_x_logo == 'left':
            pos_x_logo = 0
        elif pos_x_logo == 'center':
            pos_x_logo = int( round (width_img / 2 -  width_logo / 2))

        if pos_y_logo == 'up':
            pos_y_logo = 0
        elif pos_y_logo == 'down':
            pos_y_logo = height_img - height_logo
        elif pos_y_logo == 'middle':
            pos_y_logo = int( round ( height_img / 2 - height_logo / 2))
            

        # Make temporal logo     
        im_logo = Image.open(logo_file)
        temporal_logo = im_logo.resize ((width_logo, height_logo))
        temporal_logo.save (temporal_logo_file)

        # Add rresized logo
        print ('Adding logo to %s...' % (os.path.join(destination_dir, filename)))
        # Paste and pass the logoIm for the third argument to paste transparent pixels
        if filename.lower().endswith('.bmp'): 
            logoIm.save(logo_file + '.bmp')
            logoIm = Image.open (logo_file + '.bmp')
            im.paste (logoIm, (pos_x_logo, pos_y_logo))
        else: 
            logoIm = Image.open (temporal_logo_file).convert("RGBA")
            im.paste (logoIm, (pos_x_logo, pos_y_logo), logoIm)
        # Save changes.
        im.save (os.path.join(destination_dir, filename))