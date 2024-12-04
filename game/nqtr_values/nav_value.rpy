init python:
    from pythonpackages.nqtr.navigation import Room
    from pythonpackages.nqtr.navigation import Location
    from pythonpackages.nqtr.navigation import Map

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room
define rooms = [
    Room(id="west_wing_campus_entrance", location_id="west_wing_campus", name=_("West Wing Campus Entrance"), background ="images/location/wing_west_entrance-[tm.timeslot_number].webp"),
    Room(id="male_dorm_entrance", location_id="male_dorm_campus", name=_("Male Dorm Entrance"), background ="images/location/male-dorm-entrance-[tm.timeslot_number].webp"),
    Room(id="west_wing_hall", location_id="west_wing_campus", name=_("West Wing Hall"), background ="images/location/wing-west-hall-[tm.timeslot_number].webp"),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location
define locations = [
    Location(id = "west_wing_campus", map_id="valmont_university", external_room_id="west_wing_campus_entrance", name=_("West Wing Campus"), picture_in_background="icon map west_wing_campus", xalign=0.58, yalign=0.41),
    Location(id = "male_dorm_campus", map_id="valmont_university", external_room_id="male_dorm_entrance", name=_("Male Dorm"), picture_in_background="icon map male_dorm", xalign=0.85, yalign=0.55),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map
define maps = {
    "valmont_university": Map(
        name = _("Valmont University"), background = "bg valmont_campus",
    ),
}

label wing_west_entrance_door:
    call change_room("west_wing_hall")