# concert lenght in minutes
from typing import FrozenSet, Generator, Iterable, Iterator, List, Tuple, Union

MAXIMUM_NUMBER_OF_TRACKS = 3


def combinations(items: Union[List, Tuple], n: int) -> Iterator[Tuple[int]]:
    """
    A generator that yield all the UNIQUE combination items with n elements
    Args:
        items (list or tuple): The sequence of item to combine
        n (int): The length of elements that will be present in the returned subsequences

    Yields:
        Iterator[Tuple[int]]: n lenght subsequences of elements combined from items
    """
    if n == 0:
        yield tuple()
    else:
        for i in range(len(items)):
            for sub in combinations(items[i + 1 :], n - 1):
                item = items[i]
                item = [item] if isinstance(item, int) else item
                yield tuple(item) + sub


def _is_programation_possible_for_number_of_track(
    concert_premiere_length: int,
    track_lenghts: Iterable[int],
    max_number_of_tracks: int,
) -> bool:
    """
    a function that return a boolean depending if the programation is possible based on a possible number of tracks

    Args:
        concert_premiere_length (int): an integer that represent the time in minute of a concert premier
        track_lenghts (Iterable[int]): an iterable containing int that represent the track length in minutes
        max_number_of_tracks (int): the number of tracks to use in the permutation

    Returns:
        bool: is the programation possible
    """
    for possible_tracks in combinations(track_lenghts, max_number_of_tracks):
        # do the sum and verify the computation
        if sum(possible_tracks) == concert_premiere_length:
            return True
    return False


def is_programation_possible(
    concert_premiere_length: int,
    track_lenghts: Iterable[int],
    limit_number_of_tracks: bool = True,
) -> bool:
    """
    a function that return a boolean depending if the programation is possible based on a possible number of tracks

    Args:
        concert_premiere_length (int): an integer that represent the time in minute of a concert premier
        track_lenghts (Iterable[int]): an iterable containing int that represent the track length in minutes
        limit_number_of_tracks (int): do you want to use the number of track to MAXIMUM_NUMBER_OF_TRACKS

    Returns:
        bool: is the programation possible
    """
    # quicky check the sum of track_lenght
    total_track_lenght = sum(track_lenghts)
    # if the sum of tracks is lower than concert_premiere_length it ts impossible to fill the time
    if total_track_lenght < concert_premiere_length:
        return False
    # if by change the sum is exactly equals to the concert_premiere_length, bingo
    elif total_track_lenght == concert_premiere_length:
        return True

    # if the smallest track lenght is biggert than the concert_premiere_length, don't start start the combination and fail fast
    if min(track_lenghts) >= concert_premiere_length:
        return False

    # if limit_number_of_tracks is set to false, don't use the MAXIMUM_NUMBER_OF_TRACKS constant and try all the possible combination from 1 element to len(track_lenghts) possible combination
    if limit_number_of_tracks:
        return _is_programation_possible_for_number_of_track(
            concert_premiere_length, track_lenghts, MAXIMUM_NUMBER_OF_TRACKS
        )
    else:
        for number_of_tracks in range(1, len(track_lenghts)):
            match = _is_programation_possible_for_number_of_track(
                concert_premiere_length, track_lenghts, number_of_tracks
            )
            if match:
                return True
    return False
