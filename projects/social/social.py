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
        
        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')
        
        # OPTIMIZED solution
        # target_friendships = (num_users * avg_friendships) // 2
        # total_friendships = 0

        # while total_friendships < target_friendships:
        #     user_id = random.randint(1, self.last_id)
        #     friend_id = random.randint(1, self.last_id)
        #     if self.add_friendship(user_id, friend_id):
        #         total_friendships += 1

        # generate possible friendships
        possible = []

        # avoid dups by making sure the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible.append((user_id, friend_id))

        # shuffle the possible friendships
        random.shuffle(possible)
        # Create friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        * Take user_id as starting_node

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        * The claim for BFS is that the first time a node is discovered during the traversal, that distance from the source would give us the shortest path

        The key is the friend's ID and the value is the path.


        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # start with an ID
        # get its friends
        my_friends = self.friendships[user_id]
        # print("my_friends", my_friends)

        q = Queue()
        q.enqueue([user_id])
        # for each of those friends, add to the visited dict {friend: [user_id, friend]}
        # for friend in my_friends:
        #     if friend not in visited:
        #         visited[friend] = [user_id, friend]

        while q.size() > 0:
            path = q.dequeue()
            last_friend = path[-1]
            # print("last_friend", last_friend)

            if last_friend not in visited:
                visited[last_friend] = path

                # copy and append new list
                # with newly added value
                for value in self.friendships[last_friend]:
                    # new_path = list(path)
                    # new_path.append(value)
                    # print("new_path", new_path)
                    # q.enqueue(new_path)
                    # print("value:", value)

                    # another example:
                    # q.enqueue(path + [value])

                    # another example:
                    q.enqueue([*path, value])



        # for each of those friends, get their firends and record paths to them
        print("visited")
        return visited
"""
        
"""

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 3)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

# for i in range(1, 1000):
#     connections = sg.get_all_social_paths(i)

#     users_in_ext_network = len(connections) - 1
#     total_users = len(sg.users)

#     percentage = users_in_ext_network / total_users * 100

#     if percentage < 94:
#         print(f'User {i}: percentage: {percentage: .2f}')


