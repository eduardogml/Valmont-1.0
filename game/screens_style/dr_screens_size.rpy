init -1:
    define gui.dr_multiplicateur = config.screen_height/1080
    default gui.dr_moblile_zoom = 1

    if renpy.mobile:
        $ gui.dr_moblile_zoom = 1.5
    else:
        $ gui.dr_moblile_zoom = 1

    # text
    define gui.dr_little_text_size = convert_to_int(18 * gui.dr_multiplicateur)
    define gui.dr_normal_text_size = convert_to_int(24 * gui.dr_multiplicateur)
    define gui.dr_big_normal_text_size = convert_to_int(28 * gui.dr_multiplicateur)
    define gui.nqtr_hour_text_size = convert_to_int(60 * gui.dr_multiplicateur)
    # image
    define gui.dr_small_face_size = convert_to_int(60 * gui.dr_multiplicateur)
    define gui.nqtr_button_room_size = convert_to_int(125 * gui.dr_multiplicateur)
    define gui.nqtr_button_location_size = convert_to_int(90 * gui.dr_multiplicateur)
    define gui.dr_small_menu_size = convert_to_int(80 * gui.dr_multiplicateur * gui.dr_moblile_zoom)
    define gui.nqtr_button_map_size = convert_to_int(70 * gui.dr_multiplicateur * gui.dr_moblile_zoom)
    define gui.dr_close_button_size = convert_to_int(45 * gui.dr_multiplicateur * gui.dr_moblile_zoom)
    define gui.dr_triangular_button_size = convert_to_int(70 * gui.dr_multiplicateur)
    define gui.dr_triangular_arrow_height_button_size = convert_to_int(60 * gui.dr_multiplicateur)
    define gui.notify_image_size = convert_to_int(42 * gui.dr_multiplicateur)
    define gui.joystick_button_size = convert_to_int(150 * gui.dr_multiplicateur)
    # drawer
    define gui.dr_drawer_ypos = convert_to_int(170 * gui.dr_multiplicateur)
    define gui.dr_drawer_xpos = convert_to_int(80 * gui.dr_multiplicateur)
    define gui.dr_drawer_ysize = convert_to_int(850 * gui.dr_multiplicateur)
    define gui.dr_drawer_xsize = convert_to_int(400 * gui.dr_multiplicateur)
    # nqtr menu_memo
    define gui.nqtr_menu_memo_image_ysize = convert_to_int(400 * gui.dr_multiplicateur)
    define gui.nqtr_menu_memo_image_xsize = convert_to_int(800 * gui.dr_multiplicateur)
    define gui.nqtr_menu_memo_frame_xsize = convert_to_int(1190 * gui.dr_multiplicateur)
    define gui.nqtr_menu_memo_frame_ysize = convert_to_int(400 * gui.dr_multiplicateur)
    define gui.nqtr_menu_memo_next_button_size = convert_to_int(40 * gui.dr_multiplicateur * gui.dr_moblile_zoom)
    define gui.nqtr_button_action_size = convert_to_int(120 * gui.dr_multiplicateur)
    define gui.nqtr_button_action_size_error = convert_to_int(7 * gui.dr_multiplicateur)
    # ds userinfo
    define gui.ds_userinfo_textdistance_xsize = convert_to_int(250 * gui.dr_multiplicateur)
    # Ren'Py Layered Image Masks
    define gui.sprite_size = 640
    define gui.sprite_elaborate_size = 700
    ## only for image 1920x1080
    define gui.sprite_size_x = 1032
    define gui.sprite_size_padding_x = convert_to_int((gui.sprite_size_x - gui.sprite_elaborate_size) / 2)
    # stmb
    define gui.smartphone_height = convert_to_int(1080 * gui.dr_multiplicateur)
    define gui.smartphone_width = convert_to_int(570 * gui.dr_multiplicateur)
    define gui.smartphone_screen_height = convert_to_int(gui.smartphone_height - (40 * gui.dr_multiplicateur))
    define gui.smartphone_screen_width = convert_to_int(gui.smartphone_width - (40 * gui.dr_multiplicateur))
    define gui.smartphone_screen_with_space_width = convert_to_int(gui.smartphone_screen_width - (20 * gui.dr_multiplicateur))
    define gui.smartphone_screen_contacts_width = convert_to_int(gui.smartphone_width - (150 * gui.dr_multiplicateur))
    define gui.smartphone_screen_contacts_height = convert_to_int(gui.smartphone_height - (350 * gui.dr_multiplicateur))
    define gui.smartphone_screen_app_height = convert_to_int(gui.smartphone_height - (300 * gui.dr_multiplicateur))
    define gui.smartphone_column_app_number = 4
    define gui.smartphone_app_icon_size = convert_to_int(75 * gui.dr_multiplicateur)
    define gui.smartphone_app_icon_space = convert_to_int(45 * gui.dr_multiplicateur)
    define gui.smartphone_app_icon_space_taskbar = convert_to_int(25 * gui.dr_multiplicateur)
    define gui.smartphone_nav_button_size = convert_to_int(75 * gui.dr_multiplicateur)
    define gui.smartphone_contact_icon_size = convert_to_int(100 * gui.dr_multiplicateur)
    define gui.smartphone_contact_big_icon_size = convert_to_int(300 * gui.dr_multiplicateur)
    define gui.tv_remote_control_litled_size = convert_to_int(37 * gui.dr_multiplicateur)