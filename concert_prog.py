# concert lenght in minutes
from typing import Iterable


MAXIMUM_NUMBER_OF_TRACKS = 3


def is_programation_possible(
    concert_premiere_length: int, track_lenght: Iterable[int]
) -> bool:
    # quicky check the sum of track_lenght
    total_track_lenght = sum(track_lenght)
    if total_track_lenght <= concert_premiere_length:
        return True

    return False
