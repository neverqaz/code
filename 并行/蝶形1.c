	#include<stdio.h>
	#include<mpi.h>

	main(int argv,char* argc[]){
		int size,rank;
		int i,j,start,middle,s,t;
		MPI_Init(&argv,&argc);
		MPI_Comm_size(MPI_COMM_WORLD,&size);	
		MPI_Comm_rank(MPI_COMM_WORLD,&rank);
		start=0;
		middle=(start+size)/2;
		s=1;
	printf("½ø³ÌºÅ£º%d",rank);
		for(i=1;i<=middle;i=pow(2,i)){
			for(j=0;j<size;j=j+pow(2,i))
				{
				if(rank<i+j&&rank>=j){
				MPI_Send(&s,1,MPI_INT,rank+i,0,MPI_COMM_WORLD);
				MPI_Recv(&t,1,MPI_INT,rank+i,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE); 
				s=s+t;}
				if(rank>=i+j&&rank<j+pow(2,i)){
				MPI_Send(&s,1,MPI_INT,rank-i,0,MPI_COMM_WORLD);
				MPI_Recv(&t,1,MPI_INT,rank-i,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE); 
				s=s+t;}
				
	}
	}
	printf("s=%d",s);

		MPI_Finalize();
	}