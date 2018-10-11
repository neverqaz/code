package product;

import java.util.*;

public abstract class ProductSubject {
	List<Client>list=new ArrayList<Client>();
	public void attach(Client c){
		list.add(c);
	}
    public  void detach(Client c){
    	list.remove(c);
    }
    public void notifyClients(String infor){
    	for(Client c:list){
    		c.show(infor);
    	}
    }
}
