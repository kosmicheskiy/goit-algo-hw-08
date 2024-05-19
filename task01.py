import heapq

def find_min_cost(cable_lengths):
    heapq.heapify(cable_lengths)  # list to min-heap

    total_cost = 0
    while len(cable_lengths) > 1:
        print(cable_lengths)
        min1 = heapq.heappop(cable_lengths)  # 1st min element
        min2 = heapq.heappop(cable_lengths)  # next min element
        cost = min1 + min2
        total_cost += cost
        heapq.heappush(cable_lengths, cost)  # add element to heap

    return total_cost


cable_lengths = [1, 3, 4, 2]
min_cost = find_min_cost(cable_lengths)
print(min_cost)  # 19
