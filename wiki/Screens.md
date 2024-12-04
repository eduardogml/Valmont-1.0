# Screens

NQTR gives the recommended screens, but you can use your own screens.

## Character Info button

You can see a Character Info button in a test project, but it is not implemented in NQTR.
This button call the label `open_characters_info` if exist.

So you can create your own screen or I reccomand to use [DS-toolkit](https://github.com/DRincs-Productions/DS-toolkit).

exemple to connect the button to the DS screen:

```renpy
label open_characters_info:
    call screen menu_userinfo
```

## Inventory button

You can see an Inventory button in a test project, but it is not implemented in NQTR.
This button call the label `open_inventory` if exist.

So you can create your own screen.

## Smartphone button

You can see a Smartphone button in a test project, but it is not implemented in NQTR.
This button call the label `open_smartphone` if exist.

So you can create your own screen.

## Recommended icon pack

* [Detailed Straight Lineal color](https://www.freepik.com/author/freepik/icons/detailed-straight-lineal-color_12?t=f)
* [Basic Rounded Flat](https://www.freepik.com/author/freepik/icons/basic-rounded-flat_6?t=f#from_element=resource_detail)
* [svg repo](https://www.svgrepo.com/)

## Edit icons

* Add `nqtr_menu_icon_options` image in your game folder and edit Options button.
* Add `nqtr_menu_icon_characters_info` image in your game folder and edit Character Info button.
* Add `nqtr_menu_memo` image in your game folder and edit Quest memo button.
* Add `nqtr_menu_icon_help` image in your game folder and edit Help button.
* Add `nqtr_menu_icon_inventory` image in your game folder and edit Inventory button.
* Add `nqtr_menu_icon_phone` image in your game folder and edit Smartphone button.
* Add `nqtr_menu_icon_map` image in your game folder and edit Map button.
* Add `nqtr_menu_icon_wait` image in your game folder and edit Wait button.
* Add `nqtr_menu_icon_talk` image in your game folder and edit Talk button.

## Room Button

Into the exemple project, I use a room button [Ren'Py Layered Image Masks by Feniks](https://feniksdev.com/how-to-mask-images-in-renpy) to create a room button.
The [Ren'Py Layered Image Masks by Feniks](https://feniksdev.com/how-to-mask-images-in-renpy) resize a image into a image mask.

exemple:

```renpy
image pre action alarm = Transform("/nqtr_interface/alarm.webp", xysize=(gui.sprite_size, gui.sprite_size))
image action alarm = LayeredImageMask("pre action alarm",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
```

But if you use large images and/or there are many rooms in one place, this can create major slowdowns.
So in this case I recommend you create button images by hand.
