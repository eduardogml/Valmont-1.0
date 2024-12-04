# Navigation and Map

***INFO***: Navigation is based on `Constants`:

* What this means is that it cannot be changed while the game is running
* The benefit is not having to worry about rescues coming from different versions

---

![Navigation](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/6b493f40-d809-46f1-80ee-b2a905f1951d)

The navigation system is designed in the following way:

* The player is placed in a room
* To be reachable, each room must be connected to a location and a map
* The player, from the current room, can move to another room at the same location.
* For move in another location the player need to use the map.

## Usage

**INFO**: For don't create problems if you not implement this in your project, the `rooms`, `locations` and `maps` are not defined by default empty. BUT, if you use the dict without initializing it, the system not save the changes.

For implement this you need to add this in your project:

```renpy
init python:
    from pythonpackages.nqtr.navigation import Room
    from pythonpackages.nqtr.navigation import Location
    from pythonpackages.nqtr.navigation import Map

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room
define rooms = [
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location
define locations = [
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map
define maps = {
}
```

## Room

The [Room class](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/navigation.py#L10) is a class for create a room.

This class extend ( have all properties and methods of ) Button class, is very important read the [NQTR Button wiki](Button).

### Add a Room in list

(**code-snippets**: `DR_RoomAdd_in_list`)

```renpy
define rooms = [
        Room(id="room_id", location_id="house", name=_("My room"), button_icon="icon myroom", background ="bg myroom", action_ids = []),
        Room(id="my_room", location_id="house", name=_("MC room"), button_icon="icon myroom", background ="bg myroom", action_ids = ["sleep","nap",]), 
        Room(id="bathroom", location_id="house", name=_("Bathroom"), button_icon="icon bathroom", background ="bg bathroom"), 
        Room(id="lounge", location_id="house", name=_("Lounge"), button_icon="icon lounge", background ="bg lounge"), 
        Room(id="terrace", location_id="house", name=_("Terrace"), button_icon="icon terrace", background ="bg terrace"), 
    ]
```

### Change Room

**INFO**: changing the info will also change the current location

(**code-snippets**: `DR_ChangeRoom`)

```renpy
label start:
    call change_room(room_id = "my_room")
```

### Go Previous room

**IMPORTANT**: the chronology of rooms is only one, so be careful in using it

```renpy
call go_previous_room
```

### Room with Picture in background

![Screenshot 2023-10-21 115715](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/923e986a-775e-4f32-9871-c6221985b4a2)

With to the "[Picture in Background](Button#picture-in-background)" option you can add rooms not on the right but in an x, y position of your preference. Read more here: [Picture in Background](Button#picture-in-background)

## Location

The [Location class](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/navigation.py#L87) is a class for create a location.

This class extend ( have all properties and methods of ) Button class, is very important read the [NQTR Button wiki](Button).

### Add a Location in list

(**code-snippets**: `DR_LocationAdd_in_list`)

When the player click on the location button, the player will be moved to the `external_room_id` and close the map.

```renpy
define locations = [
        Location(id = "house_id", key_map="map", name=_("My house"), picture_in_background="icon map home", external_room_id="house_id_external_room", xalign=0.5, yalign=0.5),
]
```

### Change Location

( it is **not** recommended to use it, it makes more sense to use [**Change Room**](#change-room) )

```renpy
call change_location(location_id = "my_location")
```

## Map

The [Map class](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/navigation.py#L153) is a class for create a map.

This class extend ( have all properties and methods of ) Button class, is very important read the [NQTR Button wiki](Button).

![Screenshot 2023-10-21 120422](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/3b5f36fe-3f37-4a26-9f51-ac2fe9a13938)

### Add a Map in dict

There is the possibility to add more maps and connect them with `map_id_north`, `map_id_south`, `map_id_west` and `map_id_east`.

(**code-snippets**: `DR_MapAdd_in_dict`)

```renpy
define maps = {
    "map": Map(
        name = _("Map"), background = "bg map",
        map_id_north = "nightcity",
        map_id_south = None,
        map_id_west = None,
        map_id_east = None,
    ),
    "nightcity": Map(
        name = _("Night City"), background = "bg nightcity",
        map_id_north = None,
        map_id_south = "map",
        map_id_west = None,
        map_id_east = None,
    ),
}
```

### Block Map

For block the map you need to add the flag `goout`.

Read more about [Flags](https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags)

For Example:

```renpy
# https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags
define flag_keys = [
    # Map Block
    "goout",
]
```

### Check Go Out

Please note that to check whether the map can be used I used check_goout in open_map:

```renpy
define block_goout_dialogue = _("Now is not the time to go outside")
label check_goout:
    if(not get_flags("goout")):
        "[block_goout_dialogue]"
        call screen room_navigation
    return
```

Unlock the map:

```renpy
python:
    set_flags("goout", True)
```

### Best sites for creating map images

* [cyberpunk map](https://maps.piggyback.com/cyberpunk-2077/maps/night-city)
* [Hex Kit](https://cone.itch.io/hex-kit)
* [Village Generator](https://watabou.itch.io/village-generator)
* [Medieval Fantasy City Generator](https://watabou.itch.io/medieval-fantasy-city-generator)
* [Tabletop RPG Map editor II](https://deepnight.itch.io/tabletop-rpg-map-editor)
* [Neighbourhood Generator](https://watabou.itch.io/neighbourhood)
* [Styling Wizard](https://mapstyle.withgoogle.com/)

## Closed Room

( [**in progress**](https://github.com/DRincs-Productions/NQTR-toolkit/issues/18) )

<!-- It is possible to make a room closed: ... is a dictionary of closed rooms (id=room_id : Commitment()), it is used in change_room and in after_wait closed rooms are deleted (every hour). the expiration time is .hour_stop, if you don't want a deadline: .hour_stop = None.
The room will remain closed from hour_start to hour_stop, only if at least one NPC is present in it, if you want the room always closed: .chs = None.

Examples of how to add them:

```renpy
$ closed_rooms[cur_room.id] = df_routine["alice_sleep"]
jump after_wait
```

```renpy
$ closed_rooms[cur_room.id] = df_routine["alice_sleep"]
# does not expire
$ closed_rooms[cur_room.id].hour_stop = None
# will remain closed even if there are no NPCs inside.
$ closed_rooms[cur_room.id].chs = None
jump after_wait
```

```renpy
$ closed_rooms[cur_room.id] = Commitment(chs={"alice" : None}, hour_start=14, hour_stop=20)
jump after_wait
```

Where to change the image of the closed door or customise the event? in closed_room_event. -->

### is closed room

( [**in progress**](https://github.com/DRincs-Productions/NQTR-toolkit/issues/18) )

### Add event when room is closed

( [**in progress**](https://github.com/DRincs-Productions/NQTR-toolkit/issues/18) )

<!-- For add an event when the room is closed you need to add the label `closed_room_event_custom` in your project:

```renpy
label closed_room_event_custom:
    # Custom code
    # if (cur_room == ...):
        # ...
    return
``` -->
