#include <iostream>
#include<cstring>
#include<vector>
using namespace std;
void solve(string str,int i,vector<string>&ans,string p,int j)
{
    if(str!=p)
    {
        cout<<i;
        ans.push_back(p);
        return;
    } 
    swap(p[i],p[j]);
    if(i!=p.length()-2)
        solve(str,i++,ans,p,i++);
    solve(str,0,ans,p,i);
}
int main()
{
    string str;
    cin>>str;
    vector<string>ans;
    string output;
    solve(str,0,ans,str,1);
    for(int i=0;i<ans.size();i++)
    cout<<ans[i]<<" ";
}
