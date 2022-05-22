#include <iostream>
#include <math.h>

using namespace std;

int main()
{

    int n;
    cin >> n;

    string minName;
    string maxName;
    int maxDate = 32;
    int maxMonth = 13;
    int maxYear = 2011;

    int minYear = 0;
    int minDate = 0;
    int minMonth = 0;

    for (int i = 0; i < n; i++)
    {
        int currentDate;
        int currentMonth;
        int currentYear;
        string currentName;

        cin >> currentName >> currentDate >> currentMonth >> currentYear;

        if (currentYear < maxYear)
        {
            maxName = currentName;
            maxDate = currentDate;
            maxMonth = currentMonth;
            maxYear = currentYear;
        }
        else if (currentYear == maxYear)
        {
            if (currentMonth < maxMonth)
            {
                maxName = currentName;
                maxDate = currentDate;
                maxMonth = currentMonth;
                maxYear = currentYear;
            }
            else if (currentMonth == maxMonth)
            {
                if (currentDate < maxDate)
                {
                    maxName = currentName;
                    maxDate = currentDate;
                    maxMonth = currentMonth;
                    maxYear = currentYear;
                }
            }
        }

        if (currentYear > minYear)
        {
            minName = currentName;
            minDate = currentDate;
            minMonth = currentMonth;
            minYear = currentYear;
        }
        else if (currentYear == minYear)
        {
            if (currentMonth > minMonth)
            {
                minName = currentName;
                minDate = currentDate;
                minMonth = currentMonth;
                minYear = currentYear;
            }
            else if (currentMonth == minMonth)
            {
                if (currentDate > minDate)
                {
                    minName = currentName;
                    minDate = currentDate;
                    minMonth = currentMonth;
                    minYear = currentYear;
                }
            }
        }
    }

    cout << minName << "\n";
    cout << maxName << "\n";


    return 0;
}