#include <iostream>
#include<queue>
#include<vector>
using namespace std;

class node{
    public:
    int data;
    node* left;
    node* right;
    node(int d)
    {
        data=d;
        left=NULL;
        right=NULL;
    }
};
node* create(node* root)
{
    int d;
    cout<<"enter root";
    cin>>d;
    if(d!=-1)
    {
    root=new node(d);
    cout<<"enter left root"; 
    root->left=create(root->left);
     cout<<"enter right root"; 
    root->right=create(root->right);
    return root; 

    }
    else
    return NULL;
} 
void zigzag(node* root)
{
    queue<node*>q;   
    bool l_to_r=true;
    q.push(root);
    while(!q.empty())
    {
     int s=q.size();
     int ans[s];
     for(int i=0;i<s;i++)
      {
         node* temp=q.front();
         q.pop();
         int k=l_to_r?i:s-i-1;
         ans[k]=temp->data;
         if(temp->left)
         q.push(temp->left);
         if(temp->right)
         q.push(temp->right);
        
      }
      l_to_r=!l_to_r;
      for(int i=0;i<s;i++)
         cout<<ans[i]<<" ";
    }
}
int main()
{
    node* root;
    root=create(root);
    zigzag(root);
    return 0;
}