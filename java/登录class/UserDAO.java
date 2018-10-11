package LoginLayer;

import java.awt.List;
import java.util.Collection;

import productsale.Product;

public interface UserDAO {
	public boolean addStoke(int id);
	public boolean changeStoke(int id);
	public boolean insert(User user);
	public void delete(User user);
	public void update(User user);
	//public List<User> getAllUser(); 
	public int checkUser(User user);
	public User getUserById(int id);
	public Collection<Object> showProduct();
}
