class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1. Check if there is Enough Gas to complete Round Trip 
        if sum(gas) < sum(cost):
            return -1  # not enough gas available

        # 2. Find start station Greedily
        start = 0  # start station, representing unique circuit (ie trip)
        total = 0  # total gas remain in car at moment for current trip

        for i in range(len(gas)):
            # 1. Fill the gas from curr station {i}
            total += gas[i]

            # 2. check if car can embark to next station
            if total >= (c := cost[i]):
                # 2.1 car has enough gas to move to next station {i+1}
                total -= c # so move to next station {i+1}
            else:
                # 2.2 no enough gas so need to consider another circuit/trip 
                start = i+1  # considering next station as starting point (ie of next trip exploration)
                total = 0  # as startin new circuit from next station {i+1}

        # there exists atleast 1 start (is ensured)
        return start
