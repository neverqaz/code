package max;

import java.util.Random;
import java.util.Scanner;

public class max {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		int k=input.nextInt();
		
	double []array=new double [10000000];
	for(int i=0;i<k;i++){
		array[i]=Math.random()*10000;}
	for(int j=1;j<k;j++){
		for(int i=0;i<k-j;i++)if(array[i]>array[i+1]){double h=array[i];
		array[i]=array[i+1];
		array[i+1]=h;}}
	for(int i=0;i<k;i++)
	System.out.print(array[i]+" ");
	
	

	}



}