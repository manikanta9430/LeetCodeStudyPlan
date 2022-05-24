class Twitter:
    def __init__(self):
        # user -> post (1, time1) -> (2,time2) -> (3, time3)
        # map user -> followee [user, ...]
        self.postMap = defaultdict(list) # userId: post 
        self.userMap = defaultdict(set) # user: set()followee 
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userMap[userId].add(userId)
        self.postMap[userId].append((self.time, tweetId))
        self.time -= 1 
            

    def getNewsFeed(self, userId: int) -> List[int]:
        res, hq = [], []
        for followee in self.userMap[userId]:
            if not self.postMap[followee]: continue  # it can be empty return by default, user1 get its own feed, if empty then continue
            idx = len(self.postMap[followee]) - 1
            time, tweetId = self.postMap[followee][idx] 
            heapq.heappush(hq, (time, tweetId, followee, idx))
        while hq and len(res) < 10:
            _, tweetId, followee, idx = heapq.heappop(hq)
            res.append(tweetId)
            if idx - 1 >= 0:
                time, tweetId = self.postMap[followee][idx - 1]
                heapq.heappush(hq, (time, tweetId, followee, idx - 1))
        return res 
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].discard(followeeId)
