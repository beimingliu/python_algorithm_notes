# source: https://www.bilibili.com/video/av21540971/?p=31


def quick_sort(alist):
    """quick sort
    best: O(n)
    worst: O(n^2)
    stable
    """
    n = len(alist)
    mid_value = alist[0]
    low = 0
    high = n-1

    while low < high:
        # high move to the left
        while low < high and alist[high] > mid_value:
            high -= 1
        alist[low] = alist[high]
        low += 1

        # low move to the right
        while low < high and alist[low] < mid_value:
            low +=1
        alist[high] = alist[low]
        high -= 1

if __name__ == "__main__":
    li = [104, 54, 26, 93, 17, 77, 26, 44, 55, 20]
    print(li)
    quick_sort(li)
    print(li)