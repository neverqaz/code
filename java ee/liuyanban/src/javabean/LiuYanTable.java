package javabean;

public class LiuYanTable {
    String title;
    String liuyan;
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getLiuyan() {
		return liuyan;
	}
	public void setLiuyan(String liuyan) {
		this.liuyan = liuyan;
	}
	public LiuYanTable(String title, String liuyan) {
		super();
		this.title = title;
		this.liuyan = liuyan;
	}
    
}
