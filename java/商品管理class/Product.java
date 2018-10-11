package product;

import java.util.Date;

public class Product extends ProductSubject{
	private int id;
	private double price;
	private String name;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public double getPrice() {
		return price;
	}
	public Mementro setPrice(double price) {
		Mementro m=new Mementro(id,this.price,new Date());
		String infor="��Ʒ"+name +"�۸������"+this.price+"��Ϊ"+price+"--"+new Date();
		this.price = price;
		this.notifyClients(infor);
		
		return m;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void print(){
		System.out.println(id+" :"+name+" :"+price);
	}
	public Product(int id, double price, String name) {
		super();
		this.id = id;
		this.price = price;
		this.name = name;
	}

}
