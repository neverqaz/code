#include <iostream>
#include <iomanip>
using namespace std;
int main2( )
  { int i;
    int f[20]={1,1};            //f［0］=1,f［1］=1
    for(i=2;i<20;i++)
          f[i]=f[i-2]+f[i-1];      //在i的值为2时，f［2］=f［0］+f［1］，依此类推
    for(i=0;i<20;i++)                 //此循环的作用是输出20个数
      {if(i%5==0) cout<<endl;         //控制换行，每行输出5个数据 
         cout<<setw(8)<<f[i];         //每个数据输出时占8列宽度 
      }
    cout<<endl;                       //最后执行一次换行 
    return 0;
}
