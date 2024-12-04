## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.
init python:

    maxthumbx = config.screen_width / (3 + 1)
    maxthumby = config.screen_height / (3 + 1)

    replay_page = 0

    class ReplayItem:
        def __init__(self, thumbs, replay, name):
            self.thumbs = thumbs
            self.replay = replay
            self.name = name

        def num_replay(self):
            return len(self.thumbs)

    #add replay items here format below
    #Replay_items.append(ReplayItem(["the thumbnail"], "the_label_from_code", "brief description"))
    Replay_items = []
    Replay_items.append(ReplayItem(["Rthumb1"], "mainmenu_setup", "Gallery button setup"))
    Replay_items.append(ReplayItem(["Rthumb1"], "main_gallery_images", "Gallery Images"))
    Replay_items.append(ReplayItem(["Rthumb1"], "gallery_usage", "Making Gallery Images viewable"))
    Replay_items.append(ReplayItem(["Rthumb1"], "replay_button", "Replay button setup"))
    Replay_items.append(ReplayItem(["Rthumb1"], "replay_list_setup", "Replay list setup"))
    Replay_items.append(ReplayItem(["Rthumb1"], "finished", "The last bit needed"))


# a black background screen for the selection
image black = "#000000"

#replay thumbnails images setup defined here
image Rthumb1 = ("images/replay/replay_unlock.jpg")
#image Rthumb2 = ("images/replay/anotherimage.jpg")