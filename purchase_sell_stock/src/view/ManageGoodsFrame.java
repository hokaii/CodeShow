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
		setTitle("��Ʒ��Ϣ����");
		setBounds(100, 100, 500, 430);
		getContentPane().setLayout(null);
		
		textField = new JTextField();
		textField.setBounds(50, 22, 273, 30);
		getContentPane().add(textField);
		textField.setColumns(10);
		
		JButton button = new JButton("��ѯ");
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
				{"1", "��ʿ��", "123", "2", "1"},
				{"2", "ˮ��", "456", "3", "2"},
			},
			new String[] {
				"��ƷID", "��Ʒ��", "����/��", "����/kg", "���/L"
			}
		));
		
		button_1 = new JButton("ɾ��");
		button_1.setBounds(50, 350, 95, 30);
		getContentPane().add(button_1);
		
		button_2 = new JButton("�޸�");
		button_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		button_2.setBounds(201, 350, 95, 30);
		getContentPane().add(button_2);
		
		button_3 = new JButton("����");
		button_3.setBounds(347, 350, 95, 30);
		getContentPane().add(button_3);

	}
}
