class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def get_key(self):
        return self.key;

    def get_value(self):
        return self.value;

    def get_next(self):
        return self.next;

    def set_next(self, new_next):
        self.next = new_next;

class LinkedList:
    def __init__(self):
        self.head = None;

    def find(self, key):
        cur = self.head;

        while cur is not None:
            if cur.key == key:
                return cur;

            cur = cur.next;

        return None;

    def delete(self, key):
        cur = self.head;

        if cur.key == key:
            self.head = cur.next;
            return cur;

        prev = cur;
        cur = cur.next;

        while cur is not None:
            if cur.key == key:  # Found it!
                prev.next = cur.next   # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next

        return None;  # If we got here, nothing found

    def insert_at_head(self, node):
        node.next = self.head;
        self.head = node;

    def insert_or_overwrite_value(self, key, value):
        node = self.find(key);

        if node is None:
            # Make a new node
            self.insert_at_head(HashTableEntry(key, value));
            return True;
        else:
            # Overwrite old value
            node.value = value;
            return False;

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = MIN_CAPACITY if capacity <= MIN_CAPACITY else capacity;
        self.list = [LinkedList()] * self.capacity;
        self.total = 0;

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.list);

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.total / self.capacity;

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # total = 0;

        # key_bytes = key.encode();

        # for byte in key_bytes:
        #     total += byte;

        # print('sklfja;sdf: ' + str(self.capacity) + ' - (' + key + ') ' + str(total) + ' - ' + str(total % self.capacity));

        # return total;

        hash = 5381;
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        index = self.hash_index(key);

        temp = self.list[index].insert_or_overwrite_value(key, value);

        if temp:
            self.total += 1;

        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2);

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        if self.list[self.hash_index(key)].delete(key) is not None:
            self.total -= 1;

        if self.get_load_factor() <= 0.2:
            self.resize(self.capacity // 2 if self.capacity // 2 >= MIN_CAPACITY else MIN_CAPACITY);

        # self.list[self.hash_index(key)] = None;

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        node = self.list[self.hash_index(key)].find(key);
        if node is not None:
            return node.value;
        else:
            return None;
        # return self.list[self.hash_index(key)].find(key).value;
        # return self.list[self.hash_index(key)];

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        oldList = self.list;
        newList = [LinkedList()] * new_capacity;

        self.list = newList;
        self.capacity = new_capacity;

        for i in oldList:
            if i.head is not None:
                curr = i.head;
                while curr is not None:
                    self.put(curr.key, curr.value);
                    curr = curr.next;

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

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
