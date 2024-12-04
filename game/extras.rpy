## Content Warning ##################################
##
## A custom screen that warns players of possibly upsetting content in the game
## the first time they launch the game. Based on the About screen.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

screen content_warning():

    tag menu

    frame:

        align(0.5, 0.5)
        xmargin 50
        xpadding 100

        vbox:
            
            align(0.5, 0.5)
            spacing 50
            # xfill True
            style_prefix "presplash"

            label _("Content Warning") xalign 0.5

            text _("This is just a GUI template for projects, but if you have sensitive content that may not be suitable for all audience, this is a screen to alert players ahead of time.") text_align 0.5 xalign 0.5

            null height 20

            text _("List your content warnings here!") text_align 0.5 xalign 0.5

            null height 40

            text _("By clicking confirm, you affirm that you are willing to interact with such content.") text_align 0.5 xalign 0.5

            textbutton _("Confirm") action Return() xalign 0.5 text_align 0.5 text_size 55
    


## Splashscreen Settings##################################
##
## A custom screen that tells players to adjust their settings in the Preferences
## Screen. Edited so you don't have to keep track of two different pages.

screen splash_settings():

    tag menu

    frame:

        align(0.5, 0.5)
        xmargin 50
        xpadding 100

        vbox:
            
            align(0.5, 0.5)
            spacing 50
            # xfill True
            style_prefix "presplash"

            label _("Set Your Preferences") xalign 0.5

            text _("You can set your preferences for game settings in the next menu. These options can be adjusted at any time in the menu.") text_align 0.5 xalign 0.5

            textbutton _("Confirm") action Return() xalign 0.5 text_align 0.5 text_size 55



style presplash_label:
    top_margin gui.pref_spacing
    bottom_margin 3
    text_align 0.5

style presplash_label_text:
    yalign 1.0
    size 100


## Splashscreen Settings Old ##################################
##
## A custom screen that allows players to set their accessibility settings the first
## time they launch the game. Borrows elements from the Preferences screen in
## screens.rpy, and will need to be manually adjusted.
## You can switch back to this if you preferred the look of this

# screen splash_settings():

#     modal True

#     zorder 200

#     style_prefix "confirm"

#     frame:

#         xpadding 100
#         ypadding 50
#         xmargin 200

#         vbox:

#             yalign .5
#             xalign 0.5
#             spacing 30
#             xfill True

#             label _("Accessibility Settings") xalign 0.5
#             label _("These options can be adjusted at any time in the menu.") xalign 0.5

#             hbox:
#                 xalign 0.5
#                 vbox:
#                     style_prefix "radio"
#                     label _("Typeface")
#                     textbutton _("DejaVu Sans") action [gui.SetPreference("font", "DejaVuSans.ttf"), gui.SetPreference("size", 31), SetVariable("persistent.typeface", "DejaVuSans")] alt "Change font to DejaVu Sans"
#                     textbutton _("{font=gui/font/Atkinson-Hyperlegible-Regular-102.ttf}{size=40}Hyperlegible{/size}{/font}") action [gui.SetPreference("font", "gui/font/Atkinson-Hyperlegible-Regular-102.ttf"), gui.SetPreference("size", 32), SetVariable("persistent.typeface", "Hyperlegible")] alt "Change font to HyperLegible"

#                 vbox:
#                     style_prefix "radio"
#                     label _("Font Size")
#                     if persistent.typeface == "DejaVuSans":
#                         textbutton _("Large") action gui.SetPreference("size", 40) alt "Change to Large Size Text"
#                         textbutton _("Regular") action gui.SetPreference("size", 31) alt "Change to Regular Size Text"
#                     elif persistent.typeface == "Hyperlegible":
#                         textbutton _("Large") action gui.SetPreference("size", 38) alt "Change to Large Size Text"
#                         textbutton _("Regular") action gui.SetPreference("size", 32) alt "Change to Regular Size Text"

#                 vbox:
#                     style_prefix "radio"
#                     label _("Text Color")
#                     textbutton _("White") action gui.SetPreference("color", "#ffffff") alt "Change text color to white" 
#                     textbutton _("Cream") action gui.SetPreference("color", "#FFFDD0") alt "Change text color to cream" 

