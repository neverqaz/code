#include<stdio.h>
#include<mpi.h>
#include<math.h> 
main(int a ,char* b[])
{
	int rank,size;
	int x,y,num,j,count=0,i,m;
	MPI_Init(&a,&b);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	x=1;
	num=size;
	printf("rank=%d: ",rank);
	while(num/2!=0)
	{       count++;
		num=num/2;}
	for(i=0;i<count;i++)
	{
	
		if(rank>=(int)pow(2,num))
		{
			printf("请使用关于2的n次方个进程，输入有误结束\n");
			break;
		}
		  j=(int)pow(2,i+1);
		  m=(int)pow(2,i);
		if(rank%j<m)
               {

	           MPI_Send(&x,1,MPI_INT,rank+m,0,MPI_COMM_WORLD);
               }
	
		else
		{
			   MPI_Recv(&y,1,MPI_INT,rank-m,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			   MPI_Send(&x,1,MPI_INT,rank-m,0,MPI_COMM_WORLD);	
		           x=x+y;
		}
		if(rank%j<m)
		{
			   MPI_Recv(&y,1,MPI_INT,rank+m,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			   x=x+y;
		}	
	}
	printf("x=%d\n",x);
	MPI_Finalize();
} 


