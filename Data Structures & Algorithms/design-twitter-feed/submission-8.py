class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # add the followeeid's to the set of the follower
        self.tweetMap = defaultdict(list)# add the tweet's to the userid
        self.count = 0 # to keep track of the tweetid 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count , tweetId])
        self.count -= 1 # since we are minHeap to simulate the maxHeap

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        res = []
        heap = []
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 
                count , tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap , [count , tweetId , followeeId , index - 1])

        while len(res) < 10 and heap:
            count , tweetId , followeeId , index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                new_count , new_tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap , [new_count , new_tweetId , followeeId , index - 1])

        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
