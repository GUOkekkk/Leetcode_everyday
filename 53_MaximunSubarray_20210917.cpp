//
// Created by guo on 2021/9/20.
//
//Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
//A subarray is a contiguous part of an array.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre = 0, Max = nums[0];
        for (const auto &x: nums) { // use pointer
            pre = max(pre + x, x);
            Max = max(Max, pre); // twice max
        }
        return Max;
    }
};

int main()
{
    vector<int> test = {2, 5, 7, 9, 7};
    Solution s1;
    cout << s1.maxSubArray(test) << endl;
}
