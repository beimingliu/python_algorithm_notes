# source: https://www.bilibili.com/video/av21540971/?p=24


def select_sort(alist):
    """select sort
    best: O(n^2)
    worst: O(n^2)
    not stable
    """
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 26, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)
