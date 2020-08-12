class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


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
        #

        self.bucket = [None] * capacity
        self.item_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.bucket)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        load = self.item_count / self.capacity
        return load

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
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        new_node = HashTableEntry(key, value)

        # check if index is empty
        if self.bucket[idx] is None:
            # add index into bucket
            self.bucket[idx] = new_node
            # item count +=1
            self.item_count += 1

        # if bucket index is not None:
            # updated the value for an existing key or create a new entry for the key
        else:
            current = self.bucket[idx]

            while current.key != key and current.next:
                current = current.next

            # update keys current value
            if current.key == key:
                current.value = value

            # if no key found, new node
            else:
                current.next = new_node
                self.item_count += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        # if bucket index is not empty
        if self.bucket[idx] is not None:
            if self.bucket[idx].key == key:
                # delete index/ idx = None
                self.bucket[idx] = None
                self.item_count -= 1
        else:
            print("Key is not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        # if bucket index is empty, return None
        if self.bucket[idx] is None:
            return None
        else:
            while self.bucket[idx].key != key and self.bucket[idx].next is not None:
                self.bucket[idx] = self.bucket[idx].next

            # if bucket is not empty
            # if self.bucket[idx] is not None:
            #     # return bucket index value
            #     return self.bucket[idx]

            if self.bucket[idx].key == key:
                return self.bucket[idx].value
            else:
                return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here

        # Make a new array that's DOUBLE the current size

        old_bucket = self.bucket

        self.capacity = new_capacity
        self.bucket = [None] * new_capacity

        # Go through each linked list in the array
        for item in old_bucket:
            if item:
                currNode = item
                # Go through each item and rehash it
                # insert the items into their new location

                while currNode:
                    self.put(currNode.key, currNode.value)
                    currNode = currNode.next


if __name__ == "__main__":
    ht = HashTable(12)

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
