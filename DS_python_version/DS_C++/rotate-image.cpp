// https://leetcode-cn.com/problems/rotate-image/
using namespace std;
#include<vector>
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        vector<int> vec;
        for(int i=0;i<matrix.size();i++)
        {
            for(int j=0;j<matrix[0].size();j++)
            {
                vec.push_back(matrix[i][j]);
            }
        }
        reverse(vec.begin(),vec.end());
        for(int j=matrix.size()-1;j>=0;j--)
        {
            for(int i=0;i<matrix.size();i++)
            {
                matrix[i][j]=vec.back();
                vec.pop_back();
            }
        }
    }
};