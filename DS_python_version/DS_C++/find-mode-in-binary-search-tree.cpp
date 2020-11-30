#include<vector>
using namespace std;
//   Definition for a binary tree node.
  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 };

class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<TreeNode*>temp;
        temp=middlesearch(root,temp);
        // int maxcount=0;
        // int currentcount=0;
        // int currentnum=1;
        int i=0;
        struct record
        {
            // int data;
            int currentnum=0;
            int currentcount=1;
            /* data */
        };
        record re[1000];
        record maxNode;
        vector<int> result;
        int j=0;
        while(i<temp.size())
        {
            re[j].currentnum=temp[i]->val;
            while(temp[i]->val==temp[i+1]->val)
            {
                re[j].currentcount++;
                i++;
            }
            i++;
            j++;
            if (re[j].currentcount>maxNode.currentcount)
            maxNode=re[j];
        }
        // return maxNode.currentnum;
        for(int i=0;i<=j;i++)
        {
            if(re[i].currentcount==maxNode.currentcount)
            {
                result.push_back(re[i].currentnum);
            }
        }
        return result;
    }
    vector<TreeNode*>middlesearch(TreeNode * root,vector<TreeNode*> temp)
    {
        if(root)
        {
            middlesearch(root->left,temp);
            temp.push_back(root);
            middlesearch(root->right,temp);
        }
        return temp;
    }
};