# source: https://www.bilibili.com/video/av21540971/?p=25


def insert_sort(alist):
    """select sort
    best: O(n)
    worst: O(n^2)
    stable
    """
    n = len(alist)
    # 从右无序序列取多个元素
    for j in range(1, n):
        # i 代表内层循环起始值
        # 从右选1元素(i)，插入正确位置
        for i in range(j, 0, -1):
            if alist[i] < alist[i-1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break


if __name__ == "__main__":
    li = [104, 54, 26, 93, 17, 77, 26, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)