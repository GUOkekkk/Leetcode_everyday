#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    bool isValid(string s) {
        vector <char> v1{0};
        int n = s.size();
        if (n % 2 == 1)
        {
            return false;
        }

        for (char pare:s)
        {
            if(pare == '(' || pare == '[' || pare == '{')
            {
                v1.push_back(pare);
            }else if(pare == ')' && v1.back() == '('
                     ||pare == ']' && v1.back() == '['
                     ||pare == '}' && v1.back() == '{')
            {
                v1.pop_back();
            }else
            {
                return false;

            }
        }
        return v1.empty();

    }
};

int main() {
    string s = "()";
    Solution;
    return 0;
}
