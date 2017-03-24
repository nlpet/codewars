u"""
Pick Peaks

In this kata, you will create an object that returns the positions and the values
of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [ 0 , 1 , 2 , 5 , 1 , 0 ] has a peak in position
3 with a value of 5 (arr[3] = 5)

The output will be returned as an object with two properties: pos and peaks.
Both of these properties should be arrays. If there is no peak in the given
array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3,2,3,6,4,1,2,3,2,1,2,3]) returns {pos:[3,7],peaks:[6,3]}

All input arrays will be valid numeric arrays (although it could still be empty),
so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the
context of a mathematical function, we don't know what is after and before and
therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1,2,2,2,1] has a peak while [1, 2, 2, 2, 3] does not.
In case of a plateau-peak, please only return the position and value of the
beginning of the plateau. For example: pickPeaks([1,2,2,2,1]) returns {pos:[1],peaks:[2]}
"""
import sys

sys.path.append('..')
from helpers.test_wrapper import Test


def pick_peaks(array):
    pos, peaks = [], []
    start, peak = None, None
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            start = i - 1
            peak = i
        elif array[i - 1] > array[i]:
            if start is not None:
                pos.append(peak)
                peaks.append(array[peak])
                peak = None
                start = None

    return dict(zip(['pos', 'peaks'], [pos, peaks]))


def run_tests():
    with Test() as test:
        test.it('should support finding peaks')
        test.assert_equals(
            pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})

        test.it('should support finding peaks, but should ignore peaks on the edge of the array')
        test.assert_equals(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {
                           "pos": [3, 7], "peaks": [6, 3]})

        test.it('should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau')
        test.assert_equals(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {
                           "pos": [3, 7, 10], "peaks": [6, 3, 2]})

        test.it('should support finding peaks; if the peak is a plateau, it should only return the position of the first element of the plateau')
        test.assert_equals(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {
                           "pos": [2, 4], "peaks": [3, 2]})

        test.it('should support finding peaks, but should ignore peaks on the edge of the array')
        test.assert_equals(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})

        test.it('should work on random inputs')
        test.assert_equals(pick_peaks([0, 11, -2, -1, 19, 20]), {"pos": [1], "peaks": [11]})



if __name__ == '__main__':
    run_tests()
