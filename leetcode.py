from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self,memoryLimit):
        self.memoryLimit = memoryLimit
        self.queue = deque
        self.packetSet = set()
        self.dest_map = defaultdict(list)
    def addpacket(self, source, destination, timestamp):
        packet= self, source , destination , timestamp
        if packet in self.packetSet:
            return False
        if len(self.queue) >= self.memoryLimit:
            old_src, old_dst, old_ts = self.queue.popleft()
            self.packetSet.remove((old_src,old_dst,old_ts))
        # Remove timestamp from sorted list for that destination
            idx = bisect.bisect_left(self.dest_map[old_dst], old_ts)
            if idx < len(self.dest_map[old_dst]) and self.dest_map[old_dst][idx] == old_ts:
                self.dest_map[old_dst].pop(idx)
            if not self.dest_map[old_dst]:
                del self.dest_map[old_dst]
            # Add packet
        self.queue.append(packet)
        self.packetSet.add(packet)
        bisect.insort(self.dest_map[destination], timestamp)
        return True

    def forwardPacket(self):
        if not self.queue:
            return []

        src, dst, ts = self.queue.popleft()
        self.packetSet.remove((src, dst, ts))

        # Remove timestamp from sorted list
        idx = bisect.bisect_left(self.dest_map[dst], ts)
        if idx < len(self.dest_map[dst]) and self.dest_map[dst][idx] == ts:
            self.dest_map[dst].pop(idx)
        if not self.dest_map[dst]:
            del self.dest_map[dst]

        return [src, dst, ts]

    def getCount(self, destination, startTime, endTime):
        if destination not in self.dest_map:
            return 0

        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left
    


