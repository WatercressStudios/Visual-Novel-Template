init python:

    mr = MusicRoom(fadeout=1.0)
    

    # mr.add("music/Ambivalence.ogg", always_unlocked=True)
    # mr.add("music/Beautiful-Dreamer.ogg", always_unlocked=True)
    # mr.add("music/Budapest.ogg", always_unlocked=True)
    # mr.add("music/Budapest original.ogg", always_unlocked=True)
    # mr.add("music/Colorless-Aura.ogg", always_unlocked=True)
    # mr.add("music/DataCube Loop.ogg", always_unlocked=True)
    # mr.add("music/Digital-Virulence.ogg", always_unlocked=True)
    # mr.add("music/Dream.ogg", always_unlocked=True)
    # mr.add("music/Glass Cockpit.ogg", always_unlocked=True)
    # mr.add("music/Glass Cockpit REDUX.ogg", always_unlocked=True)
    # mr.add("music/Scene3.ogg", always_unlocked=True)
    # mr.add("music/Scene3.ogg", always_unlocked=True)
    # mr.add("music/Lights.ogg", always_unlocked=True)
    # mr.add("music/Meteorstorm.ogg", always_unlocked=True)
    # mr.add("music/Overture.ogg", always_unlocked=True)
    # mr.add("music/Promises-to-Keep.ogg", always_unlocked=True)
    # mr.add("music/Stasis.ogg", always_unlocked=True)
    # mr.add ("music/Ode To Joy.ogg", always_unlocked=True)


screen music_room:
    # variant "android"
    tag menu

    # The background of the game menu.
    window:
        style "gm_root"

    frame:
        style_group "gm_nav"
        xalign 0.02
        yalign 0.02
        has vbox
        spacing 3
        textbutton "Ambivalence" action mr.Play("music/Ambivalence.ogg") text_size 46
        textbutton "Beautiful Dreamer" action mr.Play("music/Beautiful-Dreamer.ogg") text_size 46
        textbutton "Budapest" action mr.Play("music/Budapest.ogg") text_size 46
        textbutton "Budapest (Original)" action mr.Play("music/Budapest original.ogg") text_size 46
        textbutton "Colorless Aura" action mr.Play("music/Colorless-Aura.ogg") text_size 46
        textbutton "Datacube Loop" action mr.Play("music/DataCube Loop.ogg") text_size 46
        textbutton "Digital Virulence" action mr.Play("music/Digital-Virulence.ogg") text_size 46
        textbutton "Dream" action mr.Play("music/Dream.ogg") text_size 46

        
    frame:
        style_group "gm_nav"
        xalign 0.98
        yalign 0.02

        has vbox
        spacing 3
        textbutton "Glass Cockpit" action mr.Play("music/Glass Cockpit.ogg") text_size 46
        textbutton "Glass Cockpit (Redux)" action mr.Play("music/Glass Cockpit REDUX.ogg") text_size 46
        textbutton "Glass Cockpit (Alternate)" action mr.Play("music/Scene3.ogg") text_size 46
        textbutton "Lights" action mr.Play("music/Lights.ogg") text_size 46
        textbutton "Meteor Storm" action mr.Play("music/Meteorstorm.ogg") text_size 46
        textbutton "Overture" action mr.Play("music/Overture.ogg") text_size 46
        textbutton "Promises to Keep" action mr.Play("music/Promises-to-Keep.ogg") text_size 46
        textbutton "Stasis" action mr.Play("music/Stasis.ogg") text_size 46


    # Buttons that let the user advance tracks and stop music.
    frame:
        style_group "mm"
        xalign 0.5
        yalign 0.96

        has hbox
        textbutton _("Return") action Return() text_size 41
        textbutton "Next" action mr.Next() text_size 41
        textbutton "Stop" action mr.Stop() text_size 41
        textbutton "Previous" action mr.Previous() text_size 41

    # The buttons that lets the user enter Preferences and exit the jukebox.
    # frame:
    #     style_group "gm_nav"
    #     xalign 0.02
    #     yalign 0.96

    #     has vbox

    #     textbutton _("Return") action Return() text_size 40

    # Stops main menu music playing upon entry to the jukebox.
    on "replace" action mr.Stop()

    # Restores the main menu music upon leaving.
    on "replaced" action Play("music", "music/Ode To Joy.ogg")
