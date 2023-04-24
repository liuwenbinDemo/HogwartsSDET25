from typing import List


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
    items.sort(key=lambda x: x.name, reverse=True)
    print("收集的测试用例:%s" % items)
