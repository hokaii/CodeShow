package view;

import java.awt.EventQueue;

import javax.swing.JInternalFrame;
import javax.swing.JTable;
import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.ImageIcon;
import javax.swing.table.DefaultTableModel;
import javax.swing.JScrollPane;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class ManageGoodsFrame extends JInternalFrame {
	private JTextField textField;
	private JTable table;
	private JButton button_1;
	private JButton button_2;
	private JButton button_3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ManageUserFrame frame = new ManageUserFrame();
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
	public ManageGoodsFrame() {
		setClosable(true);
		setIconifiable(true);
		setTitle("商品信息管理");
		setBounds(100, 100, 500, 430);
		getContentPane().setLayout(null);
		
		textField = new JTextField();
		textField.setBounds(50, 22, 273, 30);
		getContentPane().add(textField);
		textField.setColumns(10);
		
		JButton button = new JButton("查询");
		button.setIcon(new ImageIcon(ManageUserFrame.class.getResource("/images/search.png")));
		button.setBounds(333, 19, 95, 35);
		getContentPane().add(button);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(0, 63, 482, 275);
		getContentPane().add(scrollPane);
		
		table = new JTable();
		scrollPane.setViewportView(table);
		table.setModel(new DefaultTableModel(
			new Object[][] {
				{"1", "凡士林", "123", "2", "1"},
				{"2", "水杯", "456", "3", "2"},
			},
			new String[] {
				"商品ID", "商品名", "数量/件", "重量/kg", "体积/L"
			}
		));
		
		button_1 = new JButton("删除");
		button_1.setBounds(50, 350, 95, 30);
		getContentPane().add(button_1);
		
		button_2 = new JButton("修改");
		button_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		button_2.setBounds(201, 350, 95, 30);
		getContentPane().add(button_2);
		
		button_3 = new JButton("保存");
		button_3.setBounds(347, 350, 95, 30);
		getContentPane().add(button_3);

	}
}
