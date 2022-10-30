/*
//
// Created by gkbb on 2022/9/16.
// Write a program to solve a Sudoku puzzle by filling the empty cells.
//
//A sudoku solution must satisfy all of the following rules:
//
//Each of the digits 1-9 must occur exactly once in each row.
//Each of the digits 1-9 must occur exactly once in each column.
//Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
//The '.' character indicates empty cells.

//
#include <iostream>
using namespace std;




class Solution{
public:
    int grille[9][9];
    bool ifsuccess = false;
    int length = sizeof(grille)/ sizeof(grille[0][0]);

    void affiche_grille() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                cout << grille[i][j];
            }
            cout << endl; // next line
        }
    }

    bool grille_finie() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (grille[i][j] == 0) {
                    return false;
                    cout << i << endl;
                }
            }
        }
        return true;
    }

    bool case_possible(int x, int row, int col){
        for (int i = 0; i < 9; i++) {
            if (grille[row][i] == x) {
                return false;
            }
        }
        for (int j = 0; j < 9; j++) {
            if (grille[j][col] == x) {
                return false;
            }
        }

        int i0 = row / 3 * 3;
        int j0 = col / 3 * 3;

        // cout << i0 << j0 << endl;

        for (int i = i0; i < i0 + 3; i++) {
            for (int j = j0; j < j0 + 3; j++) {
                if (grille[i][j] == x) {
                    return false;
                }
            }
        }

        return true;
    }

    bool solve(int n) {
        if (n == length)
        {
            ifsuccess = true;
            return ifsuccess;
        }
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (grille[i][j] != 0) continue;
                for (int x = 1; x <= 9; x++) {
                    if (case_possible(x, i, j))
                    {
                        grille[i][j] = x;
                        if (solve(n+1)) return true;
                        grille[i][j] = 0;
                    }
                }
                return false;
            }
        }
    }




};

int main()
{
    int grille[9][9] = { {1,0,0,0,0,0,0,9,5},{3,0,0,4,0,0,1,0,0},{0,6,0,0,2,0,0,0,0},
                         {0,0,0,0,0,0,0,0,0},{0,0,1,0,0,0,7,6,0},{7,3,2,5,0,9,0,0,0},
                         {4,0,0,3,1,0,0,7,0},{0,0,0,0,0,0,9,5,0},{5,0,0,2,0,7,3,0,0} };

    Solution s1;

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            s1.grille[i][j] = grille[i][j];
        }
        }

    s1.affiche_grille();
    cout<< s1.grille_finie()<<endl;
    cout<< s1.case_possible(6, 0, 3)<<endl;
    s1.solve(0);
    s1.affiche_grille();
    cout<< s1.grille_finie()<<endl;
}*/
