#include <iostream>
using namespace std;
int search(int key)
{
 int i;
 const int n=10;
 int a[n];
 for(i=0;i<n;i++)
 {
        a[i]=i+1;
 }
 int low=0,high=n-1,mid;
 while(low<=high)
 {
	 mid=(low+high)/2;
	 
	 if(a[mid]==key)
		 return mid+1;
	 else if(a[mid]<key)
		 low=mid+1;
	 else
		 high=mid-1;
 }
    return 0;
}
int main11()
{
	int a,num;
	cout<<"����Ҫ���ҵ�����"<<endl;
	cin>>a;
	num=search(a);
	if(num==0)
	{
		cout<<"���������������"<<endl;
	}
	else
		cout<<a<<"������a�е�"<<num<<"������"<<endl;
	return 0;
}