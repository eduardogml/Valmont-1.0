# Conversation system

![Screenshot 2023-10-21 120118](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/b285da01-960b-4a0c-b05b-44c31e34a409)

The Talk system is related to routines. As explained in [Routine system](Routine-system) the [Conversation()](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/conversation.py) classes are used to customize the dialogues.

This class extend ( have all properties and methods of ) Button class, is very important read the [NQTR Button wiki](Button).

```python
Conversation(name = "talk_sleep", characters=a, label_name = "talk_sleep")
Conversation(name = "talk", characters=[a, mc], conversation_background = None)
Conversation(name = "talk_alice_terrace", characters=a, conversation_background = "bg alice terrace talk")
```

The property `characters` can be a [Ren'Py Character](https://www.renpy.org/doc/html/dialogue.html#Character) or a list of [Ren'Py Character](https://www.renpy.org/doc/html/dialogue.html#Character).

`characters` is most important property of Conversation class, because it is used to know where the character is. So set a correct icon of character and in case of you use a [Default conversation label](#default-conversation-label) is used to know the character to talk to.

For add the ***icon of character*** you must use the [Character Properties Method](https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Character-Properties-Method).

---

**[The group conversations or group routines is in development](https://github.com/DRincs-Productions/NQTR-System/issues/30)**

---

## Your conversation label

Is a easy solution for create a conversation label. For use it you must set `label_name` = `your_label_name`.

Read this for know how to close a label: [Methods for closing a label](Methods-for-closing-a-label)

## Default conversation label

---

If you want to use a similar system to the default conversation label, I recommend read the [My recommendation method](#my-recommendation-method) section

---

Default conversation label is a NQTR label.

For use it you must set `label_name` to `None` or not set it, so the `nqtr_talk` label will be started.

This label works in following way:

* get a first character of `characters` property
* set `current_conversation_character` to this character
* check if in the `conversations` dictionary there is a key == character
* and add all choices of this character and the choice `Back`

### Add an Talk Choice

(**code-snippets**: `DR_TalkChoiceAdd`)

```renpy
python:
    add_conversation_choice(choice_character = character_name, choice_text = _("Name"), label_name = "label_be_started")
```

### Delete an Action

(**code-snippets**: `DR_TalkChoiceDel`)

```renpy
python:
    del_conversation_choice(choice_character = character_name, choice_text = _("Name"))
```

### Custom conversation end

If you want to add phrase when the conversation ends or run a code, you can use the label `talk_back_custom`.

For example:

```renpy
# Display a random phrase and then end the conversation
label talk_back_custom:
    $ num = renpy.random.randint(1, 7)
    if num == 1:
        mc "OK, I'm off. See you."
    elif num == 2:
        mc "It's getting late. See you."
    elif num == 3:
        mc "Sorry, but I have to go now. Bye."
    elif num == 4:
        mc "Good talk. We should do this more often."
    elif num == 5:
        mc "I just remembered something. Gotta go! Bye."
    elif num == 6:
        mc "I won't keep you any longer. Bye."
    elif num == 7:
        mc "I was supposed to tell you something else.... But I can't remember."
        mc "When it comes back to me I'll let you know, bye."

    $ del num
    return
```

### My recommendation method

My recommendation method is to join the two methods: [Your conversation label](#your-conversation-label) and [Default conversation label](#default-conversation-label).

For do this you can use the `label_name` property = `your_label_name`

exemple:

```renpy
Conversation(name = "talk_alice", characters=alice, conversation_background = None, label_name = "your_label_name")
```

In `your_label_name` you can use the `current_conversation_character` variable for know the character to talk to. And you can use [Add an Talk Choice](#add-an-talk-choice) and [Delete an Action](#delete-an-action) methods for add or delete choices.

And in label end call the `nqtr_talk` label.

exemple:

```renpy
label your_label_name:
    if current_conversation_character == alice:
        # you can add a if for check location or time
        # Add an Talk Choice
        $ add_conversation_choice(choice_character = alice, choice_text = _("Name"), label_name = "label_be_started")
    call nqtr_talk
    return
```

nqtr_talk make the rest of work. And if [Custom conversation end](#custom-conversation-end) is set, it will be called.

So for clean the chioce in the end of conversation you must create a label [Custom conversation end](#custom-conversation-end) were you delete the choice.

exemple:

```renpy
label talk_back_custom:
    $ del_conversation_choice(choice_character = alice, choice_text = _("Name"))
    return
```

## Conversation with Picture in background

![Screenshot 2023-10-21 115715](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/923e986a-775e-4f32-9871-c6221985b4a2)

With to the "[Picture in Background](Button#picture-in-background)" option you can add conversations not on the right but in an x, y position of your preference. Read more here: [Picture in Background](Button#picture-in-background)

## Constants

```python
DEFAULT_LABEL_TALK = "nqtr_talk"
```

`DEFAULT_LABEL_TALK`: in case `label_name` is not set this label will be started
