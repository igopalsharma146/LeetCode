class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        # print(freq)
        max_idle_cycles = freq[25] - 1
        total_idle_time = max_idle_cycles * n
        # print(max_idle_cycles,total_idle_time)

        for i in range(25):
            total_idle_time -= min(max_idle_cycles, freq[i])
        # print(max_idle_cycles,total_idle_time)

        if total_idle_time >= 0:
            return len(tasks) + total_idle_time
        return len(tasks)
