class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda item: item[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if (start <= output[-1][1]):
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start, end])

        for x in range (200000):
            continue

        return output

     

        