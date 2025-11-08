#include <iostream>
#include <string>
using namespace std;

string converter(int n);

int main()
{
       int number;
       cout << "Enter the number: ";
       cin >> number;
       cout << "Binary number: " << converter(number) << endl;
       return 0;
}

string converter(int n)
{
       string binary = "";
       if (n == 0)
              return "0";

       while (n > 0)
       {
              binary = to_string(n % 2) + binary; // Add each digit at the start
              n = n / 2;
       }
       return binary;
}
