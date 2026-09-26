class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count , tweetId])
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        result = []
        maxHeap = []
        for followers in self.followMap[userId]:
            if followers in self.tweetMap:
                index = len(self.tweetMap[followers]) - 1 
                cnt , tweetId = self.tweetMap[followers][index]
                heapq.heappush(maxHeap , [cnt , tweetId , followers , index - 1])
        heapq.heapify(maxHeap)
        while maxHeap and len(result) < 10:
            cnt , tweetId , followerId , idx = heapq.heappop(maxHeap)
            result.append(tweetId)
            if idx >= 0:
                newCnt , newTweetId = self.tweetMap[followerId][idx]
                heapq.heappush(maxHeap , [newCnt , newTweetId , followerId , idx - 1])
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

