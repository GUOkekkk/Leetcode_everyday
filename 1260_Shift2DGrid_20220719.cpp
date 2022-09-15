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



/*
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
                int index1 = (i * col + j + k) % (row * col);
                ans[index1 / col][index1 % col] = grid[i][j];
            }
        }
        return ans;
    }
};*/
