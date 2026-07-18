class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count , tweetId])
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res , heap = [] , []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count , tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap , [count , tweetId , followeeId , index - 1])
        
        while len(res) < 10 and heap:
            count , tweetId , followeeId , index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                next_count , next_tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap , [next_count , next_tweetId , followeeId , index - 1])

        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
