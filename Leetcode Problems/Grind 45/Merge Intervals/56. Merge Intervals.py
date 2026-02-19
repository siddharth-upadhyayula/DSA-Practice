class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            laststart, lastend = merged[-1]

            if start <= lastend:
                merged[-1][1] = max(end, lastend)
            else:
                merged.append([start,end])
        return merged

            