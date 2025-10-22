from heapq import heappop, heappush

def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    heap: list[tuple[int, list[int]]] = []

    for pt in points:
        heappush(heap, (pt[0]**2 + pt[1]**2, pt))

    res = []
    for _ in range(k):
        _, pt = heappop(heap)
        res.append(pt)
    return res

if __name__ == "__main__":
    n = int(input("Enter number of points: "))
    points = []
    for _ in range(n):
        x, y = map(int, input("Enter point coordinates (x y): ").split())
        points.append([x, y])
    k = int(input("Enter number of closest points to find: "))
    result = k_closest_points(points, k)
    print("The k closest points to the origin are:")
    for point in result:
        print(point)