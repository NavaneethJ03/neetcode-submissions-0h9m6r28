class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count , tweetId])
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        minHeap = []
        res = []
        for follower in self.followMap[userId]:
            if follower in self.tweetMap:
                length = len(self.tweetMap[follower]) - 1
                count , tweetId = self.tweetMap[follower][length]
                heapq.heappush(minHeap , [count , tweetId , follower , length - 1])

        while minHeap and len(res) < 10:
            count , tweetId , followerId , idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                new_count , new_tweetId = self.tweetMap[followerId][idx]
                heapq.heappush(minHeap , [new_count , new_tweetId , followerId , idx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

