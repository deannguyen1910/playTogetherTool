#include "main.cpp"
#include<iostream>
#include<string>
#include<sstring>
#include<vector>
#include<fstream>
using namespace std;

class subject
{
public:
    string name;
    int time_a, time_b;

private:
    subject();
    subject(string name ,int time_a, int time_b)
    {
        this.name = name;
        this.time_a = time_a;
        this.time_b = time_b;
    }
};

class day //all subject listed in a day
{
public:
    vector<subject> data;
private:
    day()
    {
        return check_collapse();
    }

    bool check_collapse()
    {
        for (int i = 0; i < data.size(); i++)
        {
            for (int j = 1; j < data.size(); j++)
            {
                if (i == j) continue;

                if !(data[i].time_a  > data[j].time_b || data[i].time_b < data[j].time_a)
                {
                    return false;
                }
            }
        }

        return true;
    }

    vector<bool> the_number_calendar()
    {
        vector<bool> time(288, 0);

        for (int i = 0; i < data.size(); i++)
        {
            for (int j = data[i].time_a / 5; j < data[i].time_b / 5; j++)
            {
                time[j] = 1;
            }
        }

        return time;
    }

    string input (string data_wrap)
    {
        data_wrap.tryParse()
    }
};

class schedule
{
public: 
    vector<day> data(7);

private:
    schedule(){}

    schedule push(float timezone, float timezone_convert)
    {
        vector<day> data_temp(7);
        vector<bool> temp;
        for (int i = 0; i < data.size(); i++)
        {
            temp.push_back(data[i].the_number_calendar());
        }

        float diff = timezone_convert - timezone;
        diff *= 10;
        int (diff);
        diff /= 5;

        if (diff > 0)
        {
            vector<bool> temp2 = temp.assign(temp.end() - 1 - abs(diff), temp.size() - 1);
            temp.erase (temp.end() - 1 - abs(diff), temp.size() - 1);
            temp2.push_back(temp);
            temp = temp2;
        }
        else
        {
            vector<bool> temp2 = temp.assign(temp.begin(), temp.begin() + abs(diff) - 1);
            temp.erase(temp.begin(), temp.begin() + abs(diff) - 1);
            temp.push_back(temp2);
        }
    }

    schedule input(vector<string> data_wrap)
    {
        for (int i = 0l i< data.size(); i++)
        {
            data[i].input(data.wrap[i]);
        }
    }

    fstream* import(string name)
    {
        fstream file.open(name, ios::in);

        file >> string;
        
        vector<string> temp;
        int count = 0;

        while (!file.eof())
        {
            string line;
            getline (cin, line);

            temp.push_back(line);
        }

        input (temp);
    }
};

int main()
{

}
