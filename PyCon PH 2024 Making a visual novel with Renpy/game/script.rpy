# code for title taken from:
#  https://lemmasoft.renai.us/forums/viewtopic.php?p=227207#p227207

define header = Character(None,
    #what_font = "BOOKOS.TTF", 
    what_color = "ffffff",
    what_size = 40, 
    what_drop_shadow = (2, 2,),
    what_xpos = 0.5,
    what_ypos = 0.5,
    what_xalign = 0.5,
    what_yalign = 0.5,
    what_text_align = 0.5,
    what_xsize = 1.0,
    window_padding = (0.1, 0),
    window_ypos = 0.3,
)

define text = Character(None, 
    #what_font = "BOOKOS.TTF", 
    what_color = "ffffff",
    what_size = 40, 
    what_drop_shadow = (2, 2,),
    what_xpos = 0.5,
    what_ypos = 0.1,
    what_xalign = 0.5,
    what_text_align = 0.5,
    what_xsize = 1.0,
    window_padding = (0.1, 0),
    window_ypos = 0.95,
)

define text_center = Character(None, 
    #what_font = "BOOKOS.TTF", 
    what_color = "ffffff",
    what_size = 40, 
    what_drop_shadow = (2, 2,),
    what_xpos = 0.5,
    what_ypos = 0.5,
    what_xalign = 0.5,
    what_yalign = 0.5,
    what_text_align = 0.5,
    what_xsize = 1.0,
    window_padding = (0.1, 0),
    window_ypos = 0.75,
)

image title = ParameterizedText(
    what_size = 40,
    xalign = 0.5,
    yalign = 0.05,
    textalign = 0.5,
)

define n = Character(None, kind=nvl,
    font = "Arial",
    what_size = 40,
)

define n_header = Character(None, kind=nvl,
    font = "Candara",
    what_size = 50,
    what_bold = True,
    what_outlinecolor = "#00ff00",
    what_xalign = .5,
    what_text_align = .5,
)

init python:
    gui.nvl_text_xpos = 80
    gui.nvl_text_width = 0.9

    # spacing between text
    gui.nvl_height = None
    gui.nvl_spacing = 10

    # text outline
    gui.dialogue_text_outlines = [
        (3, "#000000", 2, 2)      # parameters = (Stroke/Outline width, Color, X offset, Y offset)
    ]

init:
    style nvl_window:
        background None

label start:
    scene bg pexels-felix-mittermeier-956999

    call prelude

    scene bg pexels-frank-cone-3607542 with fade:
        matrixcolor TintMatrix("#7FA5F2")

    call intro
    call examples
    call what_is_renpy

    scene bg pexels-felix-mittermeier-956999 with pixellate

    header "Let's learn Ren'Py"

    call surprise
    call end
    return

label prelude:
    scene bg pexels-felix-mittermeier-956999
    header "{size=+20}Make a Visual Novel with Ren'py{/size}\n{b}Workshop{/b} by Sony Valdez{fast}"

    show title "PRELUDE"
    text "The speaker, MrValdez is a person that doesn’t exists. At least, not in this universe.\n\nThis is the only time Sony Valdez will acknowledge that none of the following bio is real."

    show title "MrValdez lore\n(1/3)"
    show prelude_1:
        xalign 0.15 yalign 0.18
    show prelude_2:
        xalign 1-0.15 yalign 0.42
    text "MrValdez is a Luchador in a universe that is like our own.\n\n While Luchadores are known for physical wrestling, MrValdez came from a world where they perform as programmers."

    hide prelude_1
    hide prelude_2

    show title "MrValdez lore\n(2/3)"
    show prelude_3:
        xalign .5 yalign 0.5
    text "Having accidentally transported here by a strange Python program, MrValdez hopes to one day return to his reality."

    hide prelude_3

    show title "MrValdez lore\n(3/3)"
    show prelude_4:
        xalign 0.15 yalign 0.4
    show prelude_5:
        xalign 1-0.15 yalign 0.4
    text "In the meantime, he spends his time sharing secrets from his universe. By complete coincidence, that knowledge is applicable in this universe."

    hide prelude_4
    hide prelude_5
    hide title
    return

label intro:
    header "{size=+20}Make a Visual Novel with Ren'py{/size}\n{b}Workshop{/b} by {s}Sony{/s} MrValdez{fast}"

    n "Hi. I'm MrValdez. Gamer. Programmer. Mostly harmless."
    n "I teach Python and I'm one of the founders of Python Philippines."
    n "I use Ren'Py to teach simple programming\n and how to do project management to non-programmers"
    n "In this workshop, I will teach you how to make a simple Visual novel game."
    n "We will not be using live2d, animation system, movies playback, and audio system."
    n "For those who have Ren'Py installed,\n at the end of this workshop, you would have created a simple game."
    n "For those who don't have Ren'Py installed,\n try to download from {u}https://renpy.org/latest.html{/u}"

    nvl clear

    n_header "What are Visual Novels?{fast}{nw}"

    n "These are games focused on stories with multiple branching paths."
    n "Most of the gameplay is just reading... literally like reading a novel!"
    n "Some high production Visual novels have voice acting."
    n "The popular ones can sometimes become anime."
    n "There are different story genres such as {i}Romance{/i}, {i}Action{/i}, {i}Mystery{/i}, and {i}Horror{/i}."
    n "Some Visual novels even combine different game genres!"
    n "Let me demo the vn that is included with Ren'py."

    return

