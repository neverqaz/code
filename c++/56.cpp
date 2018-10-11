#include <iostream>
#include <iomanip>
using namespace std;
int main6( )
 { 
	int i,j,t,p,q;
	const int m=3,n=4;
    
    int a[m][n]={{1,2,3,4},{5,6,7,8},{9,10,11,12}},sumhe=0,sumrow[m]={0},sumcolum[n]={0},maxrow[m],maxcolum[n]; 
	/*
	cout<<"input 10 numbers:"<<endl;
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
			cin>>a[i][j];      
    cout<<endl;
    */

	p=0,q=0;
    for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if(a[p][q]<a[i][j])
			{
				p=i;
				q=j;
			}
		}
	}
    
	cout<<"max=:"<<a[p][q]<<"，行号是："<<p<<"，列号是："<<q<<endl;
	
	/*
    cout<<"每一行的和是:"<<endl;
	for(i=0;i<m;i++)
		cout<<sumrow[i]<<" "; 
	cout<<endl;
	
	cout<<"每一列的和是："<<endl;
	for(j=0;j<n;j++)
		cout<<sumcolum[j]<<" "; 
	cout<<endl;
	*/
                     
    return 0;
}