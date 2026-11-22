import pytest
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

    # Turn on TV, increase volume once, then mute
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #unmute TV when it is on
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


    # Turn off TV and mute
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

    # unmute while TV is off
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"








def test_channel_up():
    tv = Television()

    # TV is off, channel won't change
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # TV is on and channel goes up
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    #TV is on and channel goes to 0 after last one
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"





def test_channel_down():

    tv = Television()

    # TV is off, channel won't change
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #TV is on and channel goes to 3 before first one
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    # TV is on and channel goes down
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"








def test_volume_up():
    tv = Television()


    # TV is off, volume won't change
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # TV is on, volume increased by one
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # TV is on, then muted, then volume increase
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    #TV is on and volume stops at max
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"





def test_volume_down():
    tv = Television()


    # TV is off, volume won't change
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # TV is on, volume increase to max and decrease by one
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    # TV is on, then muted, then volume decrease by one
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # TV is on, volume stops at minimum
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
