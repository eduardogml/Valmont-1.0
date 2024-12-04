define timeslot_names = [
    (6, _("Dawn")),
    (7, _("Day")),
    (17, _("Dusk")),
    (19, _("Night")),
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
    hour_of_new_day = 6,
    hour = 6,
    weekday_weekend_begins = 6,
    day = 0,
    timeslot_names = timeslot_names,
    weekday_names = weekday_names
)
