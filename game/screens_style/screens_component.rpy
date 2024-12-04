define dr_current_next_value = 0

screen menu_tile(title, scroll=None, yinitial=0.0):

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

    label title

screen close_button(actions =  [
        Return(),
    ]):

    # button for closure
    imagebutton:
        align (0.95, 0.05)
        idle 'gui close_button'
        action actions,
        if renpy.variant("pc"):
            focus_mask True
        at dr_close_button_transform
    key 'K_ESCAPE' action actions
    key 'mouseup_3' action actions

screen check_box(my_action, value = False, my_size = 40, my_align = (0, 0)):
    imagebutton:
        align (my_align)
        if value:
            idle 'gui check_box_on'
        else:
            idle 'gui check_box_off'
        action my_action
        at dr_check_box_transform(my_size)

screen arrow(my_align = (0, 0), my_rotate = 0):
    image "gui triangular_button":
        align my_align
        rotate my_rotate
        size (gui.dr_triangular_button_size, gui.dr_triangular_arrow_height_button_size)
        at flickering_lights
