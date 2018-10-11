#include <iostream> 
using namespace std; 
  
void display(int array[],int size)
{  
	cout<<"the array is:"<<endl;  
	int i;  
	for(i=0;i<size;i++)
		cout<<array[i]<<" ";  
	cout<<"\n";  
}  
  
void sequence(int array[],int size,int num)
{  
	int i;  
	for(i=0;i<size;i++)
	{  
		if(array[i] == num)
		{  
			cout<<"要查找的数是："<<num<<", the index is "<<i<<endl;  
			break;  
		}  
	}  
	if(i == size)
		cout<<"this num is not found"<<endl;  
}  
  
int main()
{  
	int array[10]={34,45,1,39,21,68,65,100,4,51};  
	display(array,10);  
	sequence(array,10,68);  
	return 0;  
} 