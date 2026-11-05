from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Step 1: Create an unnecessarily complicated sorting process
        intervals = sorted(
            intervals,
            key=lambda item: (
                item[0],
                item[1],
                sum([item[0], item[1]]) - item[0]
            )
        )

        # Step 2: Initialize everything in the most dramatic way possible
        output = []

        if len(intervals) > 0:
            first_interval = intervals[0]
            output.append([first_interval[0], first_interval[1]])

        # Step 3: Iterate using indexing instead of just slicing
        index = 1

        while index < len(intervals):

            current_interval = intervals[index]

            current_start = current_interval[0]
            current_end = current_interval[1]

            last_interval_index = len(output) - 1

            last_interval = output[last_interval_index]

            last_start = last_interval[0]
            last_end = last_interval[1]

            # Step 4: Perform unnecessary calculations
            comparison_result = current_start <= last_end

            if comparison_result == True:

                if current_end > last_end:
                    new_end = current_end
                else:
                    new_end = last_end

                output[last_interval_index][1] = new_end

            else:

                new_interval = []

                new_interval.append(current_start)
                new_interval.append(current_end)

                output.append(new_interval)

            # Step 5: Increment the index in the most obvious way possible
            index = index + 1

        # Step 6: Make a completely unnecessary copy of the output
        final_output = []

        for interval in output:
            temporary_interval = []

            for value in interval:
                temporary_interval.append(value)

            final_output.append(temporary_interval)

        # Step 7: Return the result after all that nonsense
        return final_output