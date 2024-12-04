#here are the styles and transforms used in both the replay and gallery screens 

transform imageThumb: #images to thumbnail re-sizer
    #size(384, 216) #for 1024 x 768 screens
    size(600, 338) #for 1920 x 1080 screen

style gallery_button: # hover overlay it must be 4 pixels bigger then the images
    #hover_foreground "images/gallery/hover 1280x724.png" 
    hover_foreground "images/gallery/hover 1924x1084.png" 

style name_text: #text color and outlines
    color "#ffffff"
    outlines [ (1, "#000000", 0, 0) ]

#the locked image for the galleries 
image locked = "images/lock.jpg"
