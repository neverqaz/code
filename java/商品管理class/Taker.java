package product;

import java.util.*;

public class Taker {
	List<Mementro>list=new ArrayList<Mementro>();
	public void add(Mementro m){
		list.add(m);
	}
	public Mementro get(int i){
		return list.get(i);
		
		
	}
public void print(){
	for(Mementro m:list){
		m.print();
		
		
	}
}
}
