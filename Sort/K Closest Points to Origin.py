'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
'''


def calculate_dis(point):
    x = point[0],y = point[1]
    return x*x + y*y


def method1(points):
    if len(points) < 2:
        return points
    v = points[0][0] ** 2 + points[0][1] ** 2
    left = [p for p in points if (p[0] ** 2 + p[1] ** 2) < v ]
    right = [p for p in points if (p[0] ** 2 + p[1] ** 2) > v]
    left = method1(left)
    right = method1(right)
    res = []
    res += left
    res.append(points[0])
    res += right
    return res

def method(points,k):
    points = method1(points)
    print(points[:k])

points =[[1,3],[-2,2]]
method(points,1)

















