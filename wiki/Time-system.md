# Time system

Time system is a system that allows you to manage the time of the game. The class that handles Time is [TimeHandler](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/time.py#L9).

## Usage

**INFO**: For don't create problems if you not implement this in your project, the `tm` are not defined by default empty. BUT, if you use the dict without initializing it, the system not save the changes.

For implement this you need to add this in your project:

```renpy
define timeslot_names = [
    (2, _("Night")),
    (8, _("Morning")),
    (14, _("Afternoon")),
    (20, _("Evening")),
]
define weekday_names = [
    _("{#weekday}Monday"),
    _("{#weekday}Tuesday"),
    _("{#weekday}Wednesday"),
    _("{#weekday}Thursday"),
    _("{#weekday}Friday"),
    _("{#weekday}Saturday"),
    _("{#weekday}Sunday")
]
# ATTENTION here it is initialized
# when a save is loaded it is created with the updateTimeHandler() function
default tm = TimeHandler(
    hour_of_new_day = 5,
    hour = 8,
    weekday_weekend_begins = 6,
    day = 0,
    timeslot_names = timeslot_names,
    weekday_names = weekday_names
)
```

### New Day

(**code-snippets**: `DR_NewDay`)

```renpy
call new_day
call new_day(time_of_new_day = 9)
```

### Wait

(**code-snippets**: `DR_Wait`)

```renpy
call wait
call wait(wait_hour = 3)
```

### Now is between

(**code-snippets**: `DR_NowIsBetween`)

Check if the current time is between start and end

```renpy
if (now_is_between(start=routine.hour_start, end=routine.hour_stop)):
    # ...
```

### Is Weekend

```renpy
if tm.is_weekend:
    # ...
```

### Check of the day of the week

you can use tm.weekday_number to determine what day of the week you are on.

example:

```renpy

if tm.weekday_number == 0:
    # Monday
if tm.weekday_number == 1:
    # Tuesday
if tm.weekday_number == 2:
    # Wednesday
# ...

define weekday_names = [
    _("{#weekday}Monday"),
    _("{#weekday}Tuesday"),
    _("{#weekday}Wednesday"),
    _("{#weekday}Thursday"),
    _("{#weekday}Friday"),
    _("{#weekday}Saturday"),
    _("{#weekday}Sunday")
]
```

### Defalut Value

```renpy
# pressing the hold button will increase the time of:
define DEFAULT_WAIT_HOUR = 1
# using the default new day function the time of the next day will be:
define DEFAULT_BLOCK_SPENDTIME_DIALOGUE = _("You can't do that now")
```

### Not recommended functions

This functions are not recommended because not update update olther variables conditioned by time.

So is consigliabile use the `label after_spending_time(is_check_event=False, is_check_routines=True)` after this functions.

I left the possibility of using them for those who want to follow in a python code.
Or to customize some possibilities.

#### New Day manualy

Procedure **not recommended**, use appropriate [label](#new-day).

**Tip**: use [**after_spending_time**](Methods-for-closing-a-label#jump-after_spending_time) at the end

```renpy
python:
    new_day()
```

#### New Houre manualy

Procedure **not recommended**, use appropriate [label](#wait).

**Tip**: use [**after_spending_time**](Methods-for-closing-a-label#jump-after_spending_time) at the end.

```renpy
python:
    new_hour(3)
```

## Block the spending time

For block the spending time you can use the flag `not_can_spend_time`:

You need to add the flag in the list of [Flags](https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags):

```renpy
# https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags
define flag_keys = [
    # Block all spend_time
    "not_can_spend_time",
]
```

For example:

```renpy
# to lock
$ set_flags("not_can_spend_time", False)
# to unlock
$ set_flags("not_can_spend_time", True)
```

## Image that changes based on the time period

You can use the `tm.timeslot_number` to change the image based on the time period.

`tm.timeslot_number` depends on the `timeslot_names` list. The first element of the list is 0, the second is 1, and so on.

exemple:

```renpy
define timeslot_names = [
    (2, _("Night")), # tm.timeslot_number = 0
    (8, _("Morning")), # tm.timeslot_number = 1
    (14, _("Afternoon")), # tm.timeslot_number = 2
    (20, _("Evening")), # tm.timeslot_number = 3
]

image bg annroom = "location/garden-[tm.timeslot_number].webp"
```

![Screenshot 2023-10-21 120727](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/b1a59377-0878-45ea-9a60-f429de0576b3)

![Screenshot 2023-10-21 120807](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/9338dd31-4f03-4461-9e15-c89af0cbfb20)
