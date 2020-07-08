class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self):
        return f"Node value={self.value}"
class LinkedList:
    def __init__(self):
        self.head = None
    # def __str__(self):
    #     pass


    def insert_at_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_at_tail(self, value):
        node = Node(value)
        cur = self.head
        if cur == None:
            self.insert_at_head(value)
        else:
            while cur.next is not None:
                    cur = cur.next
            cur.next = node

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value.key == value:
                return cur.value.value
            cur = cur.next
        return None

    def delete(self, value):
        cur = self.head
        if cur.value.key == value:
            self.head = self.head.next
            cur.next = None
            return cur.value.value
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.value.key == value:
                prev.next = cur.next
                cur.next = None
                return cur.value.value
            else:
                prev = prev.next
                cur = cur.next
        return None
    def printList(self):
        cur = self.head
        if cur == None:
            print(None)
        else:
            while cur.next is not None:
                print(cur.value)
                cur = cur.next
            print("")


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f"HashTableEntry key={self.key}, value={self.value}"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.table = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        keys = 0
        for val in self.table:
            if val != None:
                keys += 1
            else:
                pass
        return keys / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here
        offset_basis = 14695981039346656037
        offset_prime = 1099511628211

        hash = offset_basis
        for char in key:
            hash = hash * offset_prime
            hash = hash ^ ord(char)
            hash &= 0xFFFFFFFFFFFFFFFF
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = (hash * 33) + ord(char)
            hash &= 0xFFFFFFFF
        return hash 


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        if self.get_load_factor() > .7:
            print(self.get_load_factor(), ">.7")
            self.resize(self.capacity*2)
        if self.get_load_factor() < .2 and self.get_load_factor() > 0:
            print(self.get_load_factor(), "<.2")
            self.resize(self.capacity//2)
        index = self.hash_index(key)
        if self.table[index] is None:
            self.table[index] = HashTableEntry(key, value)
        else:
            if type(self.table[index])== LinkedList:
                if self.get(key) is not None:
                    self.delete(key)
                self.table[index].insert_at_tail(HashTableEntry(key, value))
            else:
                if self.table[index].key == key:
                    self.delete(key)
                    self.table[index] = HashTableEntry(key, value)
                else:
                    ll = LinkedList()
                    ll.insert_at_tail(self.table[index])
                    ll.insert_at_tail(HashTableEntry(key, value))
                    self.table[index] = ll



    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if index:
            self.table[index] = None
        else:
            print("Key is not found")
        index = self.hash_index(key)
        if self.table[index]:
                if type(self.table[index])== LinkedList:
                    
                    return self.table[index].delete(key)
                else:
                    value = self.table[index].value
                    self.table[index] = None
                    return value
        else:
            print("Key is not found")
            return None
            


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.table[index]:
                if type(self.table[index])== LinkedList:
                    
                    return self.table[index].find(key)
                else:
                    return self.table[index].value
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        if new_capacity < 8:
            new_capacity = 8
        save_data = []
        for index in range(0,self.capacity):
            if type(self.table[index])== LinkedList:
                cur = self.table[index].head
                while cur is not None:
                    save_data.append(cur.value)
                    cur = cur.next
            else:
                save_data.append(self.table[index])
        self.capacity = new_capacity
        self.table = [None] * self.capacity
        for data in save_data:
            if data is not None:
                self.put(data.key, data.value)

    def recursiveResize(self):
        if self.get_load_factor() < .7 and self.get_load_factor() > .2:
            return
        else:
            if self.get_load_factor() > .7:
                self.resize(self.capacity*2)
                self.recursiveResize()
            else:
                self.resize(self.capacity//2)
                self.recursiveResize()

   


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")
 
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")

    print(ht.get_load_factor())
    


    



