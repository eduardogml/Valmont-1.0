# Wiki

## Implementation steps

Important: Read all [Renpy Utility Lib Wiki](https://github.com/DRincs-Productions/renpy-utility-lib/wiki) before start. This is a dependency of NQTR Toolkit.

For show the room_navigation in your `game/script.rpy` file, add this line:

```renpy
label start:
    # ...

    # Renpy Utility Lib Wiki
    # enable a notify screen
    call enable_notifyEx

    # NQTR Toolkit
    # the first time it opens room navigation screen use after_spending_time
    # for update routine, event...
    call after_spending_time
    # open the room navigation screen
    call screen room_navigation
```

1. [Navigation and Map](Navigation-and-Map)
2. [Time system](Time-system)
3. [Action](Action) & read [Methods for closing a label](https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Methods-for-closing-a-label)
4. [Routine](https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system) & Read [Talk system](Conversation-system) & [Events](https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#events).
5. [Quest system](Quest)
6. [Screens](Screens)

## Install & Migrations

Insert Toolkit in your project: <https://github.com/DRincs-Productions/NQTR-System#install-lts-version>

Challog & Migrations: <https://github.com/DRincs-Productions/NQTR-System/blob/main/CHANGELOG.md>
