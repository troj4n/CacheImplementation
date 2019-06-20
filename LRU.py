# coding: utf-8
# Your code here!
from collections import deque

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque([])
        

    def get(self, key: int) -> int:
        v = self.cache.get(key, -1)
        if v != -1:
            self.queue.remove(key)
            self.queue.append(key)
        return v
        

    def put(self, key: int, value: int) -> None:
        # if key already exist, then replace:
        if self.cache.get(key, -1) != -1:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        # if key not exist and capacity is full
        elif self.capacity == len(self.queue):
            pop_out = self.queue.popleft()
            self.cache[pop_out] = -1
        
            self.queue.append(key)
            self.cache[key] = value
        # if key not exist and capacity is not full
        else:
            self.queue.append(key)
            self.cache[key] = value
