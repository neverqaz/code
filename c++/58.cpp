#include <iostream>
#include <iomanip>
using namespace std;
int main8( )
 { 
	int i,j,t;
	const int n=4;
    
    int a[n][n]={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}}; 
	/*
	cout<<"input 10 numbers:"<<endl;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
			cin>>a[i][j];      
    cout<<endl;
    */

	cout<<"数组a:"<<endl;
	for(i=0;i<n;i++)
	{	
		for(j=0;j<n;j++)
			cout<<setw(4)<<a[i][j]<<" "; 
	    cout<<endl;
	}

    for(i=0;i<n;i++) //转置
		for(j=0;j<i;j++)
		{
			t=a[i][j];
			a[i][j]=a[j][i];
			a[j][i]=t;
		}
  


	cout<<"数组a转置后:"<<endl;
    for(i=0;i<n;i++)
	{	for(j=0;j<n;j++)
			cout<<setw(4)<<a[i][j]<<" "; 
	    cout<<endl;
	}
	return 0;
}