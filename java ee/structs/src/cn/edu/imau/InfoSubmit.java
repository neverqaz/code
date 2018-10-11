package cn.edu.imau;

import java.sql.Date;

import com.opensymphony.xwork2.ActionSupport;

public class InfoSubmit extends ActionSupport {
	String name;
	int age;
	Date brithday;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public Date getBrithday() {
		return brithday;
	}
	public void setBrithday(Date brithday) {
		this.brithday = brithday;
	}
	@Override
	public String execute() throws Exception {
		// TODO Auto-generated method stub
		return "s";
	}
	

}