#             hbox:
#                 xalign 0.5
#                 vbox:
#                     style_prefix "radio"
#                     label _("Line Spacing")
#                     textbutton _("Taller") action gui.SetPreference("dialogue_spacing", 4) alt "Change the height of the space between lines of dialogue to be taller"
#                     textbutton _("Regular") action gui.SetPreference("dialogue_spacing", 2) alt "Change the height of the space between lines of dialogue to the regular height"

#                 vbox:
#                     style_prefix "check"
#                     label _("Toggles") 
#                     textbutton _("Image Descriptions") action ToggleVariable("persistent.image_captions") alt "Toggle Image Descriptions"
#                     textbutton _("Audio Titles") action ToggleVariable("persistent.sound_captions") alt "Toggle Sound Captions"
#                     if renpy.variant("pc"):
#                         ## Self-voicing does not work on smartphone devices, so this
#                         ## option only shows if the user is playing on a PC.
#                         textbutton _("Self-Voicing") action Preference("self voicing", "toggle") alt "Toggle Self-Voicing"
#                     textbutton "Screenshake" action ToggleField(persistent,"screenshake",true_value=True,false_value=False) alt "Toggle Screen Shake"

#             textbutton _("Confirm") action Return() xalign 0.5

# style presplash_label:
#     top_margin gui.pref_spacing
#     bottom_margin 3
#     text_align 0.5

# style presplash_label_text:
#     yalign 1.0


## Extras screens ###########################################
##
## Screens that includes Image Galleries, Music Room, Replay Room, and Dev Notes.
## https://www.renpy.org/doc/html/rooms.html

## We let Ren'Py resize our images so we don't have to make buttons in another
## program.

## These background buttons are 480x270
image room_button = im.FactorScale("bg/room.jpg", 0.25)
image office_button = im.FactorScale("bg/future_office.jpg", 0.25)
image beach_button = im.FactorScale("bg/sort_of_beautiful_beach_day.jpg", 0.25)
image bglock_button = "gui/button/bg_locked.jpg"

## These sprite buttons are 290x290
image eneutral_button = Crop((170, 245, 290, 290), "eileen neutral")
image esurprised_button = Crop((170, 245, 290, 290), "eileen surprised")
image eupset_button = Crop((170, 245, 290, 290), "eileen upset")
image eangry_button = Crop((170, 245, 290, 290), "eileen angry")
image spritelock_button = "gui/button/sprite_locked.jpg"

init python:

    g_bg = Gallery()

    # Backgrounds for the BG Gallery
    g_bg.button("room")
    g_bg.unlock_image("room") 

    g_bg.button("office")
    g_bg.image("future_office")
    g_bg.unlock("future_office")

    g_bg.button("beach")
    g_bg.image("sort_of_beautiful_beach_day")
    g_bg.unlock("sort_of_beautiful_beach_day")

    # Sprites for the Sprite Gallery
    # We put a background in the first spot so Eileen isn't floating in a void.

    g_sprite = Gallery()

    g_sprite.button("eileen neutral")
    g_sprite.unlock_image("room", "eileen neutral")
    #g_sprite.unlock_image("room", "eileen neutral")
    g_sprite.unlock_image("sort_of_beautiful_beach_day", "eileen summer neutral")

    g_sprite.button("eileen surprised")
    g_sprite.unlock_image("room", "eileen surprised")

    g_sprite.button("eileen upset")
    g_sprite.image("room", "eileen upset")
    g_sprite.unlock("room", "eileen upset")

    g_sprite.button("eileen angry")
    g_sprite.image("room", "eileen angry")
    g_sprite.unlock("room", "eileen angry")

    # The button used for locked images
    g_bg.locked_button = "bglock_button"
    g_sprite.locked_button = "spritelock_button"

    # The transition used when switching images.
    g_bg.transition = dissolve
    g_sprite.transition = dissolve

    # MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Add music files.
    mr.add("audio/music/Careless-Summer_Looping.mp3", always_unlocked=True)
    mr.add("audio/music/Future-Business_v001.mp3")
    mr.add("audio/music/Sculpture-Garden_Looping.mp3")
    mr.add("audio/music/mystery-dark-mysterious.mp3")

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.

