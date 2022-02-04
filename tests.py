import unittest
from concert_prog import is_programation_possible, combinations


class CombinationsTests(unittest.TestCase):
    def test_combination(self):
        """
        given a list of items
        when i call the combinations function with items and ask for 2 items combination
        then i get a list of all possible permutations af 2 values
        """
        items = (
            "A",
            "B",
            "C",
        )
        all_combinations = set(combinations(items, 2))
        possible_combination = set((("A", "B"), ("A", "C"), ("B", "C")))
        # both sets should be equals
        self.assertEqual(all_combinations, possible_combination)

    def test_combination_are_uniques(self):
        """
        given a list of 2 items
        when i call the combinations function with items and ask for 2 items combination
        then i get a list of 1 possible combination because diplicate are not possible in this implementation
        """
        items = (
            "A",
            "B",
        )
        all_combinations = set(combinations(items, 2))
        self.assertEqual(len(all_combinations), 1)


class IsProgrammationPossibleTests(unittest.TestCase):
    def test_track_len_sum_lower_than_concert_premier(self):
        """
        given a list of 3 length where sum is lower than the concert_premiere_length
        when I call is_programation_possible with this list and concert_premiere_length
        Then i get a True
        """
        concert_premiere_length = 7
        track_lenghts = (1, 2, 3)
        is_possible = is_programation_possible(concert_premiere_length, track_lenghts)
        self.assertTrue(is_possible)

    def test_track_len_sum_equal_to_concert_premier(self):
        """
        given a list of 3 length where sum is equals to concert_premiere_length
        when I call is_programation_possible with this list and concert_premiere_length
        Then i get a True
        """
        concert_premiere_length = 6
        track_lenghts = (1, 2, 3)
        is_possible = is_programation_possible(concert_premiere_length, track_lenghts)
        self.assertTrue(is_possible)

    def test_smallest_track_len_is_bigger_to_concert_premier(self):
        """
        given a list of 4 length where the smallest length is bigger than the concert_premiere_length
        when I call is_programation_possible with this list and concert_premiere_length
        Then i get a True
        """
        concert_premiere_length = 6
        track_lenghts = (8, 9, 10, 11)
        is_possible = is_programation_possible(concert_premiere_length, track_lenghts)
        self.assertFalse(is_possible)

    def test_tracks_fit_the_programation(self):
        """
        given a list of 4 length where the sum of 3 of them are equal to the concert_premiere_length
        when I call is_programation_possible with this list and concert_premiere_length
        Then i get a True
        """
        concert_premiere_length = 9
        track_lenghts = (2, 5, 6, 7, 3, 4, 8)
        is_possible = is_programation_possible(concert_premiere_length, track_lenghts)
        self.assertTrue(is_possible)


if __name__ == "__main__":
    unittest.main()
