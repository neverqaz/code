#include <iostream>
#include <iomanip>
using namespace std;
int main7( )
 { 
	int i,j;
	const int m=2,n=3;
    
    int a[m][n]={{1,2,3},{4,5,6}},b[n][m]; 
	/*
	cout<<"input 10 numbers:"<<endl;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
			cin>>a[i][j];      
    cout<<endl;
    */

	cout<<"数组a:"<<endl;
	for(i=0;i<m;i++)
	{	
		for(j=0;j<n;j++)
			cout<<a[i][j]<<" "; 
	    cout<<endl;
	}

    for(i=0;i<n;i++) //转置
		for(j=0;j<m;j++)
			b[i][j]=a[j][i];
  


	cout<<"数组b:"<<endl;
    for(i=0;i<n;i++)
	{	for(j=0;j<m;j++)
			cout<<b[i][j]<<" "; 
	    cout<<endl;
	}
                     
    return 0;
}