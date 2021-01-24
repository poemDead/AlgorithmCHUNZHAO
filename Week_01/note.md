# 第一周笔记

[超好用的Cheat Sheet](https://www.bigocheatsheet.com/)
## 知识点：
- 数组 Array
    - 在内存中保留一部分地址，方便直接访问任意元素

    - 查询时间复杂度为O(1)，插入和删除为O(n)

- 链表 Linked-list
    - 单向链表，双向链表，循环链表
    - 包含Value和指针
    - 头节点Head和尾节点Tail
    - 插入和删除方便，时间复杂度为O(1)；但是查询时间复杂度为O(n)

- 跳表 Skip list
    -  为有序链表添加多级索引，提高查询效率
    - 升维思维 + 空间换时间

- 栈 Stack
    - **后入先出Last in - First out**，添加删除均为O(1)
    - python中使用list实现，进行pop和append

- 队列 Queue
    - **先入先出First in Last out**，添加删除均为O(1)
    - 优先队列 Priority Queue:
    - 双端队列 Deque(Double-ended Queue): [Python中用collections.deque实现](https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html#using-lists-as-queues)

- 哈希表 Hash table
> 也叫散列表，根据Key Value而直接访问的数据结构。工程实践：电话簿，用户信息表，LRU Cathe，Redis-键值对存储

- 映射
- 集合

## 题目总结：
- [x] 移动零
    - python中遇到0就append再remove一下
    - 目前思路：快慢指针，把0全部交换到最后
- [x] 盛水最多的容器
    - 双循环 --> 超时了
    - 学习：左右夹逼法
- [x] 爬楼梯
    > 蒙蔽时候的思路：先思考暴力法，如果不行就思考各种基本情况，找到最近重复子问题。因为编程的本质就是**找可重复部分。**
    - 爬楼梯其实本质上就是f(n) = f(n-1) + f(n-2)，也就是Fibonacci问题
- [x] 3数之和
    - 排序之后进行左右夹逼
- [x] 2数之和
- [x] 环形链表
- [x] 有效的括号
    - 使用栈Stack解决问题的典例
- [] 最小栈
- [] 柱状图的最大矩形
- [] 滑动窗口最大值
- [] 设计循环双端队列
- [] 接雨水
- [] 有效的字母异位词
- [] 字母异位词分组
- [x] 删除排序数组重复项
- [x] 旋转数组
- [x] 合并两个有序链表
    - 首次体会到递归的牛逼
- [x] 合并两个有序数组

