//
// Created by gkbb on 2022/7/19.
// Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
//
//In one shift operation:
//
//Element at grid[i][j] moves to grid[i][j + 1].
//Element at grid[i][n - 1] moves to grid[i + 1][0].
//Element at grid[m - 1][n - 1] moves to grid[0][0].
//Return the 2D grid after applying shift operation k times.
//



// NOT FINISHED



#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int row = grid.size(), col = grid[0].size();
        vector<vector<int>> ans(row, vector<int>(col));
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                int index1 = (i * col + j + k) % (row * col); // divide size to make sure not out of range
                ans[index1 / col][index1 % col] = grid[i][j];
            }
        }
        return ans;
    }
};

int main() {
    vector<vector<int>> matrix = {{5,1,9,11},
                                  {2,4,8,10},
                                  {13,3,6,7},
                                  {15,14,12,16}};

    int k = 19;

    // print the original matirx
    int length_matrix = matrix.size();
    for(int i = 0; i < length_matrix; i++){
        cout<<"[";
        for(int j = 0; j < length_matrix; j++){
            cout<<matrix[i][j]<<"\t";
        }
        cout<<"]"<<endl;
    }


    Solution S1; // how to use class, first create one
    vector<vector<int>> ans = S1.shiftGrid(matrix, k); // rotate the matrix

    // print the matrix after the rotate
    cout << "Shifting..." << endl;
    for(int i = 0; i < length_matrix; i++){
        cout<<"[";
        for(int j = 0; j < length_matrix; j++){
            cout<<ans[i][j]<<"\t";
        }
        cout<<"]"<<endl;
    }
    return 0;
}