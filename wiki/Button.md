# NQTR Button

[Button](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/button.py) is a component that is extended by other classes.

## Properties

* `name: Optional[str] = None`
* `label_name: Optional[str] = None`
* `button_icon: Optional[str] = None`
* `button_icon_selected: Optional[str] = None`
* `disabled: Union[bool, str] = False`: ***If is string***: you can put a key of flags ( the sistem get the value of flag). Explained here: [Flags - Ability to edit flags in constants](https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags#ability-to-edit-flags-in-constants)
* `hidden: Union[bool, str] = False`: ***If is string***: you can put a key of flags ( the sistem get the value of flag). Explained here: [Flags - Ability to edit flags in constants](https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags#ability-to-edit-flags-in-constants)
* `default_label_name: Optional[str] = None`: used only by the system

### Picture in Background

Most classes that extend [NQTR Button](Button) have the ability to be used as a [Picture in Background](#picture-in-background)

This option allows you to add an image with the button function to a specific location.
This is very useful for adding elements in the room that you want to interact with. (For example: TV, character, doors...)

To use this option just give a value to picture_in_background instead of button_icon.  
In case both are valued you will see both the button in the "button list" and in the x, y position of your choice.

The following properties are used only for  [Picture in Background](#picture-in-background):

* `picture_in_background: Optional[str] = None`: [idle image](https://www.renpy.org/doc/html/screens.html#screen-property-idle)
* `picture_in_background_selected: Optional[str] = None`: [hover/selected image](https://www.renpy.org/doc/html/screens.html#screen-property-hover)
* `xalign: Optional[Union[int, float]] = None`
* `yalign: Optional[Union[int, float]] = None`

## Make a background area a button

If you don't want to add an image in the background, but want to click on a certain area of the image, you can use the following trick.

You need to have the following images:
* background
* "area" of the button
* (optional) hover image

exemple:

![bedroom_mc0](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/d90fa551-7339-46c3-a207-d0ff59dc3f8e)
![tv](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/4acff9f2-3191-4533-bd8f-1b61502a8a88)
![tv0](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/e257f669-a07d-49a1-b46a-41334fbfcb26)

make the button image almost totally transparent:
```renpy
image action bedroom_mc tv:
    "enviroment_mc_home/bedroom_mc/button/tv.webp"
    alpha 0.01
image action bedroom_mc tv selected = "enviroment_mc_home/bedroom_mc/tv.webp"
```

So:

```py
Act(name = _("TV"), picture_in_background = "action bedroom_mc tv", picture_in_background_selected = "action bedroom_mc tv selected", label_name = "watching_tv"),
```
