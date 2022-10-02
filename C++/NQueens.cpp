#include <bits/stdc++.h>
using namespace std;

#define int long long
#define float double

// Finding All Possible Soltions for NQueens on a chess board

bool isvalid(vector<string> &board, int row, int col, int n)
{
    int i, j;

    for (i = 0; i < col; i++)
        if (board[row][i] == 'Q')
            return false;

    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 'Q')
            return false;

    for (i = row, j = col; j >= 0 && i < n; i++, j--)
        if (board[i][j] == 'Q')
            return false;

    return true;
}

void NQueen(vector<string> &board, int col, int n, vector<vector<string>> &ans)
{
    if (col == n)
    {
        ans.push_back(board);
        return;
    }

    for (int i = 0; i < n; i++)
    {
        if (isvalid(board, i, col, n))
        {
            board[i][col] = 'Q';

            NQueen(board, col + 1, n, ans);

            board[i][col] = '.';
        }
    }
}

signed main()
{
    int n;
    cout << "Enter The Number of Queens : ";
    cin >> n;
    vector<vector<string>> ans;
    vector<string> board(n);
    string s(n, '.');
    for (int i = 0; i < n; i++)
    {
        board[i] = s;
    }
    NQueen(board, 0, n, ans);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << ans[i][j] << "\n";
        }
        cout << "\n";
    }
}