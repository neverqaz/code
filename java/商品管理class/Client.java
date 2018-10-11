package product;

public class Client {
	private String name;
	private int id;
	public void print(){
		
		System.out.println(name+" : "+id);
	}
public void show(String infor){
	
	System.out.println(name+"ÓÃ»§ÄúºÃ£º "+infor);
}
public Client(String name, int id) {
	super();
	this.name = name;
	this.id = id;
}

}
