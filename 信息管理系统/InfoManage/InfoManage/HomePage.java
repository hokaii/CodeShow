package InfoManage;

import java.sql.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.table.DefaultTableModel;
import java.util.Date;
import java.util.Vector;

//管理系统主页
public class HomePage extends JFrame implements ActionListener, ListSelectionListener {
	private static final long serialVersionUID = 1L;
	private int WindowWidth;
	private int WindowHeight;
	private int ScreenSizeWidth;
	private int ScreenSizeHeight;
	private String stuid1;
	String studentname = null;
	DefaultTableModel defaultModel = null;
	JTable jTable = null;
	JPanel stupanel = new JPanel();
	JPanel privatestupanel = new JPanel();
	JPanel homepanel = new JPanel();

	public HomePage(String title, String stuid1) {
		super(title);
		this.stuid1 = stuid1;
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLayout(null);
		this.setResizable(false);
		this.setSize(1000, 600);
		init();
		this.setVisible(true);
	}

	@SuppressWarnings({ "rawtypes", "unchecked" })
	public void init() {
		String stuname = "";
		// 分别声明管理员和学生登录的数据库查询结果
		ResultSet select = null;
		ResultSet privateselect = null;
		try {
			Connection con = DataBase.getCon();
			stuname = DataBase.getInfo(con, stuid1, "name");
			studentname = stuname;
			select = DataBase.getSelect(con, "select * from studentinfo");
			privateselect = DataBase.getSelect(con, "select * from studentinfo where ID = '" + stuid1 + "'");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		// 登录时间信息
		Date date = new Date();
		String logintime = date.toString();
		// 使界面处于正中间
		Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
		ScreenSizeWidth = (int) dimension.getWidth();
		ScreenSizeHeight = (int) dimension.getHeight();
		WindowWidth = this.getWidth();
		WindowHeight = this.getHeight();
		this.setLocation(ScreenSizeWidth / 2 - WindowWidth / 2, ScreenSizeHeight / 2 - WindowHeight / 2);
		// 图片显示
		ImageIcon im = new ImageIcon(".\\index1.png");
		JLabel imJlabel = new JLabel(im);
		// 时间显示
		JLabel timeJlabel = new JLabel("登录时间：" + logintime);
		// 文字显示
		JLabel wordJlabel = new JLabel("你好，" + stuname);
		// 按钮显示
		JButton logout = new JButton("注销");
		JButton printreport = new JButton("报表打印");
		// 增加按钮时间监听器
		logout.addActionListener(this);
		printreport.addActionListener(this);
		// 列表框显示
		JList stuinfoList = new JList();
		stuinfoList.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);// 允许可简短的多选
		stuinfoList.setListData(new String[] { "主页", "学生信息" });
		// 增加事件监听器
		stuinfoList.addListSelectionListener(this);
		// 主页显示
		JLabel welcomelabel = new JLabel("欢迎登录学生信息管理系统");
		welcomelabel.setFont(new Font("宋体", Font.BOLD, 30));
		// 设置位置及大小
		wordJlabel.setBounds(230, 0, 100, 30);
		imJlabel.setBounds(0, 0, 220, 50);
		printreport.setBounds(300, 27, 90, 20);
		logout.setBounds(222, 27, 90, 20);
		timeJlabel.setBounds(730, 0, 260, 30);
		stuinfoList.setBounds(0, 50, 57, 510);
		homepanel.setBounds(60, 50, 925, 500);
		homepanel.add(welcomelabel);
		this.add(imJlabel);
		this.add(wordJlabel);
		this.add(logout);
		this.add(printreport);
		this.add(timeJlabel);
		this.add(stuinfoList);
		this.add(homepanel);
		// 学生信息显示区域
		privatestupanel.setLayout(null);
		Vector<String> privatecol = getCol(privateselect);
		Vector privatedata = getData(privateselect);
		// 管理员信息显示区域
		stupanel.setLayout(null);
		Vector<String> col = getCol(select);
		Vector data = getData(select);
		// 判断ID确定身份
		if (stuid1.equals("0"))
			defaultModel = new DefaultTableModel(data, col);
		else
			defaultModel = new DefaultTableModel(privatedata, privatecol);
		// 表格显示
		jTable = new JTable(defaultModel);
		JScrollPane jScrollPane = new JScrollPane();
		jScrollPane.getViewport().add(jTable);
		JButton newmessage = new JButton("新建");
		JButton delmessage = new JButton("删除");
		JButton savemessage = new JButton("保存");
		stupanel.add(newmessage);
		stupanel.add(delmessage);
		stupanel.add(savemessage);
		// 如果是学生则隐藏所有编辑按钮
		if (!stuid1.equals("0")) {
			newmessage.setVisible(false);
			delmessage.setVisible(false);
			savemessage.setVisible(false);
			jTable.setEnabled(false);
		}
		stupanel.add(jScrollPane);
		// 事件监听器
		newmessage.addActionListener(this);
		delmessage.addActionListener(this);
		savemessage.addActionListener(this);
		stupanel.setVisible(false);
		stupanel.setBounds(60, 50, 925, 500);
		newmessage.setBounds(0, 0, 60, 20);
		delmessage.setBounds(60, 0, 60, 20);
		savemessage.setBounds(120, 0, 60, 20);
		jScrollPane.setBounds(0, 20, 900, 450);
		this.add(stupanel);
	}

