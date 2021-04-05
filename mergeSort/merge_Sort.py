#Python practicing for implementing MERGE SORT

class MergeSort(object):
    def __init__(self,numbers):
        self.values = numbers
        self.count = len(numbers)

    def sort(self):
        self.mergeSort(0, self.count - 1)
        return self.values

    def mergeSort(self, low, high):
        if low < high:
            mid = (low + high) // 2

            self.mergeSort(low,mid)
            self.mergeSort(mid+1, high)
            self.merge(low,mid,high)

    def merge(self, low, mid, high):
        arr1 = []
        i = low
        j = mid +1

        while i <= mid and j<= high:
            if self.values[i] <= self.values[j]:
                arr1.append(self.values[i])
                i += 1
            else:
                arr1.append(self.values[j])
                j += 1

        while j <= high:
            arr1.append(self.values[j])
            j += 1

        for index, val in enumerate(arr1):
            self.values[low + index] = val