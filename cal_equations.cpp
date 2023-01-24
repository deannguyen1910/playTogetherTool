#include<iostream>
#include<string>
#include<sstream>
#include<vector>
using namespace std;



class fraction
{
private:
    int x;
    int y;

public:
    fraction() {}

    fraction(int x_temp, int y_temp)
    {
        if (y_temp == 0)
        {
            return;
        }

        x = x_temp;
        y = y_temp;
    }

    string _output()
    {
        stringstream ss;
        ss << x;

        if (y != 1)
        {
           ss << "/" << y;
        }
        
        return ss.str();
    }

    fraction _reduceFraction()
    {
        int min;
       
        if (x < 0 && y < 0)
        {
            x = abs(x);
            y = abs(y);
        }

        if (abs(x) < abs(y))
        {
            min = x;
        }
        else
        {
            min = y;
        }

        for (int i = min; i > 0; i--)
        {
            if (abs(x) % i == 0 && abs(y) % i == 0)
            {
                x /= i;
                y /= i;

                return *this;
            }
        }

        return *this;
    }

    fraction _operationAdd(fraction a, fraction b)
    {
        fraction temp;

        temp.x = a.x * b.y + b.x * a.y;
        temp.y = a.y * b.y;

        return temp;
    }
};

class setOfEquation
{
private:
    vector<vector<float>> equations;

    vector<string> result;

public:
    setOfEquation()
    {
        //input
    }

    bool checkSame(vector<float> x1, vector<float> x2)
    {
        float temp = x1[0]/x2[0];
        
        for (int i = 1; i < x1.size(); i++)
        {
            if (x1[i] / x2[i] != temp) return false;
        }

        return true;
    }

    void calGauss(vector<float> x1, vector<float> x2, int Column)
    {
        if (x1[Column] == 0) 
        {
            return;
        }

        if (x2[Column] == 0)
        {
            vector<float> temp = x2;
            x2 = x1;
            x1 = x2;

            return;
        }
    }

    void Gauss_ing()
    {
        int count = 1;

        for (int i = count; i < equations.size(); i++)
        {            
            calGauss(equations[i - 1], equations[i], count - 1);

            if (i == equations.size() - 1)
            {
                count++;
                i = count;
            }
        
        }
    }

    void solve()
    {
        for (int i = 0; i < equations.size() - 1; i++)
        {
            for (int j = i + 1; j < equations.size(); j++)
            {
                if (checkSame(equations[i], equations[j]))
                {
                    
                }
            }
        }

        if (equations[0][0] == 0) // No solution
        {
            for (int i = 1; i < equations.size(); i++)
            {
                if(equations[i][0] != 0)
                {
                    vector<float> temp;
                    temp = equations[i];
                    equations[i] = equations[0];
                    equations[0] = temp;
                }
            }

            if (equations[0][0])
            {
                result.insert(result.begin(), 1, "infinity");

                return;
            }
        }

        for (int i = 0; i < equations.size(); i++) // trivial solution
        {
            if (equations[i].back() == 0)
            {

            }
        }

        Gauss_ing();
    }

    void resultTheSolving()
    {

    }
};

int main ()
{
    
}