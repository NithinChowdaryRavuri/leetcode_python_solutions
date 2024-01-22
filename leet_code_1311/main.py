class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        dct=defaultdict(lambda :0)
        n=len(friends)
        st=[(id,0)]
        visited=[0]*n
        visited[id]=1
        while st:
            x,d=st.pop(0)
            for i in friends[x]:
                if visited[i]==0 and d+1<=level:
                    if d+1==level:
                        for j in watchedVideos[i]:
                            dct[j]+=1
                    st.append((i,d+1))
                    visited[i]=1
        return sorted(dct,key=lambda x: (dct[x],x))        
        