#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/19 11:01
# @Author  : Xzx
# @FileName: test_async.py
# @Software: PyCharm





if __name__ == '__main__':
    start_time = datetime.datetime.now()
    request_1()
    # request_2()
    end_time = datetime.datetime.now()
    # 这里是在统计总耗时，从打印的结果可以看到是异步处理的。
    print("the spend of total time is:", (end_time - start_time).seconds)

