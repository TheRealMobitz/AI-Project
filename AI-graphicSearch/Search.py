
import heapq
from Solution import Solution
from Problem import Problem
from datetime import datetime


class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        max_counter = 200
        while len(queue) > 0 or max_counter > 0:
            max_counter -= 1
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.goal_test(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None
    
    @staticmethod
    def dfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        stack = []
        state = prb.initState
        stack.append(state)
        max_counter = 200
        while len(stack) > 0 or max_counter > 0:
            max_counter -= 1
            state = stack.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.goal_test(c):
                    return Solution(c, prb, start_time)
                stack.append(c)
        return None
    
    @staticmethod
    def ucs(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = []
        limit= 200
        state = prb.initState
        queue.append = state
        depth = state.g_n
        while depth < limit :
            while len(queue) > 0:
                state = queue.pop(0)
                neighbors = prb.successor(state)
                for c in neighbors:
                    if prb.goal_test(c):
                        return Solution(c, prb, start_time)
                    queue.append(c)
            depth = depth + 1
        