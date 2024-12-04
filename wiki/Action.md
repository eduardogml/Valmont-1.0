***IMPORTANT***: always close labels with: [Methods for closing a label](https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Methods-for-closing-a-label)

***INFO***: day_deadline & day_start must be >0, if not the value will be ignored

---

The [Act class](https://github.com/DRincs-Productions/NQTR-toolkit/blob/main/game/tool/action.rpy#L2) is a class for create an action.

This class extend ( have all properties and methods of ) Button class, is very important read the [NQTR Button wiki](Button).

## Usage

**INFO**: For don't create problems if you not implement this in your project, the `actions` are not defined by default empty. BUT, if you use the dict without initializing it, the system not save the changes.

For implement this you need to add this in your project:

```renpy
init python:
    from pythonpackages.nqtr.action import Act

# habitual actions
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action#add-an-action-in-dictionary
define df_actions = {
}
```

## Normal Actions (with side button)

![Screenshot 2023-10-21 115849](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/a91021c4-3e08-4979-9b2b-262f1f95fd23)

### Add an Action in dictionary

**Recommended**

(**code-snippets**: `DR_ActionAdd_in_dict`)

```renpy
# dictionary editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default actions = {}

# habitual actions
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_actions = {
    "action_id" : Action(name = _("Name"),  button_icon = "/icon_url.webp", label_name = "label_be_started", room_ids=["room_id_1", "room_id_2"], hour_start=0, hour_stop=24),
}
```

### Add an Action

**Recommended only** if the action is used a few times

(**code-snippets**: `DR_ActionAdd`)

```renpy
actions["action_id"] = Action(name = _("Name"),  button_icon = "/icon_url.webp", label_name = "label_be_started", room_ids=["room_id_1", "room_id_2"], hour_start=0, hour_stop=24)
actions["deleted after 2 days"] = Action(name = _("Name"),  button_icon = "/icon_url.webp", day_deadline=2)
actions["will start after 2 days"] = Action(name = _("Name"),  button_icon = "/icon_url.webp", day_start=3)
```

### Remove an Action

(**code-snippets**: `DR_ActionRemove`)

```renpy
python:
    actions.pop("action_id")
```

## Action with Picture in background

![Screenshot 2023-10-21 115715](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/923e986a-775e-4f32-9871-c6221985b4a2)

Thanks to the "[Picture in Background](Button#picture-in-background)" option you can add actions not on the right but in an x, y position of your preference. Read more here: [Picture in Background](Button#picture-in-background)

exemples:

```renpy
python:
    actions["action_id"] = Action(name = _("Name"),  picture_in_background = "/icon_url.webp", label_name = "label_be_started", room_ids=["room_id_1", "room_id_2"], hour_start=0, hour_stop=24)
```

```renpy
define df_actions = {
    "action_id" : Action(name = _("Name"),  picture_in_background = "/icon_url.webp", label_name = "label_be_started", room_ids=["room_id_1", "room_id_2"], hour_start=0, hour_stop=24),
}
```
