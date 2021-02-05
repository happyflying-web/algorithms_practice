#include<iostream>
#include<stdio.h>
using namespace std;
/**
 * k表示第k个皇后在第k行的第x[k]列
 * x[k]的初始值是-1
 * */
void Queen()
{
    int k=0;
    while(k>=0)
    {
        x[k]++;
        while (x[k]<n&&Place(k)==1)
        {
            x[k]++;
        }

        if(x[k]<n&&k==n-1)
        {
            for(int i=0;i<n;i++)
            {
                cout<<x[i]+1<<endl;
            }
            cout<<endl;
            return ;
        }
        if(x[k]<n&&k<n-1)
        {
            k++;
        }
        else{
            x[k--]=-1;//重置，回溯
        }

    }
    cout<<"无解"<<endl;
}
int Place(int k)
{
    for(int i=0;i<k;i++)
    {
        if(x[i]==x[k]||abs(i-k)==abs(x[i]-x[k]))
        return 1; // 如果冲突返回1
    }
    return 0;  //不冲突返回0
}