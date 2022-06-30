# 小彭的乱码
import cards_tools


def cards_main():
    while True:
        cards_tools.show_menu()
        action = input('请选择操作功能：')
        print("选择的操作是：%s" % action)
        if action in ['1', '2', '3']:
            if action == '1':
                cards_tools.new_cards()
            elif action == '2':
                cards_tools.show_all()
            elif action == '3':
                cards_tools.search_card()
        elif action == '0':
            print('欢迎下次光临')
            break
        else:
            print('输入错误，请重新输入')


cards_main()