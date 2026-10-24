class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str):
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month - 1]) + day

        alice_start = date_to_day_of_year(arriveAlice)
        alice_end = date_to_day_of_year(leaveAlice)
        bob_start = date_to_day_of_year(arriveBob)
        bob_end = date_to_day_of_year(leaveBob)
        
        start_overlap = max(alice_start, bob_start)
        end_overlap = min(alice_end, bob_end)
        
        return max(0, end_overlap - start_overlap + 1)
