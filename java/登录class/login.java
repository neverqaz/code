//package LoginLayer;
//import java.awt.*;
////import java.io 
//import java.awt.event.ActionEvent;
//import java.awt.event.ActionListener;
////.File;
//import java.io 
//
//.FileNotFoundException;
//import java.sql.*;
//import java.util.Scanner;
//import java.util.Set;
//import javax.swing.*;
//public class login extends JFrame{
//	public static void main(String[] args) {
//		new login().showLogin();
//	}
//	Client c=new ClientImpl();
//	JLabel jl2;
//	JPasswordField jt2;
//	JTextField jt1;
//	JLabel jl1;
//	JButton jl;
//	JButton jl3;
//	public login(){
//		super();
//		this.showLogin();
//	}
//	//Client c=new ClientImpl();
//	public void showLogin(){
//		//super("wha");			
//	this.setLayout(null);
//		 jl1=new JLabel("账号");
//		 jl1.setSize(50, 25);
//		 jl1.setLocation(50, 50);
//		jt1=new JTextField();
//		jt1.setLocation(125, 50);
//		jt1.setSize(100,25);			
//	     jl2=new JLabel("密码");
//	     jl2.setSize(50, 25);
//		 jl2.setLocation(50, 100);
//		 jt2=new JPasswordField();
//		 jt2.setSize(100,25);
//		jt2.setLocation(125, 100);	 
//	   jl=new JButton("登录");
//		jl3=new JButton("取消");
//		jl.setSize(60, 40);
//		 jl.setLocation(65, 150);
//		 jl3.setSize(60, 40);
//		 jl3.setLocation(175, 150);
//		 this.add(jl1);
//		 this.add(jt1);
//		 this.add(jl2);
//		 this.add(jt2);
//		 this.add(jl);
//		 this.add(jl3);
//		this.setLocationRelativeTo(null);
//		this.setVisible(true);
//		this.setSize(300, 300);
//		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//		jl.addActionListener(new ActionListener(){
//			public void actionPerformed(ActionEvent arg0) {
//				String acc=jt1.getText();
//				String pass=jt2.getText();
//					User user=new User(acc, pass);
//					if(c.login(user)){
//					//	dispose();	
//						System.out.println("登录成功");
//					}
//					else{
//						jt1.setText("用户名或密码不正确！");
//					}
//			}});	
//		jl3.addActionListener(new ActionListener(){
//					public void actionPerformed(ActionEvent arg0) {
//					//dispose();
//						String acc=jt1.getText();
//						String pass=jt2.getText();
//							User user=new User(acc, pass);
//							if(c.register(user)){
//							//	 dispose();	
//								jt1.setText("用户名已存在请重新填写");
//							}
//							else{
//								jt1.setText("注册成功，请登录");
//							}
//               }});
//	}
//	
//	    } 
