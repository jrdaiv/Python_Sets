# Task 1
# destination that both airlines fly too
# Destinations unnique to mine
# whether there is an airline we both dont share

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_destination = our_routes.union(competitor_routes)
print("Both airlines travel to: ")
print(same_destination)

shared_destination = our_routes.intersection(competitor_routes)
print("Most common destination: ")
print(shared_destination)

not_shared = our_routes.symmetric_difference(competitor_routes)
print("Airlines that are not shared: ")
print(f"{not_shared}")