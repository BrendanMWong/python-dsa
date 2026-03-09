class LRUCache:
    class DlList:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def remove(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node
        
    def insert(self, node):
        second_node = self.head.next

        node.next = second_node
        node.prev = self.head

        self.head.next = node
        second_node.prev = node
            
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        # create dummy head and tail nodes and connect them to eachother
        self.head = self.DlList(None, None)
        self.tail = self.DlList(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # its recently used now
        node = self.cache[key]
        self.remove(node) # helper function
        self.insert(node) # helper function

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update key value pair
            node = self.cache[key]
            node.value = value
            self.remove(node) # helper function
            self.insert(node) # helper function
        else:
            if len(self.cache) >= self.capacity:
                # evict least recently used key if cache is full
                evict_node = self.tail.prev
                self.remove(evict_node)
                self.cache.pop(evict_node.key)
            # add key value pair
            node = self.DlList(key, value)
            self.cache[key] = node
            self.insert(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)