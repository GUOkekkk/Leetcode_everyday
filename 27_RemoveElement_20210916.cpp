/*
//
// Created by guo on 2021/9/16.
//
//Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
//
//Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
//
//Return k after placing the final result in the first k slots of nums.
//
//Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
//


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0, right = nums.size(); // cause the space complexity is O(1) so cant create a new vector just adjust in this vector. O(1) means do not depend on the input
        while (left < right) {
            if (nums[left] == val) {
                nums[left] = nums[right - 1];
                right--; // by this way, reduce the time only traverse once
            } else {
                left++;
            }
        }
        return left;
    }
};

int main()
{
    vector<int> test = {2, 5, 7, 9, 7};
    int test_val = 7;
    Solution s1;
    cout << s1.removeElement(test, test_val) << endl;
}*/