screen extras_navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("Conquest") action ShowMenu("bobcachievements") alt "Achievements"

        textbutton _("Gallery") action ShowMenu("gallery") alt "Background Gallery"

        # textbutton _("Music Room") action ShowMenu("music_gallery") alt "Music Room"

        textbutton _("Replay") action ShowMenu("replay_gallery") alt "Replay Room"

        textbutton _("Return") action Return() alt "Return"

## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.

screen extras_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    label title

    use extras_navigation


## Gallery screen ############################################################
##
## This is a simple screen that shows buttons that gallery.

screen gallery():

    tag menu

    add "gray"

    $start = gallery_page * maxperpage
    $end = min(start + maxperpage - 1, len(gallery_items) - 1)

    #grid for images
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
                    at imageThumb
            else:
                imagebutton: 
                    idle gallery_items[i].images
                    style "gallery_button" #delete this line to remove hover
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5
                    at imageThumb

        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #grid for info
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                style_prefix "name"
                spacing maxthumbx - 20
                xalign 0.5
                yalign 0.1
                text gallery_items[i].name
        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #previous, next, and return buttons
    if gallery_page > 0:
        textbutton "{color=#000}Previous{/color}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 0.98
            background "#fff8"
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "{color=#000}Next{/color}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.98
            background "#fff8"
    textbutton "{color=#000}Return{/color}":
        action Return() 
        xalign 0.5
        yalign 0.98
        background "#fff8"

screen gallery_closeup(images): #shows full sized image as a button on top of everything!
    zorder 10
    imagebutton idle images[closeup_page]:
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
        xalign 0.5
        yalign 0.98
        background "#fff8"


## Music Gallery screen ############################################################
##
## This is a simple screen that shows buttons that play a music track.

screen music_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu(_("Music Room")):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each track.
            textbutton "Mystery Dark Mysterious" action mr.Play("audio/music/mystery-dark-mysterious.mp3")
            textbutton "Sculpture Garden" action mr.Play("audio/music/Sculpture-Garden_Looping.mp3")
            textbutton "Future Business" action mr.Play("audio/music/Future-Business_v001.mp3")
            textbutton "Careless Summer" action mr.Play("audio/music/Careless-Summer_Looping.mp3")

            null height 20

            hbox:
            # Buttons that let us advance through tracks.
                textbutton "Previous" action mr.Previous() alt "Previous Song"
                textbutton "Next" action mr.Next() alt "Next Song"

            null height 20

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()

        ## Restore the main menu music upon leaving.
        ## You can actually comment this out if you want to let players enjoy the music
        ## while looking at the other screens.
        on "replaced" action Play("music", "audio/mystery-dark-mysterious.mp3")

## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.

screen replay_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu(_("Replay Room")):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each section.
            textbutton "The Beginning" action Replay("start")
            textbutton "The Office" action Replay("office")
            textbutton "The Beach" action Replay("beach")

            null height 20

## Dev Notes screen ########################################
##
## This screen contains a message for players after they beat the entire game.
## We borrowed the base of this screen from the About screen.

screen dev_notes():

    tag menu

    ## This use statement includes the extras_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the extras_menu
    ## screen.
    use extras_menu(_("Developer's Notes"), scroll="viewport"):

        style_prefix "about"

        vbox:

            ## Your text goes here.
            if gui.dev_notes:
                text "[gui.dev_notes!t]\n"

## Type your special message here.
define gui.dev_notes = _p("""Hello, this is BáiYù of tofurocks here. I want to thank you for downloading this All-In-One GUI template to use in your own game, though it's been a while since I last updated this, hasn't it? Somehow when I updated Eileen's sprite with the latest version of Mannequin, Ren'Py wouldn't recognize her new Happy face layer... I hope that it's okay though.
    \n
    While the code provided here is almost a straight copy from the official documentation for the most part, I purposely kept it very bare-bones so that you can customize the GUI yourself. I hope that by sharing this with others, the overall quality of all Ren'Py games will improve.
    \n
    Thank you for taking the time to read this, and I wish you the best on your
    development adventures to come.""")

