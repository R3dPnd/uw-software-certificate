class BinarySearchTreeSequential:

    def __init__(self, init_size=64):
        self.data = [None] * init_size
        self.count = 0

    def __expand__(self):
        self.data = self.data + [None] * len(self.data)

    def __get_idx_of_left__(self, index):
        return 2 * index + 1

    def __get_idx_of_right__(self, index):
        return 2 * index + 2

    def __get_idx_of_parent__(self, index):
        """ Returns the parent of a given index.  Returns -1 for root."""
        offset = 1 if index % 2 == 1 else 2
        return (index - offset) // 2

    def is_empty(self):
        return self.data[0] is None

    def insert(self, data):
        if self.is_empty():
            self.data[0] = data
        else:
            idx = 0
            while self.data[idx] is not None:
                if data < self.data[idx]:
                    idx = self.__get_idx_of_left__(idx)
                else:
                    idx = self.__get_idx_of_right__(idx)

                if idx > len(self.data) - 1:  # YOU HAVE REACHED
                    self.__expand__()

            self.data[idx] = data
            self.count += 1

    def search(self, data):
        idx = 0
        while self.data[idx] is not None:
            if data == self.data[idx]:
                return idx
            elif data < self.data[idx]:
                idx = self.__get_idx_of_left__(idx)
            else:
                idx = self.__get_idx_of_right__(idx)

            if idx > len(self.data) - 1:
                return None




if __name__ == "__main__":
    inputs = [8,6,7,5,3,0,9]
    bst = BinarySearchTreeSequential()  # CREATE A TREE THAT RUNS WITH NODES
    for input in inputs:
        print(f"Inserting {input}")
        bst.insert(input)

    print(f"How bloated is it: BST Contains {bst.count} records in an array of size {len(bst.data)}")
    print(bst.data[7])
    print(bst.search(7))