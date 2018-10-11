
#include <iostream>
using namespace std;

void printArray(int array[], int n); 

int main9()
{
  int a[5] = {1, 4, 3, 6, 8};
  printArray(a, 5);
  cout<<endl;
  return 0;
}

void printArray(int array[], int n)
{
  for (int i = 0; i < n; i++)
  {
    cout << array[i] <<  " ";
  }
}

	
