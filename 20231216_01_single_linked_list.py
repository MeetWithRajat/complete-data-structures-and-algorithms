class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def __str__(self):
        list_element = "The list is: "
        if self.__length == 0:
            list_element += "Empty"
            return list_element
        temp = self.__head
        while temp:
            list_element += str(temp.data)
            temp = temp.next
            if temp:
                list_element += " -> "
        return list_element

    def print_info(self):
        print(f"Head is: {type(self.__head)}\nTail is: {type(self.__tail)}\nLength is: {self.__length}")

    @property
    def length(self):
        return self.__length

    def append(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__length += 1

    def prepend(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head = node
        self.__length += 1

    def insert_after_node(self, node_value, data):
        temp = self.__head
        while temp and temp.data != node_value:
            temp = temp.next

        if temp is None:
            print(f"Node with value {node_value} not found.")
        else:
            node = Node(data)
            node.next = temp.next
            if temp.next is None:
                self.__tail = node
            temp.next = node
            self.__length += 1

    def delete_end(self):
        if self.__length == 0:
            print("List is already empty")
        elif self.__length == 1:
            print(f"Last element deleted: {self.__head.data}")
            self.__head = None
            self.__tail = None
            self.__length = 0
        else:
            temp = self.__head
            for _ in range(self.__length - 2):
                temp = temp.next
            print(f"Last element deleted: {temp.next.data}")
            temp.next = None
            self.__length -= 1


my_list = SingleLinkedList()
my_list.print_info()
print(my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.prepend(7)
my_list.prepend(0)
my_list.append(40)
my_list.insert_after_node(20, 25)
my_list.insert_after_node(0, 5)
my_list.insert_after_node(40, 50)
my_list.insert_after_node(50, 200)
my_list.append(60)

print(my_list)
print()
my_list.print_info()
print(my_list.length)

print(my_list)

my_list.delete_end()
print(my_list)
my_list.print_info()
print(my_list)
