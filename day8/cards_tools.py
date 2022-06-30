# 小彭的乱码
card_list = []


def show_menu():
    print('*' * 50)
    print('欢迎光临')
    print('')
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print('')
    print('0. 退出系统')
    print('*' * 50)


def new_cards():
    print('-' * 50)
    print('功能：新建名片')

    name = input('请输入名字：')
    phone = input('请输入电话：')
    qq = input('请输入qq号码：')
    email = input('请输入邮箱：')

    cad_dict = {"name" : name, "phone" : phone,'qq' : qq,'email' : email}

    card_list.append(cad_dict)
    print(card_list)
    print('成功加入%s名片' % cad_dict['name'])


def show_all():
    # TODO 等一下再看看
    print('-' * 50)
    print('功能：显示全部')

    print(card_list)

    if len(card_list) == 0:
        print("名片夹为空")
        return  # 一会看一下这个return的效果


def search_card():
    print('-' * 50)
    print('功能：搜索名片')

    find_name = input('请输入要搜索名片的姓名：')
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print(card_dict)
            print('')
            deal_card(card_dict)
            break
    else:
        print('没有找到')


def deal_card(find_dict):
    print(find_dict)
    action_str = input('请选择要执行的操作：【1】修改 【2】删除 【3】返回上级菜单')
    if action_str == '1':
        amendment(find_dict)
    elif action_str == '2':
        rem_card(find_dict)
    elif action_str == '3':
        search_card()


def rem_card(find_dict):
    card_list.remove(find_dict)
    print('删除成功')


def amendment(find_dict):
    action_str = input('请选择要修改的变量：【1】name 【2】phone 【3】qq 【4】email 【5】all')
    if action_str == '1':
        find_dict["name"] = input("请输入姓名：")
    elif action_str == '2':
        find_dict["phone"] = input("请输入电话：")
    elif action_str == '3':
        find_dict["qq"] = input("请输入 QQ：")
    elif action_str == '4':
        find_dict["email"] = input("请输入邮件：")
    elif action_str == '5':
        find_dict["name"] = input("请输入姓名：")
        find_dict["phone"] = input("请输入电话：")
        find_dict["qq"] = input("请输入 QQ：")
        find_dict["email"] = input("请输入邮件：")
    print("%s 的名片修改成功" % find_dict["name"])