from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        nodes = [i for i in range(n)]
        edges = sorted([sorted(row) for row in edges])
        if edges == [[]]:
            return cnt

        while edges:
            stack = deque([edges[0][0], edges[0][1]])
            edges.remove(edges[0])

            while stack:
                point = stack.popleft()
                nodes.remove(point) if point in nodes else None
                
                buf_edges = edges[:]
                for edge in buf_edges:
                    if point == edge[0]:
                        stack.append(edge[1])
                        edges.remove(edge)
                    elif point == edge[1]:
                        stack.append(edge[0])
                        edges.remove(edge)
                

            cnt += 1

        not_connected_cnt = len(nodes)
        return cnt + not_connected_cnt


