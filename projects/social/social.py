import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for i in range(num_users):
            self.add_user(i)
            
            
        # Create friendships
        # total_friendships = num_users * avg_friendships
             # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                possible_friendship = (user, friend)
                possible_friendships.append(possible_friendship)
        random.shuffle(possible_friendships)
        total_friendships = num_users * avg_friendships // 2
        random_friendships = possible_friendships[:total_friendships]
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])
        
    def get_neighbors(self, user_id):
        return self.friendships[user_id] 
        
    def search(self,   starting_vertex, destination_vertex, visited= set(), path = []):
        if len(path) == 0:
            path.append(starting_vertex)
            
        if starting_vertex == destination_vertex:
            # path.append(destination_vertex)
            return path
        
        visited.add(starting_vertex)
        
        neighbors = self.get_neighbors(starting_vertex)
        
        if len(neighbors) == 0:
            return None
        
        for n in neighbors:
            if n not in visited:
               new_path = path + [n]
               result = self.search(n, destination_vertex, visited, new_path)
            
               if result is not None:
                  return result
           
        
           
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        
        q.enqueue(user_id)
        stack = [[user_id]]
        
        while len(stack)>0:
            path = stack.pop(0)
            cur_user = path[-1]
            
            if cur_user not in visited:
                visited[cur_user]=path
                
                for user in self.friendships[cur_user]:
                    new_path = list(path)
                    new_path.append(user)
                    stack.append(new_path)
                
        # while q.size()>0:
            
        #     v = q.dequeue()
        #     neighbors = self.get_neighbors(v)
             
        #     for n in neighbors:
                 
        #         if n not in visited:
        #            q.enqueue(n) 
        #            visited[n]= self.search(v,n)
                   
                   
                
        
        
         
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print( sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("C",connections)
 