	// 获取表头
	public Vector<String> getCol(ResultSet rs) {
		Vector<String> col = new Vector<String>();
		try {
			// 获取 ResultSet 对应的 ResultSetMetaData 对象
			ResultSetMetaData metaData = rs.getMetaData();
			int columnCount = metaData.getColumnCount();
			for (int i = 1; i <= columnCount; i++) {
				col.add(metaData.getColumnName(i));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return col;
	}

	// 获取信息,返回一个矢量数组
	@SuppressWarnings({ "unchecked", "rawtypes" })
	public Vector getData(ResultSet rs) {
		Vector data = new Vector();
		try {
			ResultSetMetaData metaData = rs.getMetaData();
			int columnCount = metaData.getColumnCount();
			while (rs.next()) {
				Vector<String> v = new Vector<String>();
				for (int i = 1; i <= columnCount; i++) {
					v.addElement(rs.getString(i));
				}
				data.addElement(v);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return data;
	}

	// 按钮事件
	@SuppressWarnings({ "rawtypes" })
	public void actionPerformed(ActionEvent e) {
		if (e.getActionCommand().equals("新建"))
			defaultModel.addRow(new Vector());

		if (e.getActionCommand().equals("删除")) {
			// 获取指定行数
			int rownumber = jTable.getSelectedRow();
			if (rownumber == 0) {
				JOptionPane.showMessageDialog(null, "无法删除管理员数据！", "警告", JOptionPane.INFORMATION_MESSAGE);
			} else
				defaultModel.removeRow(rownumber);
		}

		if (e.getActionCommand().equals("保存")) {
			int row = jTable.getRowCount();
			int column = jTable.getColumnCount();
			int flag = 0;// flag为0正常保存
			try {
				// 检查是否有单元格为空
				for (int i = 0; i < row; i++) {
					for (int j = 0; j < column; j++) {
						jTable.getValueAt(i, j).toString();
					}
				}
				// 检查是否有重复的ID
				for (int i = 0; i < row; i++) {
					for (int j = i + 1; j < row; j++) {
						if (jTable.getValueAt(i, 0).toString().equals(jTable.getValueAt(j, 0).toString())) {
							flag = 2;
							break;
						}
					}
				}
			} catch (NullPointerException event) {
				flag = 1;
			}
			if (flag == 0) {
				PreparedStatement preparedStatement = null;
				String[][] value = new String[row][column];
				// 获取当前表中的数据到value数组
				for (int i = 0; i < row; i++) {
					for (int j = 0; j < column; j++) {
						value[i][j] = jTable.getValueAt(i, j).toString();
					}
				}
				try {
					Connection conn = DataBase.getCon();
					// 删除studentinfo表中所有数据
					preparedStatement = conn.prepareStatement("delete from studentinfo where true");
					preparedStatement.executeUpdate();
					// 将当前表中的数据依次存放回studentinfo表中
					for (int i = 0; i < row; i++) {
						preparedStatement = conn.prepareStatement(
								"insert into studentinfo values(" + Integer.parseInt(value[i][0]) + ",'" + value[i][1]
										+ "','" + value[i][2] + "','" + value[i][3] + "','" + value[i][4] + "','"
										+ value[i][5] + "','" + value[i][6] + "','" + value[i][7] + "','" + value[i][8]
										+ "','" + value[i][9] + "','" + value[i][10] + "','" + value[i][11] + "','"
										+ value[i][12] + "','" + value[i][13] + "','" + value[i][14] + "')");
						preparedStatement.executeUpdate();
					}
				} catch (ClassNotFoundException e1) {
					e1.printStackTrace();
				} catch (SQLException e1) {
					e1.printStackTrace();
				}
			} else if (flag == 1)
				JOptionPane.showMessageDialog(null, "表格中有空白项！请确保信息的正确填写。", "警告", JOptionPane.INFORMATION_MESSAGE);
			else
				JOptionPane.showMessageDialog(null, "ID不能重复！", "警告", JOptionPane.INFORMATION_MESSAGE);
		}
		if (e.getActionCommand().equals("注销")) {
			// 重启一个登录demo
			new LoginDemo("学生信息管理系统");
			this.setVisible(false);
		}

		if (e.getActionCommand().equals("报表打印")) {
			// 将当前表中数据转化为向量数组
			Vector<Vector> vec = defaultModel.getDataVector();
			try {
				// 将数据写出到文件
				OutputStreamWriter out = new OutputStreamWriter(new FileOutputStream(".\\" + studentname + "信息报表.csv"),
						"utf-8");
				for (int i = 0; i < vec.size(); i++) {
					String str1 = vec.get(i).toString().replace("[", "");
					String str2 = str1.replace("]", "") + "\n";
					out.append(str2);
				}
				out.flush();
				out.close();
				JOptionPane.showMessageDialog(null, "表格成功生成！", "提示", JOptionPane.INFORMATION_MESSAGE);
			} catch (FileNotFoundException e1) {
				JOptionPane.showMessageDialog(null, "写出报表失败！", "提示", JOptionPane.INFORMATION_MESSAGE);
			} catch (IOException e1) {
				JOptionPane.showMessageDialog(null, "写出报表失败！", "提示", JOptionPane.INFORMATION_MESSAGE);
			}
		}
	}

	// JList事件
	public void valueChanged(ListSelectionEvent e) {
		@SuppressWarnings("rawtypes")
		Object obj = ((JList) e.getSource()).getSelectedValue();
		if (obj.equals("主页")) {
			stupanel.setVisible(false);
			homepanel.setVisible(true);
		}
		if (obj.equals("学生信息")) {
			stupanel.setVisible(true);
			homepanel.setVisible(false);
		}
	}
}