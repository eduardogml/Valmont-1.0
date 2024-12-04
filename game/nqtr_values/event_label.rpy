label check_event_custom:
    call game_sounds
    # Custom code
    # if (cur_room == ...):
        # ...
    return

label closed_room_event_custom:
    # Custom code
    # if (cur_room == ...):
        # ...
    return

label game_sounds:

    if cur_room.id == "west_wing_campus_entrance" or cur_room.id == "male_dorm_entrance":
        if tm.timeslot_number == 3:
            if renpy.music.get_playing(channel="env_day_night") != night_ambient:
                $ play_sound(night_ambient, channel="env_day_night", fadein=1.0, loop=True)
        else:
            if renpy.music.get_playing(channel="env_day_night") != day_ambient:
                $ play_sound(day_ambient, channel="env_day_night", fadein=1.0, loop=True)
    else:
        $ renpy.music.stop(channel="env_day_night", fadeout=1.0)
    
    return
