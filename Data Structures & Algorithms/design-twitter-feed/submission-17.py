class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([tweetId , self.count])
        self.count -= 1 
    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        self.followMap[userId].add(userId)
        maxHeap = []
        for followerId in self.followMap[userId]:
            if followerId in self.tweetMap:
                idx = len(self.tweetMap[followerId]) - 1 
                tweetId , cnt = self.tweetMap[followerId][idx]
                heapq.heappush(maxHeap , [cnt , tweetId , followerId , idx - 1])

        while maxHeap and len(result) < 10:
            cnt , tweetId , followerId , idx = heapq.heappop(maxHeap)
            result.append(tweetId)
            if idx >= 0:
                newTweetId , newCnt  = self.tweetMap[followerId][idx]
                heapq.heappush(maxHeap , [newCnt , newTweetId , followerId , idx - 1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId) 
