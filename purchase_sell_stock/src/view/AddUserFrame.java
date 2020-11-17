package view;

import java.awt.EventQueue;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JInternalFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.Dimension;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.JFormattedTextField;
import javax.swing.JFrame;
import javax.swing.JRadioButton;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.SwingConstants;

public class AddUserFrame extends JFrame {
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JTextField textField_3;
	private int WindowWidth;
	private int WindowHeight;
	private int ScreenSizeWidth;
	private int ScreenSizeHeight;

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
	public AddUserFrame() {
		setTitle("×¢²á");
		setBounds(100, 100, 450, 300);
		Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
		ScreenSizeWidth = (int) dimension.getWidth();
		ScreenSizeHeight = (int) dimension.getHeight();
		WindowWidth = this.getWidth();
		WindowHeight = this.getHeight();
		setLocation(ScreenSizeWidth / 2 - WindowWidth / 2, ScreenSizeHeight / 2 - WindowHeight / 2);
		getContentPane().setLayout(null);
		
		JLabel label = new JLabel("ÐÕÃû£º");
		label.setBounds(205, 50, 55, 25);
		label.setHorizontalAlignment(JLabel.RIGHT);
		getContentPane().add(label);
		
		JLabel lblId = new JLabel("ID£º");
		lblId.setBounds(10, 50, 55, 25);
		lblId.setHorizontalAlignment(JLabel.RIGHT);
		getContentPane().add(lblId);
		
		JLabel label_1 = new JLabel("ÃÜÂë£º");
		label_1.setBounds(10, 100, 55, 25);
		label_1.setHorizontalAlignment(JLabel.RIGHT);
		getContentPane().add(label_1);
		
		JLabel lblEmail = new JLabel("EMAIL£º");
		lblEmail.setBounds(205, 100, 55, 25);
		lblEmail.setHorizontalAlignment(JLabel.RIGHT);
		getContentPane().add(lblEmail);
		
		JButton button = new JButton("×¢²á");
		button.setBounds(165, 186, 105, 35);
		getContentPane().add(button);
		
		button.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				dispose();
				LoginFrame loginframe = new LoginFrame();
				loginframe.setVisible(true);
			}
		});
		
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
	}
}
