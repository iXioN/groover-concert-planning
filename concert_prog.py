# concert lenght in minutes
from typing import FrozenSet, Iterable, Generator, Iterator, List, Tuple, Union

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


def is_programation_possible(
    concert_premiere_length: int, track_lenghts: Iterable[int]
) -> bool:
    
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

    for possible_tracks in combinations(track_lenghts, MAXIMUM_NUMBER_OF_TRACKS):
        # do the sum and verify the computation
        if sum(possible_tracks) == concert_premiere_length:
            return True
    return False
