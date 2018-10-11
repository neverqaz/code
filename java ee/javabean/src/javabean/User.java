package javabean;

import java.util.HashMap;

public class User {
	private String username;
	private String password;
	private String email;
	private String tel;
	private String address;
	private String gender;
    //错误信息保存（变化的数据 ）
	private HashMap error;
	
	public User() {
		
		username="";
		password="";
		email="";
		error=new HashMap();
		
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getError(String key) {
		String value=error.get(key)==null?"":error.get(key).toString();//判断是否是空串
		return value;
	}
	public void setError(String key ,String value) {
		 error.put(key, value);
	}

	public String getTel() {
		return tel;
	}
	public void setTel(String tel) {
		this.tel = tel;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	//校验用户信息
	public boolean validate() {
		
		boolean flag=true;
		if(username.trim().equals("")) {
			setError("username","用户名不能为空");
			flag=false;
			
		}
		if(password.length()<6||password.length()>12) {
			setError("password","密码必须是6-12位");
			flag=false;
			
		}
		if(email.indexOf("@")==-1||email.indexOf(".")==-1) {
			setError("email","电子邮件地址不正确");
			flag=false;
			
		}
		
		
		return flag;
	}

}
