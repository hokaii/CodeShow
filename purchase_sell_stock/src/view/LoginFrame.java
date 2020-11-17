package view;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JInternalFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import org.jb2011.lnf.beautyeye.BeautyEyeLNFHelper;

import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.Panel;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Color;
import java.awt.Dimension;

public class LoginFrame extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JPasswordField passwordField;
	private int WindowWidth;
	private int WindowHeight;
	private int ScreenSizeWidth;
	private int ScreenSizeHeight;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		
		try
	    {
			BeautyEyeLNFHelper.frameBorderStyle = BeautyEyeLNFHelper.FrameBorderStyle.osLookAndFeelDecorated;
	        org.jb2011.lnf.beautyeye.BeautyEyeLNFHelper.launchBeautyEyeLNF();
	    }
	    catch(Exception e)
	    {
	        //TODO exception
	    }
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					LoginFrame frame = new LoginFrame();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public LoginFrame() {
		setResizable(false);
		setTitle("µÇÂ¼");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		setBounds(100, 100, 445, 351);
		Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
		ScreenSizeWidth = (int) dimension.getWidth();
		ScreenSizeHeight = (int) dimension.getHeight();
		WindowWidth = this.getWidth();
		WindowHeight = this.getHeight();
		setLocation(ScreenSizeWidth / 2 - WindowWidth / 2, ScreenSizeHeight / 2 - WindowHeight / 2);
		
		contentPane = new JPanel();
		contentPane.setBackground(Color.WHITE);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		textField = new JTextField();
		textField.setText("ÕÅÈý");
		textField.setBounds(164, 136, 136, 28);
		contentPane.add(textField);
		textField.setColumns(10);
		
		passwordField = new JPasswordField();
		passwordField.setToolTipText("");
		passwordField.setBounds(164, 174, 136, 28);
		contentPane.add(passwordField);
		
		JLabel lblNewLabel = new JLabel("ÓÃ»§Ãû£º");
		lblNewLabel.setBounds(116, 136, 66, 28);
		contentPane.add(lblNewLabel);
		
		
		JLabel label = new JLabel("ÃÜÂë£º");
		label.setBounds(116, 173, 54, 28);
		contentPane.add(label);
		
		//ImageIcon im = new ImageIcon("/images/login_text.PNG");
		//JLabel label_1 = new JLabel(new ImageIcon(LoginFrame.class.getResource("/images/login_text.PNG")));
		//label_1.setBounds(83,  48, 255, 45);
		//contentPane.add(label_1);
		
		JButton button = new JButton("µÇÂ¼");
		button.setBounds(206, 232, 93, 34);
		contentPane.add(button);
		
		button.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				dispose();
				MainFrame mainframe = new MainFrame();
				mainframe.setVisible(true);
			}
		});
		
		JLabel label_1 = new JLabel("");
		label_1.setIcon(new ImageIcon(LoginFrame.class.getResource("/images/login_text.png")));
		label_1.setBounds(74, 26, 280, 100);
		contentPane.add(label_1);
		
		JButton button_1 = new JButton("×¢²á");
		button_1.setBounds(115, 232, 66, 34);
		contentPane.add(button_1);
		
		button_1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				dispose();
				AddUserFrame adduserframe = new AddUserFrame();
				adduserframe.setVisible(true);
			}
		});
	}
}
