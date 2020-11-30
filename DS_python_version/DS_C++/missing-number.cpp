#include<vector>
using namespace std;
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        vector<int> judge;
        for(int i=0;i<=nums.size()+1;i++)
        {
            judge.push_back(0);
        }
        for(int i=0;i<nums.size();i++)
        {
            judge[nums[i]]=1;
        }
        int temp=0;
        for(int i=0;i<judge.size();i++)
        {
            if(judge[i]==0)
            {
                temp=i;
                break;
            }
        }
        return temp;
    }
};