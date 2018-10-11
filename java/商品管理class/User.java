package product;

public class User {
	public void setprice(Product p){
		
	Taker t=new Taker();
	Mementro m=p.setPrice(15);
	t.add(m);
	m=p.setPrice(17);
	t.add(m);
	t.print(); 
		
	}

}
