/*
//
// Created by gkbb on 2022/7/12.
//There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
//
//For each location indices[i], do both of the following:
//
//Increment all the cells on row ri.
//Increment all the cells on column ci.
//Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
// Actually it is easy to solve this question by simulating it directly
// But how to solve it with time complexity=O(q+m+n) and space complexity=O(m+n)?


#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        vector<int> rows(m), cols(n);
        for(auto & index : indices){
            rows[index[0]]++;
            cols[index[1]]++;
        }
        int odd_num = 0;
        // it is easy to solve it by check the sum of the rows[i] and cols[j] & 1; & is the bit operation
        // but the time complexity is O(q+m*n) therefore should find the regular of the question

        int oddr = 0, oddc = 0;
        for (int i = 0; i < m; i++) {
            if (rows[i] & 1) {
                oddr++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (cols[i] & 1) {
                oddc++;
            }
        }

        // only odd transformation is useful but the intersection is the even and counted twice
        return oddr*n + oddc*m - 2*oddr*oddc;



    }

};

int main() {
    int n = 3;
    int m = 2;
    vector<vector<int>> indices = {{0,1}, {1,1}};
    Solution S1; // how to use class, first create one
    cout << S1.oddCells(m, n, indices) << endl; // put in the variable and use the function
    return 0;
}
*/
