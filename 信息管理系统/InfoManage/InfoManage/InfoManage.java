package InfoManage;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

//程序入口
public class InfoManage {
	public static void main(String[] args){
		new LoginDemo("学生信息管理系统登录");
	}
}

//登录界面
@SuppressWarnings("serial")
class LoginDemo extends JFrame{
	private int WindowWidth;
	private int WindowHeight;
	private int ScreenSizeWidth;
	private int ScreenSizeHeight;
	boolean flag = true;
	
	public LoginDemo(String title) {
		super(title);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//设置可关闭
		this.setLayout(null);//设置默认布局格式为空，方便后面定义布局
		this.setResizable(false);//设置不能改变大小
		this.setSize(400,400);//设置大小
		init();
		this.setVisible(true);//设置可视
	}

	private void init() {
		ImageIcon im = new ImageIcon(".\\index.png");
		JLabel imm = new JLabel(im);
		Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();//获取当前屏幕大小
		ScreenSizeWidth = (int) dimension.getWidth();
		ScreenSizeHeight = (int) dimension.getHeight();
		WindowWidth = this.getWidth();
		WindowHeight = this.getHeight();
		this.setLocation(ScreenSizeWidth / 2 - WindowWidth / 2,
		                 ScreenSizeHeight / 2 - WindowHeight / 2);//使窗口的位置为屏幕正中央
		JLabel username_label = new JLabel("学号");
		JLabel password_label = new JLabel("密码");
		final JTextField idinput_field = new JTextField();
		final JPasswordField password_field = new JPasswordField();
		JButton login_button = new JButton("登录");
		imm.setBounds(60, 40, 280, 60);
		username_label.setBounds(100, 130, 100, 40);
		password_label.setBounds(100, 180, 100, 40);
		idinput_field.setBounds(150, 130, 130, 40);
		password_field.setBounds(150, 180, 130, 40);
		login_button.setBounds(100, 250, 182, 40);
		this.add(imm);
		this.add(username_label);
		this.add(password_label);
		this.add(idinput_field);
		this.add(password_field);
		this.add(login_button);
		
		//登录按钮事件监听器
		login_button.addActionListener(new ActionListener() {
			@SuppressWarnings("deprecation")
			public void actionPerformed(ActionEvent event) {
				String stuid = "";
				String pw = "";
				try {
					Connection con = DataBase.getCon();
					stuid = idinput_field.getText();//获取输入的ID
					pw = DataBase.getInfo(con, stuid, "password");//获取该ID的密码
				}catch(ClassNotFoundException e) {
					e.printStackTrace();
				} catch (SQLException e) {
					e.printStackTrace();
				}
				try {
					if(pw.equals(password_field.getText())) {
						JOptionPane.showMessageDialog(null, "登录成功", "Login", JOptionPane.INFORMATION_MESSAGE);
						new HomePage("学生信息管理系统", stuid);
						dispose();//关闭登录demo
					}
					else {
						JOptionPane.showMessageDialog(null, "登录失败，密码错误！", "Login", JOptionPane.INFORMATION_MESSAGE);
						idinput_field.setText("");//清空输入
						password_field.setText("");
					}
				}catch(NullPointerException e) {
					JOptionPane.showMessageDialog(null, "登录失败，无此学生记录！", "Login", JOptionPane.INFORMATION_MESSAGE);
					idinput_field.setText("");
					password_field.setText("");
				}
			}
		});
	}
}