label examples:
    nvl clear

    n_header "8 Visual Novel examples{fast}{nw}"

    show steins gate onlayer overlay:
        zoom .48
        xalign 0.5 ypos 150

    n "\n\n\n\n\n\n\n\n\n\n\n\n\n\n1. Steins;Gate (mystery story that has been adopted into anime){fast}"

    nvl clear
    n_header "8 Visual Novel examples{fast}{nw}"

    show long live the queen onlayer overlay:
        zoom 1.8
        xalign 0.5 ypos 150

    n "\n\n\n\n\n\n\n\n\n\n\n\n\n\n2. Long Live The Queen (Simulation game){fast}"

    nvl clear
    n_header "8 Visual Novel examples{fast}{nw}"

    show the yahwg onlayer overlay:
        zoom 0.8
        xalign 0.5 ypos 150

    n "\n\n\n\n\n\n\n\n\n\n\n\n\n\n3. The Yawhg (one hour 1-4 players rpg about the world ending){fast}"

    nvl clear
    n_header "8 Visual Novel examples{fast}{nw}"

    show phoenix wright onlayer overlay:
        zoom .48
        xalign 0.5 ypos 150

    n "\n\n\n\n\n\n\n\n\n\n\n\n\n\n4. Phoenix Wright (court room puzzle drama){fast}"

    nvl clear
    n_header "8 Visual Novel examples{fast}{nw}"

    show persona 4 onlayer overlay:
        zoom .48
        xalign 0.5 ypos 150

    n "\n\n\n\n\n\n\n\n\n\n\n\n\n\n5. Persona 4 Golden (dungeon rpg with Visual novel elements){fast}"

    nvl clear
    n_header "8 Visual Novel examples{fast}{nw}"

    show melty blood onlayer overlay:
        zoom .55
        xalign 0.5 ypos 150

    n "\n\n\n\n\n\n\n\n\n\n\n\n\n\n6. Melty Blood (a shonen Visual novel combined with a fighting game){fast}"

    nvl clear
    n_header "8 Visual Novel examples{fast}{nw}"

    show the letter onlayer overlay:
        zoom .5
        xalign 0.5 ypos 150

    n "\n\n\n\n\n\n\n\n\n\n\n\n\n\n7. The Letter (horror Visual Novel from the Philippines){fast}"

    nvl clear
    n_header "8 Visual Novel examples{fast}{nw}"

    show doki doki onlayer overlay:
        zoom .5
        xalign 0.5 ypos 150

    n "\n\n\n\n\n\n\n\n\n\n\n\n\n\n8. Doki Doki Literature Club\n {i}Warning: This game is not suitable for children or those who are easily disturbed.{/i}{fast}"

    return

label what_is_renpy:
    nvl clear

    n_header "What is Ren'Py?{nw}"

    show renpy onlayer overlay:
        zoom 1.7
        xalign 0.8 yalign 0.7
    show runs_on onlayer overlay:
        zoom 1.5
        xalign 0.2 yalign 0.7

    n "Ren'py is a game engine built on top of pygame and Python.\n\nIt is used to make visual novels.\nIt is designed to be usable by non-programmers\n\nhttps://www.renpy.org/"

    nvl clear

    n_header "What is Ren'Py?{nw}"

    show renpy onlayer overlay:
        zoom 1.7
        xalign 0.8 yalign 0.7

    show pygame onlayer overlay:
        xalign 0.2 yalign 0.7

    n "Programmers can access Python and pygame to do advanced stuff like create minigames and connecting to the Internet\n\nA lot of ren'py visual novels are sold in itch.io, Steam, Google Play Store, and Apple's App Store"

    show renpy onlayer overlay:
        zoom 1.7
        xalign 0.8 yalign 0.7

    show pygame onlayer overlay:
        xalign 0.2 yalign 0.7

    n "Still under active development! Because of {i}Doki Doki Literature{/i}'s success, Ren'Py games are being ported to Video Game Consoles by 3rd party services."

    nvl clear

    return

label surprise:
    nvl clear

    text "Now for a surprise on this presentation.{fast}"
    text "This slide show is actually built on {fast}Ren'Py!"

    show prelude_1 at right:
        zoom 1
        yalign 0.3
        xzoom -1
    show hero bark:
        xzoom -1
        yalign 0.5
    show alex cry at right:
        xalign 0.5 yalign 0.4
        zoom 1.3

    text "Surprise!{fast}"

    hide prelude_1
    hide hero
    hide alex

    show title "Thank you"

    text "I will be sharing the source code. So if you are interested\nin looking at how I made a visual novel presentation,\nyou can study how I did it"

    text "I hope one day, I'll be able to play your game in the future. And maybe, see you give a presentation on a future PyCon."

    hide title
    return

label end:
    nvl clear
    n_header "Resources{nw}"

    n "{b}You can find the source code for this presentation at:{/b}\n - https://github.com/MrValdez/pycon-ph-2024-renpy-workshop{fast}{nw}"

    n "{b}You can find me on twitter:{/b}\n - https://twitter.com/MrValdez{fast}{nw}"
    
    n "{b}You can find more of Richel Valdez's art at her Instagram:{/b}\n - raravaldez {fast}{nw}"
    
    n "{b}For something completely different, a game created by my brother{/b}:\n - https://goodknightgame.com/{fast}"

    show hero and alex onlayer overlay:
        zoom 1.7
        xalign 0.98 yalign 0.5

    text "Any questions?"

    return