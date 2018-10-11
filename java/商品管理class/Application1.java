package product;

public class Application1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		User u=new User();
		Client c=new Client("zhangsan",1);
		Product p=new Product(1,20,"Ë®±­");
		p.attach(c);
		u.setprice(p);

	}

}
