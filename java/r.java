package r;
import java.util.Scanner;

public class r {
public static  int a[];//被访问的下一个磁道号
public static int b[]=new int [10];//移动距离。
public static int c[]=new int [10];//访问顺序。
public static int start1;//当前磁头所在的磁道号
public static int e;//异常磁道号的下标
public static int sum;//总长度
public static double res;//平均寻道长度
public static boolean res_flag=true ;
public static int maxspace1;//最大的磁道号；
static Scanner inp=new Scanner(System.in);
public static boolean input(){
	//public static int[] input() {
	if(maxspace1<start1) return false;//磁头当前所在位置的磁道号大于最大磁道号，并且防止执行该函数。
	for(int i=0;i<a.length;i++) {
		a[i]=inp.nextInt();
		if(a[i]>maxspace1) {e=i;return false;}//输入被访问的下一磁道号大于最大磁道号并且保留该磁道号的下标，然后退出该函数。
		}
	return true;}
public static boolean output() {
	if(maxspace1<start1||a[e]>maxspace1) return false;//磁头当前所在位置的磁道号大于最大磁道号，或者，输入被访问的下一磁道号大于最大磁道号， 退出。
	System.out.println("每次移动距离：");
	for(int i=0;i<b.length;i++) {
		System.out.print(b[i]+", ");
	}
	System.out.println("");
	System.out.println("访问顺序：");
	for(int i=0;i<c.length;i++) {
		System.out.print(c[i]+", ");
	}
return true;	
}
public static boolean exect(){
	if(maxspace1<start1||a[e]>maxspace1) { if(res==0) {res_flag=false;}return false; }//输入被访问的下一磁道号大于最大磁道号 防止调用输出函数
	for(int i=0;i<a.length;i++) {
		b[i]=Math.abs(start1-a[i]);
		c[i]=a[i];
		start1=a[i];}
	for(int i = 0;i<b.length;i++) {
		sum+=b[i];}
	 res=sum/b.length; 	
	return true;}	
	public static void main(String[] args) {
		while(true) {
			
		System.out.println("模拟磁盘管理 先来先服务算法（FCFS）");
		System.out.println("请输入最大的磁道号：");
		maxspace1=inp.nextInt();
		System.out.println("请输入磁头当前的磁道号且小于最大的磁道号"+maxspace1+":");
		start1=inp.nextInt();
		if(maxspace1<start1) {System.out.println("磁头当前所在位置的磁道号大于最大磁道号 所以退出了");continue;}
        System.out.println("请输入"+a.length+"个磁道顺序");
  input();
  exect();
  output();
  if(res_flag) {System.out.print("平均寻道长度：");//如果平均寻道长度不等于零时才输出。
  System.out.println(res);}
  else System.out.println("磁头当前所在位置的磁道号小于最大磁道号满足 ，但是输入被访问的下一磁道号大于最大磁道号，所以退出了");
 }}}
