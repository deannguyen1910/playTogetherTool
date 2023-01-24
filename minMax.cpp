#include<iostream>
#include<conio.h>
#include<vector>
using namespace std;



int main()
{
    int key_press = 0;
    vector<float> numbers;

    while (1)
    {
        float temp;
        cin >> temp;
        numbers.push_back(temp);

        key_press = _getch();
        if (key_press == 0)
        {
            key_press = -_getch();
            if (key_press == -64)
            {
                break;
            }
        }


        cout << key_press;
    }

    for (int i = 0; i <= numbers.size(); i++)
    {
        cout << numbers[i] << " ";
    }

    return 3;

}
