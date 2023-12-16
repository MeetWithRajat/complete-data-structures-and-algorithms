class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def print_info(self):
        print(f"Head is: {type(self.__head)}\nTail is: {type(self.__tail)}\nLength is: {self.__length}")

    @property
    def length(self):
        return self.__length

    def insert_end(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node
        self.__length += 1

    def insert_beginning(self, data):
        node = Node(data)
        node.next = self.__head
        self.__head = node
        self.__length += 1

    def insert_after_node(self, node_value, data):
        temp = self.__head
        while temp is not None and temp.value != node_value:
            temp = temp.next

        if temp is None:
            print(f"Node with value {node_value} not found.")
        else:
            node = Node(data)
            node.next = temp.next
            temp.next = node
            self.__length += 1

    def print_list(self):
        if self.__length == 0:
            print("Empty", end="")
        temp = self.__head
        while temp is not None:
            print(temp.value, end="")
            temp = temp.next
            if temp is not None:
                print(" -> ", end="")
        print()

    def delete_end(self):
        if self.__length == 0:
            print("List is already empty")
        elif self.__length == 1:
            print(f"Last element deleted: {self.__head.value}")
            self.__head = None
            self.__tail = None
            self.__length = 0
        else:
            temp = self.__head
            for _ in range(self.__length - 2):
                temp = temp.next
            print(f"Last element deleted: {temp.next.value}")
            temp.next = None
            self.__length -= 1


my_list = SingleLinkedList()
my_list.print_info()
my_list.insert_end(10)
my_list.insert_end(20)
my_list.insert_end(30)
my_list.insert_end(40)
my_list.insert_beginning(0)
my_list.insert_after_node(20, 25)
my_list.insert_after_node(0, 5)
my_list.insert_after_node(40, 50)
my_list.insert_after_node(56, 200)

print("\nThe list is: ", end="")
my_list.print_list()
print()
my_list.print_info()
print(my_list.length)

print("\nThe list is: ", end="")
my_list.print_list()

my_list.delete_end()
print("The list is: ", end="")
my_list.print_list()
my_list.print_info()
