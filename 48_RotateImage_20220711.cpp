/*
//
// Created by gkbb on 2022/7/12.
//You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
//
//You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
// How to success it without creating a new matrix??
// Using flip to replace the rotate

#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    void rotate(vector<vector<int>>& matrix) {
        int matrix_length = matrix.size();
        // horizontal flip
        for(int i = 0; i < matrix_length/2 ; i++){
            for(int j = 0; j < matrix_length; j++){
                swap(matrix[i][j], matrix[matrix_length-i-1][j]);
            }
        }

        // main diagonal flip
        for (int i = 0; i < matrix_length; i++) {
            for (int j = 0; j < i; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};

int main() {
    vector<vector<int>> matrix = {{5,1,9,11},
                                  {2,4,8,10},
                                  {13,3,6,7},
                                  {15,14,12,16}};
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
    S1.rotate(matrix); // rotate the matrix

    // print the matrix after the rotate
    cout << "Rotating..." << endl;
    for(int i = 0; i < length_matrix; i++){
        cout<<"[";
        for(int j = 0; j < length_matrix; j++){
            cout<<matrix[i][j]<<"\t";
        }
        cout<<"]"<<endl;
    }
    return 0;
}
*/
