class Solution {
public:
    int countOdds(int low, int high) {
        int pre=(low)/2;
        int all=(high+1)/2;
        int result=all-pre;
        return result;
    }
};