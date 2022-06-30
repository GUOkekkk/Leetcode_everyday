//
// Created by guo on 2021/9/20.
//
//Given an integer array nums_array, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
//A subarray is a contiguous part of an array.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums_array) {
        int pre = 0, MaxSum = nums_array[0];
        for (const auto &x: nums_array) { // use pointer x
            // cout << x << endl;
            // How to find the subarray?
            // A: By using the below function
            pre = max(pre + x, x); // if pre < 0  and x > 0 return the x, else return the pre + x
                                   // if pre < 0 and x < 0  return the x
            MaxSum = max(MaxSum, pre); // twice max //if all behind the num[0] is < 0. return the num[0].
        }
        return MaxSum;
    }
};

int main()
{
    vector<int> test = {-2, -5, -7, 9, -7};
    Solution s1;
    cout << s1.maxSubArray(test) << endl;
}
