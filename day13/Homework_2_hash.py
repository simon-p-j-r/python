# 小彭的乱码
class HashNode:
    def __init__(self, num):
        self.num = num
        self.next = None

    def __repr__(self):
        return self.num


MAXKEY = 10


def elf_hash(hash_str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        h &= ~g
    return h % MAXKEY


class HashBuild:
    def __init__(self):
        self.info_list = [None] * MAXKEY

    def addnode(self, node: HashNode):
        """
        向hash数组中增加元素
        :param node:
        :return:
        """
        hash_num = elf_hash(node.num)
        if self.info_list[hash_num] is None:
            self.info_list.insert(hash_num, node)
        else:
            tag: HashNode = self.info_list[hash_num]
            while tag.next is not None:
                tag = tag.next
            tag.next = node

    def find_hash(self, target):
        list1 = self.info_list
        tag = 0
        for i in range(0, MAXKEY):
            if list1[i] is not None:
                if list1[i].next is not None:
                    node = list1[i].next
                    while node is not None:
                        if node.num == target:
                            tag += 1
                        node = node.next
                if list1[i].num == target:
                    tag += 1
        print(target, '出现了', tag, '次')

    # def delete_hash(self, target):
    #     list1 = self.info_list
    #     for i in range(0, MAXKEY):
    #         if list1[i] is not None:
    #             if list1[i].next is not None:
    #                 node = list1[i].next
    #                 node_pre = list1[i]
    #                 while node is not None:
    #                     if node.num == target:
    #                         print(i, '删除成功')
    #                         node_pre.next = None
    #                     node_pre = node
    #                     node = node.next
    #             else:
    #                 if list1[i].num == target:
    #                     print(i,'删除成功')
    #                     list1[i] = None


    def output_all(self):
        """
        输出hash数组中的所有元素
        :return:
        """
        list1 = self.info_list
        for i in range(0, MAXKEY):
            if list1[i] is not None:
                if list1[i].next is not None:
                    node = list1[i]
                    while node is not None:
                        print(list1[i], end='->')
                        node = node.next
                else:
                    print(list1[i])
            else:
                print(list1[i])


if __name__ == '__main__':
    node = HashNode('asd')
    node1 = HashNode('asd')
    node2 = HashNode('asd')
    node3 = HashNode('pengjiaren')
    hash_table = HashBuild()
    hash_table.addnode(node)
    hash_table.addnode(node1)
    hash_table.addnode(node2)
    hash_table.addnode(node3)
    hash_table.find_hash('asd')
    hash_table.output_all()
