import random
class LoadBalancer:

    def __init__(self):
        self.Servers=[]
        self.current_index=0

    def add_server(self, server) ->  bool:
        if server not in self.Servers and len(self.Servers) < 10:
            self.Servers.append(server)
            return True
        return False
    
    def remove_server(self,server) -> bool:
        if server in self.Servers:
            self.Servers.remove(server)
            return True
        return False
    def show_all(self):
        print(self.Servers)
    
    def get_random_server(self) -> object:
        if len(self.Servers) > 0:
            return random.choice(self.Servers)
    
    def get_round_robin_server(self) -> object:
        if len(self.Servers) > 0:
            srv=self.Servers[self.current_index]
            self.current_index=(self.current_index +1) % len(self.Servers)
            return srv
    def get_next_server(self, strategy="round_robin"):
        if strategy == "round_robin":
            return self.get_round_robin_server()
        elif strategy == "random":
            return self.get_random_server()
        else:
            raise ValueError("Invalid load balancing strategy")



l = LoadBalancer()
l.add_server('server 1')
l.add_server('server 2')
l.add_server('server 3')
for i in range(10):
    print(l.get_next_server())
l.remove_server('server 2')
print('-----------------server 2 removed---------------------')
for i in range(10):
    print(l.get_next_server())
print('---------------server 4 added-----------------------')    
l.add_server('server 4')
for i in range(10):
    print(l.get_next_server())    