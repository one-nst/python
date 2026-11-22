class Television:

    """Television with power, channel, volume, and mute controls."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3



    def __init__(self) -> None:

        """Initialize the television's state for power, mute, channel and volume."""

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL



    def power(self) -> None:

        """Power the television on or off."""

        self.__status = not self.__status



    def mute(self) -> None:

        """Mute or unmute the television if powered on."""

        if self.__status:
            self.__muted = not self.__muted



    def channel_up(self) -> None:

        """Increase channel by one if the tv is on, go to beginning after last channel."""

        if self.__status:

            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

            else:
                self.__channel += 1




    def channel_down(self) -> None:

        """Decrease channel by one if the tv is on, go to end before first channel."""

        if self.__status:

            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

            else:
                self.__channel -= 1




    def volume_up(self) -> None:

        """Increase volume by one if the tv is on, unmute if muted and stop at highest volume."""

        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1





    def volume_down(self) -> None:

        """Decrease volume by one if the tv is on, unmute if muted and stop at lowest volume."""

        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1





    def __str__(self) -> str:

        """Return a formatted string showing status of power, channel, and current volume."""

        if self.__muted:
            display_volume = Television.MIN_VOLUME
        else:
            display_volume = self.__volume

        return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}")