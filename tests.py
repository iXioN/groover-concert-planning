import unittest
from concert_prog import is_programation_possible


class IsProgrammationPossibleTests(unittest.TestCase):
    def test_track_len_sum_lower_than_concert_premier(self):
        """
        given a list of 3 length where sum is lower than the concert_premiere_length
        when I call is_programation_possible with this list and concert_premiere_length
        Then i get a True
        """
        concert_premiere_length = 7
        track_lenght = (1, 2, 3)
        is_possible = is_programation_possible(concert_premiere_length, track_lenght)
        self.assertTrue(is_possible)

    def test_track_len_sum_equal_to_concert_premier(self):
        """
        given a list of 3 length where sum is equals to concert_premiere_length
        when I call is_programation_possible with this list and concert_premiere_length
        Then i get a True
        """
        concert_premiere_length = 6
        track_lenght = (1, 2, 3)
        is_possible = is_programation_possible(concert_premiere_length, track_lenght)
        self.assertTrue(is_possible)

    def test_smallest_track_len_is_bigger_to_concert_premier(self):
        """
        given a list of 4 length where the smallest length is bigger than the concert_premiere_length
        when I call is_programation_possible with this list and concert_premiere_length
        Then i get a True
        """
        concert_premiere_length = 6
        track_lenght = (8, 9, 10, 11)
        is_possible = is_programation_possible(concert_premiere_length, track_lenght)
        self.assertFalse(is_possible)


if __name__ == "__main__":
    unittest.main()
