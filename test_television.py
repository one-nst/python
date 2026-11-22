from television import Television


def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    tv = Television()
    # Off and unmuted -> mute has no effect
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # Turn on, increase volume once, then mute
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Unmute while on
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # Turn off while unmuted, mute while off, then turn back on
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_channel_up():
    tv = Television()
    # Off -> channel_up has no effect
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # On -> increase channel
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    # Past MAX_CHANNEL (3) -> wraps to MIN_CHANNEL (0)
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    tv = Television()
    # Off -> channel_down has no effect
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # On at MIN_CHANNEL (0) -> wraps to MAX_CHANNEL (3)
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    # Decrease normally from 3 to 2
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"


def test_volume_up():
    tv = Television()
    # Off -> volume_up has no effect
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # On -> increase volume
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # On, muted, volume_up -> unmutes and increases volume
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Past MAX_VOLUME (2) -> stays at 2
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    tv = Television()
    # Off -> volume_down has no effect
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # On, increase to max (2), then decrease to 1
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # On, muted, volume_down -> unmutes and decreases volume
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Past MIN_VOLUME (0) -> stays at 0
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"