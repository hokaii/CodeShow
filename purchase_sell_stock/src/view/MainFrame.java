package view;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.event.MenuListener;

import org.jb2011.lnf.beautyeye.BeautyEyeLNFHelper;

import javax.swing.JPasswordField;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.beans.PropertyVetoException;
import java.awt.SystemColor;
import java.awt.Color;
import java.awt.Dimension;

import javax.swing.ImageIcon;
import javax.swing.JTabbedPane;
import javax.swing.JLabel;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.UIManager;
import javax.swing.JButton;
import java.awt.CardLayout;
import javax.swing.JLayeredPane;
import javax.swing.JInternalFrame;
import javax.swing.JDesktopPane;

public class MainFrame extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try
	    {
			BeautyEyeLNFHelper.frameBorderStyle = BeautyEyeLNFHelper.FrameBorderStyle.osLookAndFeelDecorated;
	        org.jb2011.lnf.beautyeye.BeautyEyeLNFHelper.launchBeautyEyeLNF();
	        UIManager.put("TabbedPane.tabAreaInsets"
	        	    , new javax.swing.plaf.InsetsUIResource(3,3,2,10));
	    }
	    catch(Exception e)
	    {
	        //TODO exception
	    }
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MainFrame frame = new MainFrame();
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
	public MainFrame() {
		setIconImage(Toolkit.getDefaultToolkit().getImage(MainFrame.class.getResource("/images/base.png")));
		setTitle("���������ϵͳ��ҳ");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 550, 400);
		setExtendedState(JFrame.MAXIMIZED_BOTH);
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu menu = new JMenu("�û�����");
		menu.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menuBar.add(menu);
		
		JMenu menu_1 = new JMenu("��Ʒ����");
		menu_1.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menuBar.add(menu_1);

		JMenu menu_2 = new JMenu("����");
		menu_2.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menuBar.add(menu_2);
		
		JMenuItem menuItem_4 = new JMenuItem("��������");
		menuItem_4.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menu_2.add(menuItem_4);
		
		JMenuItem menuItem_5 = new JMenuItem("����");
		menuItem_5.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menu_2.add(menuItem_5);
		
		JMenu menu_3 = new JMenu("�û�");
		menu_3.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menuBar.add(menu_3);
		
		JMenuItem menuItem_6 = new JMenuItem("ע��");
		menuItem_6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				dispose();
				LoginFrame loginframe = new LoginFrame();
				loginframe.setVisible(true);
			}
		});
		menuItem_6.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		
		menu_3.add(menuItem_6);
		
		//JMenuItem menuItem_7 = new JMenuItem("ע��");
		//menuItem_7.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		//menu_3.add(menuItem_7);
		
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(new BorderLayout(0, 0));
		
		JDesktopPane desktopPane = new JDesktopPane();
		desktopPane.setBackground(Color.WHITE);
		contentPane.add(desktopPane, BorderLayout.CENTER);
		
		JMenuItem menuItem = new JMenuItem("�鿴�û�");
		menuItem.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menu.add(menuItem);
		
		menuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				ManageUserFrame manageuserframe = new ManageUserFrame();
				desktopPane.add(manageuserframe);
				manageuserframe.setVisible(true);
			}
		});
		
		/*JMenuItem menuItem_1 = new JMenuItem("�½��û�");
		menuItem_1.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menu.add(menuItem_1);
		
		menuItem_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AddUserFrame adduserframe = new AddUserFrame();
				desktopPane.add(adduserframe);
				adduserframe.setVisible(true);
			}
		});*/
		
		JMenuItem menuItem_2 = new JMenuItem("�鿴��Ʒ");
		menuItem_2.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menu_1.add(menuItem_2);
		
		menuItem_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				ManageGoodsFrame managegoodsframe = new ManageGoodsFrame();
				desktopPane.add(managegoodsframe);
				managegoodsframe.setVisible(true);
			}
		});
		
		JMenuItem menuItem_3 = new JMenuItem("�½���Ʒ");
		menuItem_3.setIcon(new ImageIcon(MainFrame.class.getResource("/images/base.png")));
		menu_1.add(menuItem_3);
		
		menuItem_3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AddGoodsFrame addgoodsframe = new AddGoodsFrame();
				desktopPane.add(addgoodsframe);
				addgoodsframe.setVisible(true);
			}
		});
		
	}
}