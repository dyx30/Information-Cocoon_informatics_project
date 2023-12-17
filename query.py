def query(lb):
    """
    请求用户从abc中选择一个，读取一个字符输入
    如果读到z，返回-1
    :return: 对应的大类（int）
    """
    user_input = input("请选择您想观看的视频：")
    lowercase_input = user_input.lower()
    if lowercase_input == 'z':
        return -1
    elif lowercase_input in lb:
        return lb[lowercase_input]
    else:
        print("无效的选择，请从a、b、c中选一个")
        return query(lb)  # 递归调用以重新请求输入

'''
#test
label={"a":3,"b":1,"c":2}  #代表三个选项分别对应的大类标签
result = query(lb=label)
print("用户选择的大类是:", result)
'''


