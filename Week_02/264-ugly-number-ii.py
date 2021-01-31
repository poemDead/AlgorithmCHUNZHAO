class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # m 记录现在算了几个丑数
        # u 记录所有丑数
        # i2,i3,i5是三指针
        m = 1
        u = [1]
        i2, i3, i5 = 0, 0, 0

        while m < n:
            # 目前，2，3，5✖️指针，谁最小，最小的就是这轮的丑数
            j2, j3, j5 = u[i2] * 2, u[i3] * 3, u[i5] * 5
            temp = min(j2, j3, j5)
            if temp == j2:
                i2 += 1
            if temp == j3:
                i3 += 1
            if temp == j5:
                i5 += 1
            u.append(temp)
            m += 1
        
        return u[-1]