# Methods for closing a label

It is very important to understand how to close labels: to avoid ending the game prematurely, apply the most suitable backgrounds, controls on events...

## return

Return is the **recommended method in basic cases**.

**IMPORTANT**: it should not be used after a Jump otherwise it will cause the **game to end**.

**Pros**:

- Performance
- Will not start any [Closed Room](Navigation-and-Map#closed-room)
- Does are the basic controls: custom here `after_return_from_room_navigation`

**Cons**:

- Cannot be used after Jump
- Will not start any [Event](Routine-system#events)

## call screen room_navigation

Use it in case you don't want to use the selected background later and don't know want any kind of event.

```renpy
call screen room_navigation
```

**Pros**:

- Performance
- Can be used after Jump

**Cons**:

- Does not change the last background used
- **Not do any search to see if anything has been changed** in the meantime
- Will not start any [Event](Routine-system#events)
- Will not start any [Closed Room](Navigation-and-Map#closed-room)

## Add more controls

to add more controls you can use:

```renpy
call after_spending_time
```

```renpy
call change_room
```

in addition to the previous methods
