package LoginLayer;

public class User {
	int level;
public String name;
public String passward;
public String phone;
public String address;
public User(String name, String passward, String phone, String address,int level) {
	super();
	this.name = name;
	this.passward = passward;
	this.phone = phone;
	this.address = address;
	this.level=level;
}
public User(String name, String passward) {
	super();
	this.name = name;
	this.passward = passward;
}

public int getLevel() {
	return level;
}
public String getPhone() {
	return phone;
}

public String getAddress() {
	return address;
}

public String getname(){
	return name;
}
public String getpassward(){
	return passward;
}
}
