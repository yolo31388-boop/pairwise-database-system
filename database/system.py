"""
pairwise-database-system - DatabaseSystem

This module contains a deliberately broken implementation.
Fix all bugs so that tests pass.
"""


class DatabaseSystem:
    def __init__(self):
        self.state = {}

    def execute_query(self, *args, **kwargs):
        """BUG: 执行查询不做查询优化，永远全表扫描"""
        return None

    def create_index(self, *args, **kwargs):
        """BUG: 索引不做B+树，用数组线性查找"""
        return None

    def begin_transaction(self, *args, **kwargs):
        """BUG: 事务不做隔离级别，脏读不可重复读"""
        return None

    def parse_query(self, *args, **kwargs):
        """BUG: 查询解析不做语法检查，SQL错了不报错"""
        return None

    def read_write_data(self, *args, **kwargs):
        """BUG: 存储不做页管理，每条记录单独IO"""
        return None

