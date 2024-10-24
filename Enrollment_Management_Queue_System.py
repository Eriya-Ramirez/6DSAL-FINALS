class Node:
    """Node class for linked list implementation."""

    def __init__(self, name, is_pwd=False):
        self.name = name
        self.is_pwd = is_pwd
        self.next = None


class EnrollmentQueue:
    """Linked-list-based enrollment queue with PWD priority."""

    def __init__(self):
        self.pwd_head = None  # Head of the PWD queue
        self.pwd_tail = None  # Tail of the PWD queue
        self.normal_head = None  # Head of the normal queue
        self.normal_tail = None  # Tail of the normal queue
        self.currently_serving = None  # Tracks who is being served

    def enqueue(self, name, is_pwd):
        """Adds a student to the respective queue."""
        new_node = Node(name, is_pwd)

        if is_pwd:
            if self.pwd_tail:  # If PWD queue is not empty
                self.pwd_tail.next = new_node
            else:  # If PWD queue is empty
                self.pwd_head = new_node
            self.pwd_tail = new_node
            print(f"{name} (PWD) has been added to the PWD queue.")
        else:
            if self.normal_tail:  # If normal queue is not empty
                self.normal_tail.next = new_node
            else:  # If normal queue is empty
                self.normal_head = new_node
            self.normal_tail = new_node
            print(f"{name} (Normal) has been added to the normal queue.")

    def dequeue(self):
        """Serves the next student, prioritizing PWDs."""
        if self.pwd_head:
            # Serve from PWD queue
            self.currently_serving = self.pwd_head
            print(f"{self.pwd_head.name} (PWD) is being served.")
            self.pwd_head = self.pwd_head.next  # Move to the next in line
            if not self.pwd_head:  # If PWD queue becomes empty
                self.pwd_tail = None
        elif self.normal_head:
            # Serve from normal queue
            self.currently_serving = self.normal_head
            print(f"{self.normal_head.name} (Normal) is being served.")
            self.normal_head = self.normal_head.next  # Move to the next in line
            if not self.normal_head:  # If normal queue becomes empty
                self.normal_tail = None
        else:
            print("No one is in the queue.")
            self.currently_serving = None

    def view_currently_serving(self):
        """Displays who is currently being served."""
        if self.currently_serving:
            status = "PWD" if self.currently_serving.is_pwd else "Normal"
            print(f"Currently serving: {self.currently_serving.name} ({status})")
        else:
            print("No one is currently being served.")

    def view_queue(self):
        """Displays the state of both queues."""
        print("\n-- Queue Status --")
        print("PWD Queue:", end=" ")
        self._print_queue(self.pwd_head)
        print("Normal Queue:", end=" ")
        self._print_queue(self.normal_head)
        print("-------------------\n")

    def _print_queue(self, head):
        """Helper method to print the queue."""
        if not head:
            print("Empty")
        else:
            current = head
            while current:
                print(current.name, end=" -> " if current.next else "\n")
                current = current.next


def main():
    queue = EnrollmentQueue()

    while True:
        print("\nEnrollment Queue System")
        print("1. Add to Queue")
        print("2. Serve Next Person")
        print("3. View Currently Serving")
        print("4. View Queue")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            is_pwd = input("Is the student a PWD? (y/n): ").lower() == 'y'
            queue.enqueue(name, is_pwd)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.view_currently_serving()
        elif choice == '4':
            queue.view_queue()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
