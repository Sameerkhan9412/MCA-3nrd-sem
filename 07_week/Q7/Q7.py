class Router:
    def __init__(self,name):
        self.name = name
        self.connections = {f"{self.name}": 0,}
    def __str__(self):
        
        return self.name
    def connect(self,router,cost = 1):
        self.connections[router.name] = cost
        router.connections[self.name] = cost

    def printRouters(self):
        print("Router: ",self)
        print("Routing Table")
        for key in self.connections.keys():
            print(f"{key}   |  {self.connections.get(key)}")


def updateRouters(routers):
    for router in routers.keys():
        get_con = routers.get(router).connections.copy()
        for con_router, cost in get_con.items():
            if cost == 1:
                update_routing_table(routers.get(router),con_router)
        routers.get(router).printRouters()          
            
def update_routing_table(myrouter, neighbor_name):


        neighbor = routers[neighbor_name]
        for destination, neighbor_cost in neighbor.connections.items():
            if destination != myrouter.name:  
                new_cost = myrouter.connections[neighbor_name] + neighbor_cost
                
            
                if destination not in myrouter.connections or new_cost < myrouter.connections[destination]:
                    print(f"    Updating {myrouter.name}'s table: {destination} via {neighbor_name} with cost {new_cost}")
                    myrouter.connections[destination] = new_cost     


r1 = Router("R1")
r2 = Router("R2")
r3 = Router("R3")
r4 = Router("R4")
r5 = Router("R5")

r1.connect(r2)
r2.connect(r3)
r2.connect(r4)
r3.connect(r5)
r4.connect(r5)

routers = {r1.name : r1,r2.name : r2,r3.name : r3,r4.name : r4,r5.name : r5}

print("Initial Routing table")
for router in routers.keys():
    routers.get(router).printRouters()
    print("----------------------------")
    
for i in range(0,3):
    
    print(f"\nRouting Iteration : {i}\n")
    updateRouters(routers)