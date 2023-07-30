label start:

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    

    $ allow_skipping = True
    $ config.allow_skipping = True

    show natsuki turned at t11
    s_name "djfkjfgdjgdkfjgkdjlgdjlgkdfjlgjdflgkj"
