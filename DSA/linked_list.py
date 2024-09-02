
class User:
    def __init__(self, name, id, password):
        self.name = name
        self.id = int(id)  
        self.password = password

class UserNode:
    def __init__(self, user):
        self.user = user
        self.left = None
        self.right = None

class UserBST:
    def __init__(self):
        self.root = None

    def signup(self, name, user_id, password):
        new_user = User(name, user_id, password)
        new_node = UserNode(new_user)
        if self.root is None:
            self.root = new_node
            print("Signup successful!")
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.user.id < current.user.id:
            if current.left is None:
                current.left = new_node
                print("Signup successful!")
            else:
                self._insert(current.left, new_node)
        elif new_node.user.id > current.user.id:
            if current.right is None:
                current.right = new_node
                print("Signup successful!")
            else:
                self._insert(current.right, new_node)
        else:
            print("ID already exists!")

    def login(self, id, password):
        return self._search(self.root, int(id), password)  

    def _search(self, current, id, password):
        if current is None:
            print("Invalid ID or password!")
            return False
        if id < current.user.id:
            return self._search(current.left, id, password)
        elif id > current.user.id:
            return self._search(current.right, id, password)
        else:
            if current.user.password == password:
                print(f"Login successful! Welcome {current.user.name}!")
                return True
            else:
                print("Invalid ID or password!")
                return False

    def display_users(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(f"Name: {node.user.name}, ID: {node.user.id}")
            self._inorder_traversal(node.right)

class StudentBST(UserBST):
    pass
