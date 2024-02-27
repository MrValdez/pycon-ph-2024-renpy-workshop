define me = Character("MrValdez")
define villain = Character("A snake")

# visual novel: flags
default is_brave = True

label start:
    scene bg meadow

    $ name = renpy.input("What is your name? ")

    "Hello, [name]"

    show me happy at left

    me "I am MrValdez"

    #scene bg uni with fade
    scene bg uni with pixellate
    show me surprised at truecenter with move

    me "Nice to meet you"

    show villain at right with moveinbottom

    villain "BOOO!"
    with vpunch

    menu:
        "I am hungry":
            #jump hungry_ending
            call hungry_ending
        "I am afraid":
            #jump afraid_ending
            call afraid_ending
        "I am not afraid" if is_brave:
            "I AM NOT AFRAID"

    jump credits

label hungry_ending:
    "Poor doggo is hungry"
    return
    # jump credits

label afraid_ending:
    "Poor doggo is afraid"
    # jump credits

label credits:
    "Designed by committee"


