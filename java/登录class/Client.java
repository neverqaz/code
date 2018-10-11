package LoginLayer;

import java.util.Collection;

import productsale.Product;

public interface Client {
public boolean register(User us);
public int login(User us);
public Collection<Object> getProduct();

}
