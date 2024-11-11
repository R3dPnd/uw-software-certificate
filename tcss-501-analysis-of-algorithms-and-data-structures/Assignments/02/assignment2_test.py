from linked_list_and_queue import Deque, LinkedList

print("\n\n\n\n\n--- Linked List Tests ---")

list = LinkedList()
list.append("Hello")
list.append("World")
list.append("Wow")

print("Original list content:")
for i in list.iter():
    print(i)


print("- Char Count: " + str(list.charCount()) + " expected [5, 5, 3]")
print("- Char Count Aggregated: " + str(list.charCount(aggregated=True)) + " expected 13")

list.delete("Wow")

print("- Char Count after Delete: " + str(list.charCount()) + " expected [5, 5]")
print("- Char Count after Delete Aggregated: " + str(list.charCount(aggregated=True)) + " expected 10")

try:
    print("- Original List:")
    for i in list.iter():
        print(i)
        
    new_list = list.reverse()
    print("- New List Reversed (in_place = False):")
    for i in new_list.iter():
        print(i)
except Exception as e:
    print("FAILED NEW LIST REVERSE")
    print(e)

try:
    print("- Reversed in_place=True List:")
    list.reverse(in_place=True)
    for i in list.iter():
        print(i)
except Exception as e:
    print("FAILED IN PLACE REVERSE")
    print(e)


print("\n--- Queue Tests ---")

queue = Deque()

queue.enqueue("Hello")
queue.enqueue("World")
queue.enqueue("Wow")

def print_queue(queue):
    result_string = ""

    temp_queue = Deque()
    item = queue.dequeue()
    attempts = 0

    while item is not None:
        temp_queue.enqueue(item)
        result_string += item + " "
        item = queue.dequeue()

        attempts += 1
        if attempts > 100:
            print("Infinite loop detected FAILED")
            break

    item = temp_queue.dequeue()
    while item is not None:
        queue.enqueue(item)
        item = temp_queue.dequeue()

        attempts += 1
        if attempts > 100:
            print("Infinite loop detected FAILED")
            break

    return result_string

print("Queue state:")
result = print_queue(queue)
print(result)

queue.addFirst("First")

print("Queue state after addFirst:")
result = print_queue(queue)
if result != "First Hello World Wow ":
    print("FAILED ADD FIRST")
    print(result)
else:
    print("PASSED ADD FIRST")

queue.addLast("Last")

print("Queue state after addLast:")
result = print_queue(queue)
if result != "First Hello World Wow Last ":
    print("FAILED ADD LAST")
    print(result)
else:
    print("PASSED ADD LAST")

queue.removeFirst()

print("Queue state after removeFirst:")
result = print_queue(queue)
if result != "Hello World Wow Last ":
    print("FAILED REMOVE FIRST")
    print(result)
else:
    print("PASSED REMOVE FIRST")

queue.removeLast()

print("Queue state after removeLast:")
result = print_queue(queue)

if result != "Hello World Wow ":
    print("FAILED REMOVE LAST")
    print(result)
else:
    print("PASSED REMOVE LAST")