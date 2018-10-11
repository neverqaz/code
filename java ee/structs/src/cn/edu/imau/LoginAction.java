package cn.edu.imau;

import com.opensymphony.xwork2.ActionSupport;

public class LoginAction extends ActionSupport {
	String username;
	
	String password;

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

	@Override
	public String execute() throws Exception {
		// TODO Auto-generated method stub
		if("zhangsan".equals(username)&&"123".equals(password))
		return SUCCESS;
		else return "failure";
	}

	@Override
	public void validate() {
		// TODO Auto-generated method stub
		if(null==username||"".equals(username.trim()))
        this.addFieldError(username, "用户名不能为空");
		if(null==password||"".equals(password.trim()))
	        this.addFieldError(password, "用户名不能为空");
		super.validate();
	}
	
	
	

}
