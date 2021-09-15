/*
// Created by Ke GUO on 2021/09/14
// Leetcode Everyday: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
//An input string is valid if:
//Open brackets must be closed by the same type of brackets.
//Open brackets must be closed in the correct order.



#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    bool isValid(string s) {
        vector <char> v1{0}; // use vector to store the all kinds of dynamic information. Set a initial value to avoid some error.
        int n = s.size();
        if (n % 2 == 1)
        {
            return false;
        }

        for (char pare:s)
        {
            if(pare == '(' || pare == '[' || pare == '{')
            {
                v1.push_back(pare); // push_back: put the value into the vector
            }else if(pare == ')' && v1.back() == '(' //back: the last value
                     ||pare == ']' && v1.back() == '['
                     ||pare == '}' && v1.back() == '{')
            {
                v1.pop_back(); // pop_back: delete the last value
            }else
            {
                return false;

            }
        }
        v1.pop_back(); // remove the initial value
        return v1.empty();

    }
};

int main() {
    string s = "(]";
    Solution S1; // how to use class, first create one
    cout << boolalpha << S1.isValid(s) << endl; // put in the variable and use the function
    return 0;
}
*/
