// https://leetcode-cn.com/problems/group-anagrams/
#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>> res;
        for(auto temp:strs)
        {
            string item=temp;
            sort(item.begin(),item.end());
            res[item].push_back(temp);
        }
        vector<vector<string>> result;
        for(auto it=res.begin();it!=res.end();it++)
        {
            result.push_back(it->second);
        }
        return result;
    }
};