## Achievements screen ######################################
##
## Achievements have been moved to 0bobcachievements.rpy and sbobcachievements.rpy

## End Credits Scroll ############################################################
## A new optimized screen for showing rolling credits. This is similar to the
## gui.about string in options.rpy, and you can style it using text tags.
## https://www.renpy.org/doc/html/text.html

## The contents of your credits screen.
define credits_string = _p("""
{size=+100}Credits{/size}
\n\n
{size=+75}Programming{/size}
\n
BáiYù
\n
bobcgames
\n
npckc
\n
TheoMinute
\n\n
{size=+75}Art{/size}
\n
Sprites - Mannequin by HelloAR14
\n
Backgrounds - Uncle Mugen
\n\n
{size=+75}Soundtrack{/size}
\n
Eric Matyas
\n\n
{size=+75}Special Thanks{/size}
\n
Renall
\n\n\n\n\n\n\n\n
{size=+100}Made with{/size}
\n
{size=+100}Ren'Py [renpy.version_only].{/size}
\n\n\n\n
{size=+100}Thanks for Playing!{/size}
""")

## Here's a blank one with common roles to fit your game.
## TODO: Adjust this to fit your project
# define credits_string = _p("""
# {size=+100}Credits{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Producer:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Director:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Writing:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Art:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Music:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Sound:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Voiceover:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Programming:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Trailer:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Beta-Testing:{/size}
# \n
# Lorem Ipsum
# \n\n
# {size=+75}Special Thanks:{/size}
# \n
# Lorem Ipsum
# \n\n
# \n\n\n\n\n\n\n\n
# {size=+25}Made with Ren'Py [renpy.version_only].{/size}
# \n\n\n\n\n\n\n\n
# {size=+100}Thanks for Playing!{/size}
# """)

## This controls the position and speed of your end credits.
transform credits_scroll(t):
    xcenter 0.5 yanchor 0.0 ypos 1.0
    linear t yanchor 1.0 ypos 0.0

## The actual end credits screen that we call.
screen credits(t):
    
    style_prefix "credits"

    ## Ensure that the game_menu screens don't appear and interrupt the credits.
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    ## If a player has seen the end credits before, this button appears.
    if persistent.credits_seen:

        textbutton _("Skip End Credits") action Jump("skip_credits") xalign 1.0 yalign 1.0

    ## When t is up, the game will go to the next line.
    timer t action Return()
    ## The contents of your credits screen is here.
    text credits_string text_align 0.5 at credits_scroll(t)

    ## To use in script:
    ### call screen credits(t)
    ## Where t is the number of seconds it takes to scroll

style credits_text:
    size gui.title_text_size
    color "#ffffff"


## Results Screen ############################################################
## A screen that displays how much of the game the player has seen.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=39859
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.count_dialogue_blocks

# This creates a percentage based on how much of the game the player has seen. 
init python:

    numblocks = renpy.count_dialogue_blocks()

    def percent():

        global readtotal
        readtotal = renpy.count_seen_dialogue_blocks()* 100 / numblocks
        persistent.readtotal = readtotal
        ## This is displayed in our Achievements screen.

default readtotal = 0

screen results():
    
    zorder 200

    vbox:
        xalign .5
        yalign .2
        spacing 45

        text _("Script Seen: [readtotal]%") color "#fff"

## TODO: Figure out how to get total game time working properly
## https://lemmasoft.renai.us/forums/viewtopic.php?t=40407
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.get_game_runtime

# default playtime = 0

# init 2 python:

#     def total_playtime(d):
#         renpy.store.playtime += renpy.get_game_runtime()
#         #renpy.clear_game_runtime()
#         d["playtime"] = renpy.store.playtime

    # config.save_json_callbacks = [total_playtime]