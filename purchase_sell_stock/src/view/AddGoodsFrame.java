package view;

import java.awt.EventQueue;

import javax.swing.JInternalFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JFormattedTextField;
import javax.swing.JRadioButton;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.SwingConstants;

public class AddGoodsFrame extends JInternalFrame {
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JTextField textField_3;
	private JTextField textField_4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					AddUserFrame frame = new AddUserFrame();
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
	public AddGoodsFrame() {
		setTitle("新建商品");
		setClosable(true);
		setIconifiable(true);
		setBounds(100, 100, 450, 300);
		getContentPane().setLayout(null);
		
		JLabel label = new JLabel("商品名：");
		label.setBounds(205, 50, 55, 25);
		label.setHorizontalAlignment(JLabel.RIGHT);
		getContentPane().add(label);
		
		JLabel lblId = new JLabel("商品ID：");
		lblId.setBounds(10, 50, 55, 25);
		lblId.setHorizontalAlignment(JLabel.RIGHT);
		getContentPane().add(lblId);
		
		JLabel label_1 = new JLabel("数量：");
		label_1.setBounds(10, 100, 55, 25);
		label_1.setHorizontalAlignment(JLabel.RIGHT);
		getContentPane().add(label_1);
		
		JLabel lblEmail = new JLabel("重量：");
		lblEmail.setBounds(205, 100, 55, 25);
		lblEmail.setHorizontalAlignment(JLabel.RIGHT);
		getContentPane().add(lblEmail);
		
		JButton button = new JButton("保存");
		button.setBounds(170, 204, 105, 35);
		getContentPane().add(button);
		
		textField = new JTextField();
		textField.setBounds(60, 50, 144, 25);
		getContentPane().add(textField);
		textField.setColumns(10);
		
		textField_1 = new JTextField();
		textField_1.setBounds(255, 50, 144, 25);
		getContentPane().add(textField_1);
		textField_1.setColumns(10);
		
		textField_2 = new JTextField();
		textField_2.setBounds(60, 100, 144, 25);
		getContentPane().add(textField_2);
		textField_2.setColumns(10);
		
		textField_3 = new JTextField();
		textField_3.setBounds(255, 100, 144, 25);
		getContentPane().add(textField_3);
		textField_3.setColumns(10);
		
		JLabel label_2 = new JLabel("体积：");
		label_2.setHorizontalAlignment(SwingConstants.RIGHT);
		label_2.setBounds(10, 150, 55, 25);
		getContentPane().add(label_2);
		
		textField_4 = new JTextField();
		textField_4.setColumns(10);
		textField_4.setBounds(60, 152, 144, 25);
		getContentPane().add(textField_4);

	}
}

