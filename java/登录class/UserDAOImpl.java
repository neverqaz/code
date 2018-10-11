
package LoginLayer;
import java.sql.*;
import java.util.ArrayList;
//import java.util.list;
import java.util.Collection;
import java.util.List;

import productsale.Product;



public class UserDAOImpl implements UserDAO{
	static Connection conn=null;
	PreparedStatement ps=null;
	ResultSet rs=null;
	
	@Override
	public boolean insert(User user) {
		// TODO Auto-generated method stub
		boolean flag=false;
		int quan;
		String str="select name from test1 where name=?";
		conn=ConnectMysql.ConnectMysql();
		try { 
			ps=conn.prepareStatement(str);
			ps.setString(1,user.name);
			if(user.level==1){
				quan=100;
			}
			else{
				quan=50;
			}
			rs=ps.executeQuery();{
				if(rs.next()){
					flag=true;
				}//insert into test1 values (?,?);
				else{
					PreparedStatement pr=conn.prepareStatement("Insert into client(username,password,phone,address,quan,level)values(?,?,?,?,?,?);");
					pr.setString(1,user.name);
					pr.setString(2, user.passward);
					pr.setString(3, user.phone);
					pr.setString(4, user.address);
					pr.setInt(5, quan);
					pr.setInt(6, user.level);
					pr.executeUpdate();
				}
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}finally{
			ConnectMysql.closeAll(rs, ps, conn);
		}
		return flag;
	}
	@Override
	public void delete(User user) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void update(User user) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public int checkUser(User user) {
		// TODO Auto-generated method stub
		int level=0;
		String sql="select * from client where username=? and password=?";
		System.out.println(user.name+"  "+user.passward);
		try {
			conn=ConnectMysql.ConnectMysql();
			ps= conn.prepareStatement(sql);
			ps.setString(1,user.name);
			ps.setString(2,user.passward);
		    rs=ps.executeQuery();
			if(rs.next()){
				PreparedStatement pr=conn.prepareStatement("select level from client where username=?;");
				pr.setString(1,user.name);
				rs=pr.executeQuery();
				if(rs.next()){
					level=rs.getInt(1);
				}
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally{
			ConnectMysql.closeAll(rs, ps, conn);	
		}
		return level;
	}

	@Override
	public User getUserById(int id) {
		// TODO Auto-generated method stub
		return null;
	}
	@Override
	public boolean changeStoke(int id) {//购买后改变库存
		boolean flag=false;
		String str="select number from product where id=?";
		conn=ConnectMysql.ConnectMysql();
		try { 
			ps=conn.prepareStatement(str);
			ps.setInt(1,id);
			rs=ps.executeQuery();
			{
				if(rs.next()){
					System.out.println(id);
					int stoke=rs.getInt(1);
					System.out.println(stoke);
					if(stoke>=1)
					{
					stoke=stoke-1;
					PreparedStatement pr=conn.prepareStatement("Update product set number=? where id=?;");
					pr.setInt(1,stoke);
					pr.setInt(2,id);
					pr.executeUpdate();
					flag=true;
					}
					else{
						flag=false;
					}
				}
				else{flag=false;}
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
		return flag;
	}
	public boolean addStoke(int id) {//退货审批后增加库存
		boolean flag=false;
		String str="select number from product where id=?";
		conn=ConnectMysql.ConnectMysql();
		try { 
			ps=conn.prepareStatement(str);
			ps.setInt(1,id);
			
			rs=ps.executeQuery();
			{
				if(rs.next()){
					System.out.println(id);
					int stoke=rs.getInt(1);
					stoke=stoke+1;
					PreparedStatement pr=conn.prepareStatement("Update product set number=? where id=?;");
					pr.setInt(1,stoke);
					pr.setInt(2,id);
					pr.executeUpdate();
					flag=true;
				}
				else{flag=false;}
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
		return flag;
	}
	@Override
	public Collection<Object> showProduct() {
		// TODO Auto-generated method stub
		conn=ConnectMysql.ConnectMysql();
		List<Object> list=new ArrayList<Object>();
		try {
			ps=conn.prepareStatement("Select * from product ;");
			rs=ps.executeQuery();
			while(rs.next()){
				int id=rs.getInt("id");
				String name=rs.getString("name");
				String kind=rs.getString("kind");
				int price=rs.getInt("price");
				int number=rs.getInt("number");
				String stoke;
				if(number>=1){
					stoke="有货";
				}
				else {
					stoke="无货";
				}
				list.add(new Product(id, name, kind, price, stoke));
				}} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}list.add(1);
		return list;
	}
}
