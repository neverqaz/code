package frame1;
import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Label;
import java.awt.TextArea;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class frame1 extends JFrame {
	
	TextArea txa=null;
	JMenuBar jmb=null;
	JMenu jm=null;
	JMenuItem jmi1=null;
	JMenuItem jmi2=null;
	JMenuItem jmi3=null;
	JButton jbt=null;
    Font f=new Font("����",44,34);
    public frame1(){ 
		 jmb=new JMenuBar();
		 
         jm=new JMenu("������");
		jmi1=new JMenuItem("����URL");
	    jmi2=new JMenuItem("����ؼ���");
	    jmi3=new JMenuItem("�洢html��ַ");
	    jmb.add(jm);
	    jm.add(jmi1);
	    jm.add(jmi2);
	    jm.add(jmi3);setJMenuBar(jmb);
	    txa=new TextArea("��ѯ�����ʾ��");
	    txa.setSize(400, 300);
	    txa.setLocation(100, 100);
	    jbt=new JButton("��ѯ");
	    jbt.setLocation(600, 200);
	    jbt.setSize(100, 100);
	    this.setLayout(null);
	    add(txa);
	    add(jbt);
	    setTitle("����");
	    setSize(800,614);
		setLocation(50,20);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
		
	    }
	 public static void main(String[] args) {
			
		new frame1();
					
		}

}
