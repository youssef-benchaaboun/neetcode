class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        count_i=defaultdict(int)
        count_j=defaultdict(int)
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j]=='B':
                    count_i[i] +=1
                    count_j[j] +=1
        result=0
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if count_i[i]==1 and count_j[j]==1 and picture[i][j]=='B':
                    result +=1
        return result