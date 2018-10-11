#include<iostream.h>
#include<stdlib.h>
#include<string.h>
typedef char sign[20];
template <class Q,class Q1,class Q2>class list;
template <class Q,class Q1,class Q2> class listnode{
	friend class list<Q,Q1,Q2>;
	private:
		sign name;
		Q number;
		Q1 math;
		Q2 english;
		listnode<Q,Q1,Q2> *next;};
template <class Q,class Q1,class Q2>class list{
private:
	listnode<Q,Q1,Q2> *L;
public:
	list(){L=new listnode<Q,Q1,Q2>;L->next=NULL;}
	void print();
	int setup(int x);
	int inset(int y,sign name1,Q number1,Q1 math,Q2 english1);
};
template <class Q,class Q1,class Q2>int list<Q,Q1,Q2>::setup(int x){
	listnode<Q,Q1,Q2> *h;
	int i;
	for(i=x;i>0;--i){
	h=new listnode<Q,Q1,Q2>;
	cin>>h->name>>h->number>>h->math>>h->english;
	h->next=L->next;
	L->next=h;	}

return 1;
}
template <class Q,class Q1,class Q2>void list<Q,Q1,Q2>::print(){
	listnode<Q,Q1,Q2> *g;
		g=L->next;
	while(g!=NULL){cout<<g->name<<" "<<g->number<<" "<<g->math<<" "<<g->english<<endl;
	g=g->next;}cout<<endl;
}
template<class Q,class Q1,class Q2>int list<Q,Q1,Q2>::inset(int y,sign name1,Q number1,Q1 math1,Q2 english1){
listnode<Q,Q1,Q2> *t,*m;
   t=L->next;
   int j=1;
   while(t!=NULL&&j<y-1){
   t=t->next;
   j++;
   }
if(t==NULL||j>y-1)return 0;
m=new listnode<Q,Q1,Q2>;

if(t==NULL)exit(0);
strcpy(m->name,name1);
m->number=number1;
m->math=math1;
m->english=english1;
m->next=t->next;
t->next=m;
return 1;
}
int main(){
list<int,double,double> vb;
sign name;
int number,d,m;
double math,english;
cin>>d;
vb.setup(d);
vb.print();
cin>>m>>name>>number>>math>>english;
vb.inset(m,name,number,math,english);
vb.print();



return 0;}
