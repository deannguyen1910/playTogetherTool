#include<iostream>
#include<cmath>
using namespace std;

float _ex2(float x, int n)
{
    int temp = 1;
    float sum = 1;
    bool next_operator = false;

    if (n == 1) return 1;

    for (int i = 2; i <= n; i+= 2)
    {
        temp *= i - 1;
        temp *= i;

        if (next_operator == false)
        {
            sum -= pow(x, i)/ temp;
            next_operator = true;
        }
        else
        { 
            sum += pow(x, i)/ temp;
            next_operator = false;
        }
    }

    return sum;
}

float _ex3(float x, int n)
{
    int temp = 1;
    float sum = 1;
    bool next_operator = false;

    if (n == 1) return 1;

    for (int i = 3; i <= n; i+= 2) /// sửa chỗ này từ 2 thành 3
    {
        temp *= i - 1;
        temp *= i;

        if (next_operator == false)
        {
            sum -= pow(x, i)/ temp;
            next_operator = true;
        }
        else
        { 
            sum += pow(x, i)/ temp;
            next_operator = false;
        }
    }

    return sum;
}

int main()
{
    cout << _ex2(3, 4);
}