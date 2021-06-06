import json
import json_tools
#利用json_tools对比；
def json_diff(json_1, json_2):
    result = json_tools.diff(json_1, json_2)
    print(result)

a = {"rd": "yanan", "pro": {"sh": "shandong", "city": ["zibo", "weifang"]}}
b = {"rd": "Yanan", "pro": {"sh": "shandong", "town": ["taian", "weifang"]}}

json_diff(a, b)


#简单数据结构的对比
'''
dict1 = {"id": "2", "name": "测试"}
dict2 = {"id": "3", "name": "2"}

for src_list, dst_list in zip(sorted(dict1), sorted(dict2)):
    if str(dict1[src_list]) != str(dict2[dst_list]):
        print(src_list,dict1[src_list],dst_list,dict2[dst_list])
'''

def cmp(src_data, dst_data):
    if isinstance(src_data, dict):
        """若为dict格式"""
        for key in dst_data:
            if key not in src_data:
                print("src不存在这个key")
        for key in src_data:
            if key in dst_data:
                """递归"""
                cmp(src_data[key], dst_data[key])
            else:
                print("dst不存在这个key")
    elif isinstance(src_data, list):
