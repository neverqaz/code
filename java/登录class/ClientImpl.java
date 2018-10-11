package LoginLayer;

import java.util.Collection;

import productsale.Product;

public class ClientImpl implements Client{
		UserDAO ud=new UserDAOImpl();
	public ClientImpl() {
		// TODO Auto-generated constructor stub
		
	}

	@Override
	public boolean register(User us) {
		// TODO Auto-generated method stub
		return ud.insert(us);
	}

	@Override
	public int login(User us) {
		// TODO Auto-generated method stub
		return ud.checkUser(us);
	}

	@Override
	public Collection<Object> getProduct() {
		// TODO Auto-generated method stub
		return ud.showProduct();
	}

}
