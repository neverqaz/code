package r;
import java.util.Scanner;

public class r {
public static  int a[];//�����ʵ���һ���ŵ���
public static int b[]=new int [10];//�ƶ����롣
public static int c[]=new int [10];//����˳��
public static int start1;//��ǰ��ͷ���ڵĴŵ���
public static int e;//�쳣�ŵ��ŵ��±�
public static int sum;//�ܳ���
public static double res;//ƽ��Ѱ������
public static boolean res_flag=true ;
public static int maxspace1;//���Ĵŵ��ţ�
static Scanner inp=new Scanner(System.in);
public static boolean input(){
	//public static int[] input() {
	if(maxspace1<start1) return false;//��ͷ��ǰ����λ�õĴŵ��Ŵ������ŵ��ţ����ҷ�ִֹ�иú�����
	for(int i=0;i<a.length;i++) {
		a[i]=inp.nextInt();
		if(a[i]>maxspace1) {e=i;return false;}//���뱻���ʵ���һ�ŵ��Ŵ������ŵ��Ų��ұ����ôŵ��ŵ��±꣬Ȼ���˳��ú�����
		}
	return true;}
public static boolean output() {
	if(maxspace1<start1||a[e]>maxspace1) return false;//��ͷ��ǰ����λ�õĴŵ��Ŵ������ŵ��ţ����ߣ����뱻���ʵ���һ�ŵ��Ŵ������ŵ��ţ� �˳���
	System.out.println("ÿ���ƶ����룺");
	for(int i=0;i<b.length;i++) {
		System.out.print(b[i]+", ");
	}
	System.out.println("");
	System.out.println("����˳��");
	for(int i=0;i<c.length;i++) {
		System.out.print(c[i]+", ");
	}
return true;	
}
public static boolean exect(){
	if(maxspace1<start1||a[e]>maxspace1) { if(res==0) {res_flag=false;}return false; }//���뱻���ʵ���һ�ŵ��Ŵ������ŵ��� ��ֹ�����������
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
			
		System.out.println("ģ����̹��� �����ȷ����㷨��FCFS��");
		System.out.println("���������Ĵŵ��ţ�");
		maxspace1=inp.nextInt();
		System.out.println("�������ͷ��ǰ�Ĵŵ�����С�����Ĵŵ���"+maxspace1+":");
		start1=inp.nextInt();
		if(maxspace1<start1) {System.out.println("��ͷ��ǰ����λ�õĴŵ��Ŵ������ŵ��� �����˳���");continue;}
        System.out.println("������"+a.length+"���ŵ�˳��");
  input();
  exect();
  output();
  if(res_flag) {System.out.print("ƽ��Ѱ�����ȣ�");//���ƽ��Ѱ�����Ȳ�������ʱ�������
  System.out.println(res);}
  else System.out.println("��ͷ��ǰ����λ�õĴŵ���С�����ŵ������� ���������뱻���ʵ���һ�ŵ��Ŵ������ŵ��ţ������˳���");
 }}}
