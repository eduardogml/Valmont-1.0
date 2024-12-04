style dr_menu_vscroll is vscrollbar:
    xsize 7
    unscrollable 'hide'

init:
    transform nqtr_button_room_transform:
        size (gui.nqtr_button_room_size, gui.nqtr_button_room_size)
        on selected_idle:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 1 alpha 0.9 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 1 alpha 0.9 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.5)
    transform nqtr_button_location_transform:
        size (gui.nqtr_button_location_size, gui.nqtr_button_location_size)
        on selected_idle:
            yanchor 0 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 1 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 1 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform nqtr_button_action_transform:
        size (gui.nqtr_button_action_size, gui.nqtr_button_action_size)
        on selected_idle:
            yanchor 0 alpha 0.7
        on idle:
            yanchor 0 alpha 0.7
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform nqtr_button_picture_transform:
        on selected_idle:
            yanchor 0 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform dr_small_face_transform:
        size (gui.dr_small_face_size, gui.dr_small_face_size)
        on selected_idle:
            yanchor 0 alpha 1.0
        on idle:
            yanchor 0 alpha 1.0
        on hover:
            yanchor 1 alpha 0.93
        on selected_hover:
            yanchor 1 alpha 0.93
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform dr_button_menu_transform:
        size (gui.dr_small_menu_size, gui.dr_small_menu_size)
        on selected_idle:
            yanchor 0 alpha 0.4
        on idle:
            yanchor 0 alpha 0.4
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform dr_close_button_transform:
        xanchor 25
        size (gui.dr_close_button_size, gui.dr_close_button_size)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.5)
            linear 1.0 matrixcolor BrightnessMatrix(0.2)
            linear 1.0 matrixcolor BrightnessMatrix(0.5)
            repeat
    transform nqtr_button_map_transform(rotation = 0):
        rotate rotation
        xysize (gui.nqtr_button_map_size, gui.nqtr_button_map_size)
        on selected_idle:
            yanchor 0 alpha 0.5
            linear 2.0 alpha 0.8
            linear 2.0 alpha 0.5
            repeat
        on idle:
            yanchor 0 alpha 0.5
            linear 2.0 alpha 0.8
            linear 2.0 alpha 0.5
            repeat
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform dr_button_next_transform(rotation = 0):
        size (gui.nqtr_menu_memo_next_button_size, gui.nqtr_menu_memo_next_button_size)
        rotate rotation
        on idle:
            alpha 0.6 matrixcolor BrightnessMatrix(0)
        on hover:
            alpha 1.0 matrixcolor BrightnessMatrix(0.2)
        on insensitive:
            alpha 0.6 matrixcolor BrightnessMatrix(-0.5)
    transform dr_check_box_transform(my_size):
        size (my_size, my_size)
        on selected_idle:
            yanchor 0 alpha 0.7
        on idle:
            yanchor 0 alpha 0.7
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    # stmb
    transform smartphone_nav_button:
        xanchor 25
        size (gui.smartphone_nav_button_size, gui.smartphone_nav_button_size)
        on idle:
            matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.2)
    transform smartphone_app(icon_size):
        xanchor 25
        size (icon_size, icon_size)
        on idle:
            matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.2)
    transform smartphone_contact_icon:
        size (gui.smartphone_contact_icon_size, gui.smartphone_contact_icon_size)
    transform tv_remote_control_small_button:
        size (gui.tv_remote_control_litled_size, gui.tv_remote_control_litled_size)
        on idle:
            matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.2)
    transform flickering_lights:
        matrixcolor BrightnessMatrix(0) 
        linear 1.0 matrixcolor BrightnessMatrix(0.2)
        linear 1.0 matrixcolor BrightnessMatrix(0)
        repeat
    transform joystick_button:
        size (gui.joystick_button_size, gui.joystick_button_size)
        on idle:
            matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.4)
        on selected_idle:
            matrixcolor BrightnessMatrix(0.2)
        on selected_hover:
            matrixcolor BrightnessMatrix(0.4)
        on insensitive:
            matrixcolor BrightnessMatrix(-0.3)
