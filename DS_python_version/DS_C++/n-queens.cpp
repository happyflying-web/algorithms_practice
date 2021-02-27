// https://leetcode-cn.com/problems/n-queens/
#include<vector>
#include<string>
using namespace std;
class Solution {
public:
    vector<int> x;
    vector<vector<string>> solveNQueens(int n) {
        for(int i=0;i<n;i++)
        {
            x.push_back(-1);

        }// 初始化

        vector<vector<string>> result;
        result=Queen( n);
        return result;

    }
    vector<vector<string>> Queen(int n)
    {
        int k=0;
        vector<vector<string>> result;
        while (k>=0)
        {
            x[k]++;
            while (x[k]<n&&Place(k)==1)
            {
                x[k]++;
                /* code */
            }
            if(x[k]<n&&k==n-1)
            {
                for(int i=0;i<n;i++)
                {
                    for(int j=0;j<n;j++)
                    {
                        if(j==x[i])
                        {
                            result[i][j]="Q";
                        }
                        else{
                            result[i][j]=".";
                        }
                    }
                }
                // return result;
            }

            if(x[k]<n&&k<n-1)
            {
                k++;
            }
            else{
                x[k--]=-1;
            }
            
        }
        return result;
    }
    int Place(int k)
    {
        for(int i=0;i<k;i++)
        {
            if(x[i]==x[k]||abs(i-k)==abs(x[i]-x[k]))
            return 1;
        }
        return 0;
    }
};                                 

int main ()
{
    
}