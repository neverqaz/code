#include <iostream>
#include <iomanip>
using namespace std;
int main3( )
 { 
	int i,k=0,p=0;
	const int n=10;
    
    int a[n];   
	for(i=0;i<n;i++)
		cin>>a[i];      
        
    for(i=1;i<n;i++)
	{
		if(a[k]<a[i])
			k=i;      
        if(a[p]>a[i])
			p=i; 
	}
    
	cout<<"max="<<a[k]<<",下标为："<<k<<endl;          
    cout<<"min="<<a[p]<<",下标为："<<p<<endl;       
                     
    return 0;
}