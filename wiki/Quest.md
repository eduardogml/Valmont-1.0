![Quest](https://github.com/DRincs-Productions/NQTR-System/assets/67595890/3d50034e-d2f4-46c5-9b56-bed00e17787f)

## Usage

**INFO**: For don't create problems if you not implement this in your project, the `quests` and `quest_stages` are defined by default empty, **but** their not save the changes.

For implement this you need to add this in your project:

```renpy
init python:
    from pythonpackages.nqtr.quest import Stage
    from pythonpackages.nqtr.quest import Quest

define quests = {
}
define quest_stages = {
}
```

## Quest

The [Quest class](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/quest.py#L187) is a set of stages, which follow each other in an orderly fashion.

### Add a Quest

(**code-snippets**: `DR_QuestAdd`)

```renpy
define quests = {
    "quest_id"  : Quest(id = "quest_id", title = _("Help [a]"), info_image ="quest quest_id",
        stage_ids = ["stages_id_1", "stages_id_2"],
        description = _("Long Description"),
        development = True
    ),
    "alice"     :   Quest(id = "alice", title = _("Help [a]"), info_image ="bg alice terrace talk", 
        stage_ids = ["talk alice1", "order products", "take products", "talk alice2"], 
        description = _("To learn more about how the repo works, Talk to [a]. \nGoing when she is there will automatically start an \"Event\" (see routine*.rpy to learn more). \nAfter that an action (action*.rpy) will be added to open the pc, in MC room. \n\n(during the quest you can talk to [a] and you will see her talking during the quests of the same Quest)")
    ),
    "ann"       :   Quest(id = "ann", title = _("Help [an]"), stage_ids = ["talk al about ann"], development = True),
}
```

### Start a Quest

(**code-snippets**: `DR_QuestStart`)

```renpy
python:
    quest_start(id = "quest_id")
```

### Next Stage

(**code-snippets**: `DR_QuestNextStage`)

This function is used to move to the next stage of a quest.

```renpy
python:
    quest_next_stage(id = "quest_id")
```

### Next Stage Only if is completed

(**code-snippets**: `DR_QuestNextStageIfCompleted`)

This function is used to move to the next stage of a quest only if the current stage is completed.

(in process)

```renpy
python:
    quest_next_stage_only_if_completed(id = "quest_id")
```

### If Number of Stages completed in Quest

(**code-snippets**: `DR_QuestIfNumberOfStagesCompleted`)

To check which stage number a Quest has arrived at:

```renpy
if (number_stages_completed_in_quest["alice"] == 2):
    # ...
```

### Set Days required to start

```renpy
python:
    quest_add_required_days_to_start(id = "quest_id", day = 2)
```

### Quest description

If you need a description of the quest that true over time, you need to add this in your project:

```renpy
default quests_descriptions = {
    # "quest_id"  : "description",
}
```

### Completing a quest

For complete a quest you need use [Next Stage](#next-stage) until the last stage.

#### Force completion of a quest

There is a way to force completion of a quest, that is to set the `number_stages_completed_in_quest["quest_id"]` to the last stage.

```renpy
python:
    ## -1 because the list starts at 0
    number_stages_completed_in_quest["quest_id"] = len(quests[cur_task_menu].stage_ids) - 1
```

#### Quest in development

If you want to show a message that the quest is in development, when the quest is completed, you can use the `development` parameter.

```renpy
define quests = {
    "ann"  : Quest(
        id = "ann",
        title = _("Help [an]"),
        info_image = None,
        stage_ids = ["talk al about ann", "take the key"], 
        description = _("Long Description"),
        development = True,
    ),
}
```

## Stage

The [Stage class](https://github.com/DRincs-Productions/NQTR-System/blob/main/pythonpackages/nqtr/quest.py#L56) is a class necessary for the proper functioning of a quest. (Quests are a list of Stages).

### Add a Stage

(**code-snippets**: `DR_QuestStageAdd`)

```renpy
define quest_stages = {
    # Quest "alice"
    "talk alice1"           :   Stage(idQuestOrTask = "alice", title = _("Talk [a]"), 
    description = _("Talk [a] on the terrace."), label_start="stagestart_talkalice"),
    "order products"        :   Stage(idQuestOrTask = "alice", title = _("Order products"), 
    description = _("Order the products with your PC.")),
    "take products"         :   Stage(idQuestOrTask = "alice", title = _("Take products"), 
    description = _("Take products on the Terrace."), 
    description_request = _("Wait for the products you ordered to arrive (2 day)"), 
    days_late = 2, label_start="add_product"),
    "talk alice2"           :   Stage(idQuestOrTask = "alice", title = _("Talk [a]"), description = _("Talk [a].")),
    # Quest "ann"
    "talk al about ann"     :   Stage(idQuestOrTask = "ann", title = _("Talk [a]"), description = _("Talk [a].")),
    "visit ann"             :   Stage(idQuestOrTask = "ann", title = _("Visit [an]"), 
    description = _("Go to the house of [an].")),
}
```

### find

(in process Goal)

## Task

They are identical to the Quests, except that after completion they are not replaced by the next one, but eliminated.

(in process)

## Goal

Goal class, it has been designed to be included in the Stage class.
To complete the goals use find()

(in process)

## Life cycle of a Quest

### First phase (Initialize a Stage)

```python
quest_start(id = "quest_id"):
    quest_stages["stage_id"].add_in_current_stages()
    current_quest_stages["quest_id"].start():
        # self = current_quest_stages["quest_id"]
        self.request_check():
            self.active = True
```

### Checking whether it is completed

```python
quest_next_stage_only_is_completed(id = "quest_id"):
    if current_quest_stages["quest_id"].is_completed():
        # self = quests["quest_id"]
        self.next_stage():
            self.after_next_stage():
                # here look for any errors by reporting them
                if: #if it's not the last quest:
                    self.start(number_stages_completed_in_quest[self.id] + 1) # Start the cycle again
```
