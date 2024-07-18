from fastapi import FastAPI

app = FastAPI()

# Problem 1: Majority Element
def find_majority_element(number_string: str) -> int:
    numbers = number_string.split(',')
    count_dict = {}
    
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    
    n = len(numbers)
    for number, count in count_dict.items():
        if count > n / 2:
            return int(number)

@app.get("/majority-element")
def get_majority_element(number_string: str):
    majority_element = find_majority_element(number_string)
    return {"majority_element": majority_element}

# Problem 2: Linked List Sorting
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def sort(self, ascending=True):
        result = self.to_list()
        result.sort(reverse=not ascending)
        self.head = None
        for data in result:
            self.append(data)

def create_linked_list_from_string(number_string: str) -> LinkedList:
    numbers = number_string.split(',')
    linked_list = LinkedList()
    for number in numbers:
        linked_list.append(int(number))
    return linked_list

@app.get("/sort-linked-list")
def get_sorted_linked_list(number_string: str, order: str):
    linked_list = create_linked_list_from_string(number_string)
    if order == "ascending":
        linked_list.sort(ascending=True)
    elif order == "descending":
        linked_list.sort(ascending=False)
    else:
        return {"error": "Invalid order parameter. Use 'ascending' or 'descending'."}
    
    sorted_list = linked_list.to_list()
    return {"sorted_list": sorted_list}

# To run the FastAPI app:
# uvicorn filename:app --reload
