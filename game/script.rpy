# The script of the game goes in this file.

# Set up LayeredImage Sprites
layeredimage eileen:

    group base auto:
        attribute casual default

    if casual:

        "eileen_headband"

    group face auto:
        attribute neutral default

# This adds Eileen's headband to her sprite when True
default casual = True

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#f88787", image="eileen")
define e_nvl = Character("Eileen", color="#f88787", kind=nvl, image="eileen")
define e_bubble = Character(color="#f88787", kind=bubble, image="eileen")
define nar_nvl = nvl_narrator

## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

## The animation is boring so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

image splash_anim_1:

    "gui/n421rr-logo.webp"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

default persistent.firstlaunch = False

label splashscreen:
    
    scene black

    ## Here begins our splashscreen animation.
    show splash_anim_1
    show text "{size=60}Made with Ren'Py [renpy.version_only]{/s}":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 6.0
        linear 1.0 alpha 1.0
    
    ## The first time the game is launched, players cannot skip the animation.
    if not persistent.seen_splash:
        
        ## No input will be detected for the set time stated.
        ## Set this to be a little longer than how long the animation takes.
        $ renpy.pause(8.5, hard=True)
 
        $ persistent.seen_splash = True
    
    ## Players can skip the animation in subsequent launches of the game.
    else:
 
        if renpy.pause(8.5):
 
            jump skip_splash

    scene black
    with fade
 
    label skip_splash:
 
        pass
    
    call screen content_warning

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.firstlaunch:

        call screen splash_settings

        call screen preferences

        ## This screen will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.firstlaunch = True

    return

## The game starts here.

label start:    
    
    $ set_flags("goout", True)
    
    call map_doors_setup

    call change_room(room_id = "west_wing_campus_entrance")

    # enable a notify screen
    call enable_notifyEx

    # the first time it opens room navigation screen use after_spending_time
    # for update routine, event...
    call after_spending_time
    # "Hello, this is a test of NQTR-System."
    # open the room navigation screen
    call screen room_navigation
    return

## End Credits
label credits:

    ## We hide the quickmenu for the last part of the game so they don't
    ## appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things
    window hide

    scene black with fade

    ## Find "End Credits Scroll" in extras.rpy to change text.
    call screen credits(15.0)

    $ persistent.credits_seen = True

    scene black
    with fade
    
    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:
 
        pass

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.
    show screen results
    
    centered "Fin"

    hide screen results

    if persistent.game_clear:

        pass

    ## Do you want to leave some author's notes or a hidden message for your dedicated fans?
    ## This will check if they've seen all that the game has to offer.
    else:

        if readtotal == 100:

            achieve completionist

            ## Due to the way that $ percent() works, we need to make this a text displayable
            ## or else it'll try to count it too.
            show text "{size=60}{color=#ffffff}You've unlocked a special message.\nAccess it through the Extras Menu.{/color}{/s}":
                xalign 0.5 yalign 0.5 alpha 0.0
                linear 1.0 alpha 1.0

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    ## We re-enable the quickscreen as the credits are over.
    $ quick_menu = True

    # This ends the game.
    return