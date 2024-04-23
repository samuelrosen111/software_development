#include <iostream>
#include <iomanip>
#include <limits>
#include <functional> // for inner functions
using namespace std;

void numbers() {
    auto print_all_number_types = []() {
        cout << "\nFollowing are all number types and their sie in bits: \n" << endl;

        cout << left << setw(20) << "Type" 
            << setw(20) << "Bits" 
            << setw(25) << "Min" 
            << setw(25) << "\tMax" << endl;

        cout << left << setw(20) << "int" 
            << setw(20) << sizeof(int) * 8 
            << setw(25) << numeric_limits<int>::min() 
            << "\t" << numeric_limits<int>::max() << endl;

        cout << left << setw(20) << "unsigned int" 
            << setw(20) << sizeof(unsigned int) * 8 
            << setw(25) << 0 
            << "\t" << numeric_limits<unsigned int>::max() << endl;

        cout << left << setw(20) << "short" 
            << setw(20) << sizeof(short) * 8 
            << setw(25) << numeric_limits<short>::min() 
            << "\t" << numeric_limits<short>::max() << endl;

        cout << left << setw(20) << "unsigned short" 
            << setw(20) << sizeof(unsigned short) * 8 
            << setw(25) << 0 
            << "\t" << numeric_limits<unsigned short>::max() << endl;

        cout << left << setw(20) << "long" 
            << setw(20) << sizeof(long) * 8 
            << setw(25) << numeric_limits<long>::min() 
            << "\t" << numeric_limits<long>::max() << endl;

        cout << left << setw(20) << "unsigned long" 
            << setw(20) << sizeof(unsigned long) * 8 
            << setw(25) << 0 
            << "\t" << numeric_limits<unsigned long>::max() << endl;

        cout << left << setw(20) << "long long" 
            << setw(20) << sizeof(long long) * 8 
            << setw(25) << numeric_limits<long long>::min() 
            << "\t" << numeric_limits<long long>::max() << endl;

        cout << left << setw(20) << "unsigned long long" 
            << setw(20) << sizeof(unsigned long long) * 8 
            << setw(25) << 0 
            << "\t" << numeric_limits<unsigned long long>::max() << endl;

        cout << left << setw(20) << "float" 
            << setw(20) << sizeof(float) * 8 
            << setw(25) << numeric_limits<float>::lowest() 
            << "\t" << numeric_limits<float>::max() << endl;

        cout << left << setw(20) << "double" 
            << setw(20) << sizeof(double) * 8 
            << setw(25) << numeric_limits<double>::lowest() 
            << "\t" << numeric_limits<double>::max() << endl;

        cout << left << setw(20) << "long double" 
            << setw(20) << sizeof(long double) * 8 
            << setw(25) << numeric_limits<long double>::lowest() 
            << "\t" << numeric_limits<long double>::max() << endl;
    };

    print_all_number_types();
}

int main() {
    numbers();
    return 0;
}
