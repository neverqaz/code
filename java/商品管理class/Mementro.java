package product;

import java.util.Date;


public class Mementro {
	private int id;
	private double price;;
	private Date date;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public Date getDate() {
		return date;
	}
	public void setDate(Date date) {
		this.date = date;
	}
	public Mementro(int id, double price, Date date) {
		super();
		this.id = id;
		this.price = price;
		this.date = date;
	}
public void print(){
	System.out.println(id+" ,"+price+" ,"+date);
}

	
	
	
	

}
