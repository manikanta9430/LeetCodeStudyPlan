class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        tracker = {}
        for element in secret:
            if element in tracker:
                tracker[element] += 1
            else:
                tracker[element] = 1
        bulls = 0
        cows = 0
        guessTracker = {}
        for i, elem in enumerate(guess):
            if elem == secret[i]:
                bulls += 1
                if elem in guessTracker:
                    guessTracker[elem] += 1
                    if guessTracker[elem] > tracker[elem]:
                        cows -= 1
                else:
                    guessTracker[elem] = 1
            elif elem in tracker:
                if elem in guessTracker:
                    if tracker[elem] > guessTracker[elem]:
                        cows += 1
                        guessTracker[elem] += 1
                else:
                    cows += 1
                    guessTracker[elem] = 1
        cows = max(cows, 0)
        return (str(bulls) + 'A' + str(cows) + 'B')
