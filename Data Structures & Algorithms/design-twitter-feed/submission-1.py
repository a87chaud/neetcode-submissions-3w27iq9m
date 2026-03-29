class Twitter:

    def __init__(self):
        self.userTweet = defaultdict(list) # user id -> [](both)
        self.userFollowers = defaultdict(set) # user id -> their followers
        self.ts = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.userTweet[userId]
        self.ts += 1
        self.userTweet[userId].append((-1 * (self.ts), tweetId))
    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = self.userTweet[userId].copy()
        followerIds = self.userFollowers[userId]
        for fId in followerIds:
            maxHeap.extend(self.userTweet[fId].copy())
        heapq.heapify(maxHeap)
        print(maxHeap)
        result = []
        i = 0
        while maxHeap and i < 10:
            ts, tweetId = heapq.heappop(maxHeap)
            result.append(tweetId)
            i += 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowers[followerId]:
            self.userFollowers[followerId].remove(followeeId)
