def bf(s1: str, s2: str) -> int:
    """
    BF算法伪伪代码
    :param s1:原字符串
    :param s2: 要匹配的子字符串
    :return: 匹配子字符串第一次出现的位置，没有返回-1
    """
    # 指针
    p1 = 0
    p2 = 0

    # 遍历整个原字符串
    for i in range(len(s1)):
        # 下面两个操作可以放在循环尾，方便理解
        # p1 = i
        # p2 = 0

        # 验证是否能匹配
        for j in range(len(s2)):
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:  # 当发现不匹配时终止匹配操作
                break
        if p2 == len(s2):
            return p1 - p2 + 1  # 返回子在串中开始的位置
        p1 = i
        p2 = 0
    return -1  # 没有匹配到返回-1


if __name__ == "__main__":
    s1 = "abababc"
    s2 = "abc"
    print(bf(s1, s2))
    print(s1.find(s2) + 1)
    print("abc".find("a"))
