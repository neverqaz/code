//package LoginLayer;
//import java.awt.BorderLayout;
//import java.awt.GridLayout;
//import java.awt.event.ActionEvent;
//import java.awt.event.ActionListener;
//import java.io.File;
//import java.io.FileNotFoundException;
//import java.sql.Connection;
//import java.sql.ResultSet;
//import java.sql.SQLException;
//import java.sql.Statement;
//import java.util.Scanner;
//
//import javax.swing.JButton;
//import javax.swing.JFrame;
//import javax.swing.JLabel;
//import javax.swing.JPanel;
//import javax.swing.JPasswordField;
//import javax.swing.JTextField;
//
//
//class OriginalCode extends JFrame{
//	Client c=new ClientImpl();
//	OriginalCode(){
//		super("wha");
//		JPanel C=new JPanel();
//		JPanel C1=new JPanel();
//		C.setLayout(new GridLayout(2,2));
//		JLabel jl1=new JLabel("�˺�");
//		final JTextField jt1=new JTextField();
//		C.add(jl1);
//		C.add(jt1);
//		JLabel jl2=new JLabel("����");
//		final JPasswordField jt2=new JPasswordField(15);
//		C.add(jl2);
//		C.add(jt2);
//		add(C,BorderLayout.CENTER);
//		JButton jl=new JButton("��¼");
//		JButton jl3=new JButton("ȡ��");
//		C1.add(jl);
//		C1.add(jl3);
//		setLocationRelativeTo(null);
//		add(C1,BorderLayout.SOUTH);
//		setVisible(true);
//		setSize(300, 200);
//		jl.addActionListener(new ActionListener(){
//			public void actionPerformed(ActionEvent arg0) {
//				String acc=jt1.getText();
//				String pass=jt2.getText();
//			//		User user=new User(acc, pass);
//					if(c.login(user)){
//					//	dispose();	
//						System.out.println("��¼�ɹ�");
//					}
//					else{
//						jt1.setText("�û��������벻��ȷ��");
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
//								jt1.setText("�û����Ѵ�����������д");
//							}
//							else{
//								jt1.setText("ע��ɹ������¼");
//							}
//               }});
//	}
//	public static void main(String[] args) {
//		OriginalCode j=new OriginalCode();
//			j.setVisible(true);
//			j.setSize(400, 300);
//			j.setLocationRelativeTo(null);
//	    } 
//
//}
//
