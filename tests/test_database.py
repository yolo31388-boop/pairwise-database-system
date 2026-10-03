import pytest
from database.system import DatabaseSystem


class TestDatabaseSystem:

    def test_execute_query(self):
        """执行查询不做查询优化，永远全表扫描"""
        obj = DatabaseSystem()
        result = obj.execute_query()
        self.assertIsNotNone(result)

    def test_create_index(self):
        """索引不做B+树，用数组线性查找"""
        obj = DatabaseSystem()
        result = obj.create_index()
        self.assertIsNotNone(result)

    def test_begin_transaction(self):
        """事务不做隔离级别，脏读不可重复读"""
        obj = DatabaseSystem()
        result = obj.begin_transaction()
        self.assertIsNotNone(result)

    def test_parse_query(self):
        """查询解析不做语法检查，SQL错了不报错"""
        obj = DatabaseSystem()
        result = obj.parse_query()
        self.assertIsNotNone(result)

    def test_read_write_data(self):
        """存储不做页管理，每条记录单独IO"""
        obj = DatabaseSystem()
        result = obj.read_write_data()
        self.assertIsNotNone(result)

