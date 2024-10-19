import heapq
from random import randint


def min_connection_cost(cables: list[float]):
    heap = cables.copy()
    heapq.heapify(heap)
    total_cost = 0

    while len(heap) > 1:
        c1 = heapq.heappop(heap)
        c2 = heapq.heappop(heap)
        cost = c1 + c2
        total_cost += cost
        heapq.heappush(heap, cost)

    return total_cost, heapq.heappop(heap)


def main():
    cables = [randint(1, 20) for _ in range(10)]
    total_cost, total_len = min_connection_cost(cables)
    print(f'Cables: {cables}')
    print(f'Total len: {total_len}')
    print(f'Total min cost: {total_cost}')


if __name__ == "__main__":
    main()
