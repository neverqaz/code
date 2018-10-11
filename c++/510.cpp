# include <iostream>
using namespace std;

	
int main10()
{   //const int n=6;
    void select_sort(int array[],int n);
	int a[6]={9,8,5,4,2,0},i;

    cout<<"数组a排序前："<<endl;
	for(i=0;i<6;i++)
		cout<<a[i]<<",";
	cout<<endl;

	select_sort(a,6);

	cout<<"数组a排序后："<<endl;
	for(i=0;i<6;i++)
		cout<<a[i]<<",";
	cout<<endl;

	return 0;
}
void select_sort(int array[],int n)
{
	int i,j,t,k;
	for(i=0;i<n-1;i++)
	{
		k=i;
		for(j=i+1;j<n;j++)
		{
			if(array[k]>array[j]) k=j;
		}
		t=array[k];
		array[k]=array[i];
		array[i]=t;
	}
}