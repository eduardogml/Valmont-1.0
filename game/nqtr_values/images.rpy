image bg valmont_campus = "location/valmont-campus-[tm.timeslot_number].webp"

# locations
image pre map west_wing_campus = Transform("images/location/campus-ala-oeste2.webp", xysize=(gui.sprite_size, gui.sprite_size))
image icon map west_wing_campus = LayeredImageMask("pre map west_wing_campus",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
image pre map male_dorm = Transform("images/location/male-dorm.webp", xysize=(gui.sprite_size, gui.sprite_size))
image icon map male_dorm = LayeredImageMask("pre map male_dorm",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)