class StackADT:
    def __init__(self)->None:
        self.stk = []
        
    def push(self, elem)->None:
        self.stk.append(elem)

    def pop(self):
        return None if self.is_empty() else self.stk.pop()

    def peek(self):
        return None if self.is_empty() else self.stk[-1]

    def is_empty(self)->bool:
        return len(self.stk) == 0

    def size(self)->int:
        return len(self.stk)

    def display(self)->None:
        print(self.stk)
        
    def clear(self):
        self.stk.clear()

def reverse_string_using_stack(str):
    stk = StackADT()
    for ch in str:
        stk.push(ch)
    rev = ""
    while (not stk.is_empty()):
        char = stk.pop()
        rev = rev + char # type:ignore
    return rev
    
def main():
    stk = StackADT()
    while True:
        print("< ---- STACK ADT MENU ---- >")
        print("1. Push \n2.Pop \n3. Peek \n4. isEmpty \n5. Size \n6. Display Stack \n7. Reverse String \n0. Exit")
        choice = int(input())
        match choice:
            case 0:
                print("Exiting...")
                return
            case 1:
                elem = int(input("Enter number to push"))
                stk.push(elem)
            case 2:
                print(f"Popped element: {stk.pop()}")
            case 3:
                print(f"Peeked element: {stk.peek()}")
            case 4:
                print(f"Stack is empty? {stk.is_empty()}")
            case 5: 
                print(f"Size of stack: {stk.size()}")
            case 6:
                print(f"Stack elements:")
                stk.display()
            case 7:
                st = input("Enter string: ")
                print(f"Reversed: {reverse_string_using_stack(st)}")
            case _:
                print("Invalid Input")

if __name__ == "__main__":
    main()