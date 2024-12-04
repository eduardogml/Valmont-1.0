# Routine system

![Routine](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/b285da01-960b-4a0c-b05b-44c31e34a409)

For manage the character routine, you can use the "Routine system". This system is based on the Commitment class.
The [Commitment class](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/routine.py) is the fundamental element for creating a routine system.

exemple:

```python
Commitment(
    characters = a, # characters can be a Ren'Py Character or a list
    hour_start = 20, hour_stop = 10, # hour_start and hour_stop are int
    location_id = "house", room_id = "alice_room", # location_id and room_id are string
    background ="bg alice roomsleep", # background image
),
```

To implement the routine system there are two different methods:

* [Repetitive routines](#repetitive-routines) (routines that recur every day, every week...)
* [Routines destined to have an end](#routines-destined-to-have-an-end) (Routine that will end in a few days, week...)
* [Events](#events) is a particular routine that run a label when the player is in a certain position and/or at a certain time and/or based on the disabled check.

Both methods have the following characteristics:

* [Characters and Conversation](#characters-and-conversation)
* [Disabled](#disabled)
* [Priority](#priority)

## Repetitive routines

Repetitive routines are routines that recur every day, every week...

Repetitive routines are based on a dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)

Pay attention to these characteristics:

* If you want [disable](#disabled) a routine, you must use the `key of flags` (the sistem get the value of flag).
* `day_deadline` property not work.

### Usage

(**code-snippets**: `DR_RoutineAdd_in_dict`)

**INFO**: For don't create problems if you not implement this in your project, the `df_routine` are not defined by default empty. BUT, if you use the dict without initializing it, the system not save the changes.

For implement this you need to add this in your project:

```renpy
init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.conversation import Conversation

# habitual routine
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_routine = {
}
```

exemple:

```renpy
init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.conversation import Conversation

# habitual routine
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_routine = {
    "alice_sleep" : Commitment(
        conversations = [
            Conversation(
                name="talk_alice_sleep",
                label_name="talk_sleep",
                characters=a,
                conversation_background = None,
            ),
        ],
        hour_start=20, hour_stop=10,
        location_id="house", room_id="alice_room",
        background ="bg alice roomsleep",
    ),
    # alice_go_school have more priority than alice_read, because it is before in the dictionary
    "alice_go_school" : Commitment(
        characters=a, # characters can be a string or a list of strings
        hour_start=10, hour_stop=14,
        location_id="school",
        disabled="weekend",
    ),
    "alice_read" : Commitment(
        conversations = [
            Conversation(
                name="talk_alice_read",
                characters=a,
                conversation_background ="bg alice terrace talk"
            ),
        ],
        hour_start=10, hour_stop=20,
        location_id="house", room_id="terrace",
        background ="bg alice terrace",
    ),
}
```

## Routines destined to have an end

Routines destined to have an end are routines that will end in a few days, week...

This routines are based on a dictionary enpy that can be modified at runtime.

You can use `day_deadline` property for set the deadline of the routine.

### Add an Commitment

(**code-snippets**: `DR_RoutineAdd`)

```renpy
python:
    routine["stagealice1"] = Commitment(characters=a, hour_start=14, hour_stop=20, location_id="house", room_id="terrace")
```

### Delete an Commitment

```renpy
python:
    del routine["stagealice1"]
```

## Events

**IMPORTANT**: in case at the end of the event the same event occurs again the event will be deleted (to avoid loops). to not delete it you can use some stratagems with these functions: [Methods for closing a label](https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Methods-for-closing-a-label)

By Events we mean: a label that is automatically started as soon as the player is in a certain position and/or at a certain time and/or based on the disabled check.

To implement it simply pass it by parameter to a [Commitment](#commitment) `event_label_name`

### Add an Event in [Repetitive routines](#repetitive-routines)

( **Recommended** )

(**code-snippets**: `DR_EventAdd_in_dict`)

```renpy
init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.conversation import Conversation

# habitual routine
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_routine = {
    "routine_id" : Commitment(
        characters=[],
        event_label_name = "routine_id_event_label"
        hour_start=0, hour_stop=24,
        room_id="room_id", location_id="home",
    ),
}
```

### Add an Event in [Routines destined to have an end](#routines-destined-to-have-an-end)

(**code-snippets**: `DR_EventAdd`)

```renpy
python:
    routine["routine_id"] = Commitment(
        characters=[],
        event_label_name = "routine_id_event_label"
        hour_start=0, hour_stop=24,
        room_id="room_id", location_id="home",
    )
```

### Add event by if

If you want to add an event based on a condition, you can use the label `check_event_custom`.

For example:

```renpy
label check_event_custom:
    # Custom code
    # if (cur_room == ...):
        # call ...
    return
```

## Characters and Conversation

How show up, into the Commitment class, you can set the `characters` and `conversations` properties.

Into the creation of Commitment class, the `characters` and `conversations` properties are unified.

### characters

```python
Commitment(
    characters = a, # characters can be a Ren'Py Character or a list
    hour_start = 20, hour_stop = 10,
    location_id = "house", room_id = "alice_room",
    background ="bg alice roomsleep",
),
```

The `characters` property can be a [Ren'Py Character](https://www.renpy.org/doc/html/dialogue.html#Character) or a list of [Ren'Py Character](https://www.renpy.org/doc/html/dialogue.html#Character). You can use this property for set the characters into the your Commitment.

---

**[The group conversations or group routines is in development](https://github.com/DRincs-Productions/NQTR-System/issues/30)**

---

This is very important for the know where the character is.

If there are more Commitments with the same character, the System will prioritize the Commitment with the highest [priority](#priority).

For add the ***icon of character*** you must use the [Character Properties Method](https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Character-Properties-Method).

### conversations

```python
Commitment(
    conversations = [
        Conversation(
            name="talk_alice_sleep",
            label_name="talk_sleep",
            characters=a,
            conversation_background = None,
        ),
    ],
    hour_start=20, hour_stop=10,
    location_id="house", room_id="alice_room",
    background ="bg alice roomsleep",
),
```

---

**[The group conversations or group routines is in development](https://github.com/DRincs-Productions/NQTR-System/issues/30)**

---

The `conversations` property have the same function of [`characters` property], but is a dictionary and you can use this property for set the add [Conversation Action](Conversation-system) into the your Commitment.

For add the ***icon of character*** you must use the [Character Properties Method](https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Character-Properties-Method).

## Disabled

For disable a commitment you can use the property `disabled`. This property can be set to bool or a string.

***If is string***: you can put a key of flags ( the sistem get the value of flag). Explained here: [Flags - Ability to edit flags in constants](https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags#ability-to-edit-flags-in-constants)

In case there are multiple routines in a given hour for a given character:

* if all are enabled, only the routine with the highest [priority](#priority) will be used while the others are ignored
* if the routine with the highest priority is disabled, only the second one with the highest [priority](#priority) will be enabled
* and so on

Exemple:

```renpy
define df_routine = {
    # alice_go_school have more priority than alice_read, because it is before in the dictionary
    "alice_go_school" : Commitment(
        characters=a, # characters can be a string or a list of strings
        hour_start=10, hour_stop=14,
        location_id="school",
        disabled="weekend",
    ),
    "alice_read" : Commitment(
        conversations = [
            Conversation(
                name="talk_alice_read",
                characters=a,
                conversation_background ="bg alice terrace talk"
            ),
        ],
        hour_start=10, hour_stop=20,
        location_id="house", room_id="terrace",
        background ="bg alice terrace",
    ),
}

# Flags
define flag_keys = [
    "weekend",
]
label update_current_flags_custom:
    # Custom code
    if tm.is_weekend:
        $ set_flags("weekend", True)
    else:
        $ set_flags("weekend", False)
    return
```

## Priority

Returns the commitments of the ch (NCPs) in that Location at that time. Prioritize the special commitment and then the first commitment found.
