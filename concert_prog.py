# concert lenght in minutes
from typing import FrozenSet, Iterable, Generator, Iterator, List, Tuple, Union

MAXIMUM_NUMBER_OF_TRACKS = 3


def combinations(items: Union[List, Tuple], n: int) -> Iterator[Tuple[int]]:
    """
    A generator that yield all the unique combination items with n elements
    Args:
        items (list or tuple): The sequence of item to combine
        n (int): The length of elements that will be present in the returned subsequences

    Yields:
        Iterator[List[int]]: n lenght subsequences of elements combined from items
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
    if total_track_lenght <= concert_premiere_length:
        return True

    for possible_tracks in combinations(track_lenghts, MAXIMUM_NUMBER_OF_TRACKS):
        print(possible_tracks)
        # do the sum and verify the computation
        if sum(possible_tracks) == concert_premiere_length:
            print("good tracks")
            print(possible_tracks)
            return True
    return False
