# this one is a good presentation for the quick sort
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quick_sort(arr, l, r):
            # when the length of the array is 1 or 0, return
            if l >= r:
                return

            # set the first element as the sentinel
            i, j = l, r
            while i < j:
                # find the j smaller than the sentinel from the right
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                # find the i bigger than the sentinel from the left
                while i < j and arr[i] <= arr[l]:
                    i += 1
                # swap the two elements
                arr[i], arr[j] = arr[j], arr[i]
            # swap the sentinel with the element in the middle
            # after that the left part is smaller than the sentinel and the right part is bigger than the sentinel
            arr[l], arr[i] = arr[i], arr[l]
            # iterate the left part and the right part
            quick_sort(arr, l, i - 1)
            quick_sort(arr, i + 1, r)

        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]


# we can optimize it, cause we only return the first k smaller elements
# so when the i-1 - l + 1 == k, we can return the result
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # the special case
        if k >= len(arr):
            return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            # if k < i, keep sorting the left part
            if k < i:
                return quick_sort(l, i - 1)
            # if k > i, keep sorting the right part
            if k > i:
                return quick_sort(i + 1, r)
            # if k == i, return the result
            return arr[:k]

        return quick_sort(0, len(arr) - 1)
