#include <iostream>
#include <iomanip>
using namespace std;
int main4( )
 { 
	int i,j,t;
	const int n=10;
    
    int a[n]; 
	cout<<"input 10 numbers:"<<endl;
	for(i=0;i<n;i++)
		cin>>a[i];      
    cout<<endl;
    
    for(i=1;i<n;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(a[j]>a[j+1])
			{
				t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;

			}
		}
	}
    
	cout<<"after the sorted, the number is:"<<endl;
	for(i=0;i<n;i++)
		cout<<a[i]<<" "; 
	cout<<endl;
                     
    return 0;
}