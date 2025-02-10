class Spaceship:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    def __str__(self):
        return f"{self.name} has {self.fuel} fuel."

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0: #edge case
            return None
        temp = self.head #temp assigned to index 0
        self.head = self.head.next #head assigned to index 1
        temp.next = None #get rids of connection between index 0 and 1
        self.length -= 1 #decreases length by 1 from the list
        if self.length == 0: #if list is 0, tail still points to temp although it doesn't exist
            self.tail = None #Have to update tail to None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre #moving the tail from temp (last node) to the previous one from the end of the list
        self.tail.next = None
        self.length -= 1 #reduced the size of the
        if self.length == 0: #length does not manually decrease because it was pre-defined in class LinkedList
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insert_at_index(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def delete_at_index(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.delfirst()
        if index == self.length - 1:
            return self.dellast()
        previous = self.head
        for _ in range(index - 1):
            previous = previous.next
        temp = previous.next
        previous.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

s1 = Spaceship("Voyager", 300)
s2 = Spaceship("Enterprise", 300)
s3 = Spaceship("Atlantis", 300)
s4 = Spaceship("Challenger", 300)
s5 = Spaceship("Artemis", 300)

myLinkedList = LinkedList(s1)
myLinkedList.append(s2)
myLinkedList.append(s3)
myLinkedList.prepend(s4)
myLinkedList.prepend(s5)
myLinkedList.print_list()
print("End of list")

myLinkedList.insert_at_index(2, Spaceship("Discovery", 300))
print("After insert_at_index function")
myLinkedList.print_list()

myLinkedList.delete_at_index(3)
print("After delete_at_index function:")
myLinkedList.print_list()