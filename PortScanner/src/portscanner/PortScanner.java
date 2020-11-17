package portscanner;

import java.awt.Component;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Vector;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;

public class PortScanner extends JFrame{
	private static final long serialVersionUID = 1L;
	//声明组件
	private JPanel contentPane = new JPanel();
	private JLabel label_1 = new JLabel("起始IP:");
	private JLabel label_2 = new JLabel("结束IP:");
	private JLabel label_3 = new JLabel("端口号:");
	private JLabel label_4 = new JLabel("线程数:");
	private JLabel label_5 = new JLabel("进度");
	private JLabel label_6 = new JLabel("超时:");
	private JTextField textfield_1 = new JTextField();
	private JTextField textfield_2 = new JTextField();
	private JTextField textfield_3 = new JTextField();
	private JTextField textfield_4 = new JTextField();
	private JTextField textfield_5 = new JTextField();
	private JScrollPane scrollPane = new JScrollPane();
	private JButton button_1 = new JButton("扫描");
	private JButton button_2 = new JButton("帮助");
	private JButton button_3 = new JButton("关于...");
	private JButton button_4 = new JButton("退出");
	private JRadioButton radioButton = new JRadioButton("只显示开放端口");
	private static JProgressBar progressBar = new JProgressBar();
	private JTextArea textArea = new JTextArea();
	//声明变量
	private String pattern_1 = "^(2[0-5]{2}|[0-1]?\\d{1,2})(\\.(2[0-5]{2}|[0-1]?\\d{1,2})){3}$";
	private String pattern_2 = "^(?=^.{3,255}$)[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$";
	private boolean flag = false;
	public boolean flag_1 = true;
	public Vector<String> col = new Vector<String>();
	public Vector data = new Vector();
	public DefaultTableModel defaultModel = null;
	private static int min_progress = 0;
	private static int max_progress = 100;
	private static  int currentProgress = min_progress;
	public static JTable table = new JTable();
	//定义服务栏显示的协议, 其他则为unknown
	public static String[] port_to_pro = new String[] {"21", "FTP", "22", "SSH", "23", "Telnet", "25", "SMTP", "37", "Time", 
			"53", "DNS", "68", "DHCP", "69", "TFTP", "80", "HTTP", "109", "pop2", "110", "pop3", "123", "NTP", "143", "IMAP", 
			"161", "SNMP", "443", "HTTPS"};
	//声明button_1中用到的变量
	ExecutorService thread_pool = null;
	String IP_1 = null;
	String IP_2 = null;
	String port = null;
	String thread = null;
	String time = null;
	Pattern r_1 = null;
	Pattern r_2 = null;
	Matcher m_1 = null;
	Matcher m_2 = null;
	Matcher m_3 = null;
	String start_ip = null;
	String end_ip = null;
	InetAddress address = null;
	List<Integer> port_list = null;
	int thread_num;
	int timeout;
	String all_ip;
	List<String> IP_list = null;
	String[] IPs = null;
	GoThread t = null;
	
	//主函数
	public static void main(String[] args){
		new PortScanner("端口扫描器");
	}
	
	public PortScanner(String title) {
		super(title);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLayout(null);
		this.setResizable(false);
		this.setSize(453, 323);
		// 使界面处于屏幕正中间
		Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
		int ScreenSizeWidth = (int)dimension.getWidth();
		int ScreenSizeHeight = (int)dimension.getHeight();
		int WindowWidth = this.getWidth();
		int WindowHeight = this.getHeight();
		this.setLocation(ScreenSizeWidth / 2 - WindowWidth / 2, ScreenSizeHeight / 2 - WindowHeight / 2);
		this.setContentPane(contentPane);
		init();
		this.setVisible(true);
	}
	
	class GoThread extends Thread {
		public void run(){
			try {
				go();
			}catch(NullPointerException e) {
				JOptionPane.showMessageDialog(null, "程序出错，错误代码1", "警告",JOptionPane.WARNING_MESSAGE);
			}
		}
	}
	
	private void go() {
		try {
			//启动线程投入线程池
			for(int i = 0; i < thread_num; i++) {
				Function func = new Function(thread_num, i, timeout, IPs, port_list);
				thread_pool.execute(func);
			}
			thread_pool.shutdown();
			while(true) {
				if(thread_pool.isTerminated()) {
					textArea.setText("扫描结束");
					break;
				}
				try {
					Thread.sleep(1000);
				}catch(InterruptedException e3) {
				}
			}
			currentProgress = 500;
			//使按钮可点击
			button_1.setEnabled(true);
			radioButton.setEnabled(true);
			t = null;
		}catch(NullPointerException e) {
			JOptionPane.showMessageDialog(null, "程序出错，错误代码2", "警告",JOptionPane.WARNING_MESSAGE);
		}
	}
	
	public void init() {
		//设置组件属性
		col.addElement("IP地址");
		col.addElement("端口");
		col.addElement("端口状态");
		col.addElement("服务");
		defaultModel = new DefaultTableModel(data, col);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(null);
		contentPane.setVisible(true);
		label_1.setBounds(10, 10, 42, 18);
		label_2.setBounds(10, 42, 42, 18);
		label_3.setBounds(10, 74, 42, 18);
		label_4.setBounds(10, 106, 42, 18);
		label_5.setBounds(10, 210, 42, 15);
		label_6.setBounds(10, 138, 42, 18);
		textfield_1.setBounds(56, 9, 99, 21);
		textfield_2.setBounds(56, 41, 99, 21);
		textfield_3.setBounds(56, 73, 99, 21);
		textfield_4.setBounds(56, 105, 99, 21);
		textfield_5.setBounds(56, 137, 99, 21);
		textfield_1.setColumns(10);
		textfield_2.setColumns(10);
		textfield_3.setColumns(10);
		textfield_4.setColumns(10);
		textfield_1.setText("157.122.98.13");//测试: www.163.com
		textfield_2.setText("157.122.98.20");
		textfield_3.setText("53-80");//测试: 53号为DNS, 80号为HTTP
		textfield_4.setText("5");
		textfield_5.setText("300");
		scrollPane.setBounds(165, 31, 272, 171);
		table.setEnabled(false);
		table.setModel(defaultModel);
		scrollPane.setViewportView(table);
		button_1.setBounds(10, 240, 95, 35);
		button_2.setBounds(120, 240, 95, 35);
		button_3.setBounds(230, 240, 95, 35);
		button_4.setBounds(340, 240, 95, 35);
		radioButton.setBounds(161, 8, 121, 23);
		progressBar.setBounds(44, 212, 383, 14);
		progressBar.setMinimum(min_progress);
		progressBar.setMaximum(max_progress);
		progressBar.setStringPainted(true);
		textArea.setBounds(10, 167, 145, 33);
		textArea.setText("欢迎使用端口扫描器！");
		textArea.setEditable(false);
		contentPane.add(button_1);
		contentPane.add(button_2);
		contentPane.add(button_3);
		contentPane.add(button_4);
		contentPane.add(label_1);
		contentPane.add(label_2);
		contentPane.add(label_3);
		contentPane.add(label_4);
		contentPane.add(label_5);
		contentPane.add(label_6);
		contentPane.add(progressBar);
		contentPane.add(radioButton);
		contentPane.add(scrollPane);
		contentPane.add(textArea);
		contentPane.add(textfield_1);
		contentPane.add(textfield_2);
		contentPane.add(textfield_3);
		contentPane.add(textfield_4);
		contentPane.add(textfield_5);
		
		//扫描按钮事件监听器
		button_1.addActionListener(new ActionListener() {
			public synchronized void actionPerformed(ActionEvent e) throws NullPointerException{
				currentProgress = 0;
				textArea.setText("扫描开始");
				data.clear();
				button_1.setEnabled(false);
				radioButton.setEnabled(false);
				thread_pool = Executors.newCachedThreadPool();
				IP_1 = textfield_1.getText();
				IP_2 = textfield_2.getText();
				port = textfield_3.getText();
				thread = textfield_4.getText();
				time = textfield_5.getText();
				r_1 = Pattern.compile(pattern_1);
				r_2 = Pattern.compile(pattern_2);
				m_1 = r_1.matcher(IP_1);
				m_2 = r_1.matcher(IP_2);
				m_3 = r_2.matcher(IP_1);
				start_ip = new String();
				end_ip = new String();
				address = null;
				port_list = new ArrayList<Integer>();
				IP_list = new ArrayList<String>();
				IPs = new String[] {};
				//检查IP地址输入是否合法
				if(m_1.matches()) {
					if(m_2.matches()) {
						start_ip = IP_1;
						end_ip = IP_2;
					}
					else {
						JOptionPane.showMessageDialog(null, "结束IP格式错误！", "警告",JOptionPane.WARNING_MESSAGE);
						button_1.setEnabled(true);
						return;
					}
				}else if(m_3.matches()) {
					//域名转IP
					try {
						address = InetAddress.getByName(IP_1);
						start_ip = address.getHostAddress().toString();
						end_ip = address.getHostAddress().toString();
					}catch(UnknownHostException e1) {
						JOptionPane.showMessageDialog(null, "找不到目的主机！", "信息", JOptionPane.PLAIN_MESSAGE);
						button_1.setEnabled(true);
						return;
					}
				}else {
					JOptionPane.showMessageDialog(null, "起始IP格式错误！", "警告", JOptionPane.WARNING_MESSAGE);
					button_1.setEnabled(true);
					return;
				}
				//判断端口号输入是否合法
				try {
					int num = port.indexOf("-");
					String[] port1 = port.split("\\,");
					if(num >= 0)
						port1 = null;
					if(port1 != null) {
						for(String j: port1) {
							if(Integer.parseInt(j) < 0 || Integer.parseInt(j) > 65535) {
								JOptionPane.showMessageDialog(null, "端口号应>=0且<=65535", "警告", JOptionPane.WARNING_MESSAGE);
								button_1.setEnabled(true);
								return;
							}
						}
						for(String k : port1) {
							if(port_list.indexOf(Integer.parseInt(k)) == -1)
								port_list.add(Integer.parseInt(k));
						}
						flag = true;
					}
					if(num > 0) {
						int num_1 = Integer.parseInt(port.substring(0, num));
						int num_2 = Integer.parseInt(port.substring(num+1, port.length()));
						if(num_1 >= 0 && num_1 <= 65535 && num_2 >= 0 && num_2 <= 65535 && num_1 < num_2) {
							for(int i = num_1; i <= num_2; i++) {
								port_list.add(i);
							}
							flag = true;
						}
						else {
							JOptionPane.showMessageDialog(null, "端口号应>=0且<=65535且前一个端口号应小于后一个!", "警告", JOptionPane.WARNING_MESSAGE);
							button_1.setEnabled(true);
							return;
						}
					}
				}catch(NumberFormatException ex) {
					JOptionPane.showMessageDialog(null, "端口号格式错误！", "警告", JOptionPane.WARNING_MESSAGE);
					button_1.setEnabled(true);
					return;
				}
				if(!flag) {
					JOptionPane.showMessageDialog(null, "端口号格式错误！", "警告", JOptionPane.WARNING_MESSAGE);
					button_1.setEnabled(true);
					return;
				}
				//判断线程输入是否合法
				try {
					thread_num = Integer.parseInt(thread);
					if(thread_num <= 0) {
						JOptionPane.showMessageDialog(null, "线程格式错误！", "警告", JOptionPane.WARNING_MESSAGE);
						button_1.setEnabled(true);
						return;
					}
				}catch(NumberFormatException ex1) {
					JOptionPane.showMessageDialog(null, "线程格式错误！", "警告", JOptionPane.WARNING_MESSAGE);
					button_1.setEnabled(true);
					return;
				}
				//判断超时输入是否合法
				try {
					timeout = Integer.parseInt(time);
					if(timeout <= 0) {
						JOptionPane.showMessageDialog(null, "超时格式错误！", "警告", JOptionPane.WARNING_MESSAGE);
						button_1.setEnabled(true);
						return;
					}
				}catch(NumberFormatException ex2) {
					JOptionPane.showMessageDialog(null, "超时格式错误！", "警告", JOptionPane.WARNING_MESSAGE);
					button_1.setEnabled(true);
					return;
				}
				//分配子线程给进度条更新进度
				new Thread(new Runnable() {
				    public void run() {
				    	while(true) {
				    		if(currentProgress == 500) {
				    			progressBar.setValue(100);
				    			break;
				    		}
				    		if(currentProgress < 100)
				    			progressBar.setValue(currentProgress);
				    		try {
								Thread.sleep(500);
							} catch (InterruptedException e) {
								JOptionPane.showMessageDialog(null, "程序出错，错误代码3", "警告",JOptionPane.WARNING_MESSAGE);
							}
				    	}
				    }
				   }).start();
				//执行功能
				String[] from_ip = start_ip.split("\\.");
				String[] to_ip = end_ip.split("\\.");
				int[] int_ipf = new int[4];
				int[] int_ipt = new int[4];
				for(int i = 0; i < 4; i++) {
					int_ipf[i] = Integer.parseInt(from_ip[i]);
					int_ipt[i] = Integer.parseInt(to_ip[i]);
				}
				//四层循环获取IP地址段中全部IP地址
				for(int ip1 = int_ipf[0]; ip1 <= int_ipt[0]; ip1++) {
					for(int ip2 = (ip1 == int_ipf[0] ? int_ipf[1] : 0); ip2 <= (ip1 == int_ipt[0] ? int_ipt[1] : 255); ip2++) {
						for(int ip3 = (ip2 == int_ipt[1] ? int_ipf[2] : 0); ip3 <= (ip2 == int_ipt[1] ? int_ipt[2] : 255); ip3++) {
							for(int ip4 = (ip3 == int_ipt[2] ? int_ipf[3] : 0); ip4 <= (ip3 == int_ipt[2] ? int_ipt[3] : 255); ip4++) {
								all_ip = ip1 + "." + ip2 + "." + ip3 + "." + ip4;
								IP_list.add(all_ip);
							}
						}
					}
				}
				IPs = IP_list.toArray(new String[IP_list.size()]);
				//分配子线程执行功能
				if(t == null) {
					t = new GoThread();
					t.start();
				}
			}
		});
		
		//帮助按钮事件监听器
		button_2.addActionListener(new ActionListener() {
			public synchronized void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(null, "输入起始IP地址结束IP地址或者域名；输入单个端口号用,分隔输入端口号段用-分隔。", "帮助", JOptionPane.PLAIN_MESSAGE);
			}
		});
		
		//关于按钮事件监听器
		button_3.addActionListener(new ActionListener() {
			public synchronized void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(null, "作者:郑洪铠", "关于", JOptionPane.PLAIN_MESSAGE);
			}
		});
		
		//退出按钮事件监听器
		button_4.addActionListener(new ActionListener() {
			public synchronized void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		
		//可选按钮事件监听器
		radioButton.addActionListener(new ActionListener() {
			public synchronized void actionPerformed(ActionEvent e) throws NullPointerException{
				if(radioButton.isSelected()) {
				Vector data_1 = new Vector();
					//筛选端口开放的vector
					for(int i = 0; i < data.size(); i++) {
						if(((Vector<String>) data.get(i)).get(2) == "open") {
							data_1.addElement(data.get(i));
						}
					}
					//替换model
					DefaultTableModel defaultModel_1 = new DefaultTableModel(data_1, col);
					table.setModel(defaultModel_1);
					try {
						table.updateUI();
					}catch(NullPointerException e5) {
						JOptionPane.showMessageDialog(null, "程序出错，错误代码4", "警告",JOptionPane.WARNING_MESSAGE);
					}
				}else {
					table.setModel(defaultModel);
					try {
						table.updateUI();
					}catch(NullPointerException e4) {
						JOptionPane.showMessageDialog(null, "程序出错，错误代码5", "警告",JOptionPane.WARNING_MESSAGE);
					}
				}
			}
		});
	}
	
	//线程池线程并行调用run
	class Function implements Runnable{
		private List<Integer> port_list_1 = new ArrayList<Integer>();
		private int thread_num, serial;
		private int timeout;
		private String[] IPs = new String[] {};
		private int num;
		
		public Function(int numthread, int serial, int time_out, String[] IP_s, List<Integer> port_list) {
			this.thread_num = numthread;
			this.serial = serial;
			this.timeout = time_out;
			this.IPs = IP_s;
			this.port_list_1 = port_list;
		}

		public synchronized void run() throws NullPointerException{
			try {
				num = IPs.length * port_list_1.size();
				if(num > 100)
					num = 1;
				else
					num = 100 / num;
				int ip = 0;
				for(ip = serial; ip <= IPs.length-1; ip += thread_num) {
					for(int j : port_list_1) {
						try {
							//创建socket对象
							Socket s = new Socket();
							//尝试用创建的socket与目的IP建立连接
							s.connect(new InetSocketAddress(IPs[ip], j), timeout);
							if(s.isConnected()) {
								//连接成功证明端口开放
								boolean flag_2 = false;
								Vector<String> v = new Vector<String>();
								v.addElement(IPs[ip]);
								v.addElement(j+"");
								v.addElement("open");
								//判断端口号是否为常见端口
								for(int k = 0; k < port_to_pro.length; k=k+2) {
									if(Integer.parseInt(port_to_pro[k]) == j) {
										v.addElement(port_to_pro[k+1]);
										flag_2 = true;
									}
								}
								//不常见则显示为unknown
								if(!flag_2)
									v.addElement("unknown");
								data.addElement(v);
								try {
									defaultModel.fireTableDataChanged();
								}catch(NullPointerException e) {
									JOptionPane.showMessageDialog(null, "程序出错，错误代码6", "警告",JOptionPane.WARNING_MESSAGE);
								}
								currentProgress += num;
							}
							s.close();
						}catch(IOException e) {
							//连接不成功,证明该端口关闭
							boolean flag_3 = false;
							Vector<String> u = new Vector<String>();
							u.addElement(IPs[ip]);
							u.addElement(j+"");
							u.addElement("close");
							//判断端口号是否为常见端口
							for(int k = 0; k < port_to_pro.length; k=k+2) {
								if(Integer.parseInt(port_to_pro[k]) == j) {
									u.addElement(port_to_pro[k+1]);
									flag_3 = true;
								}
							}
							if(!flag_3)
								u.addElement("unknow");
							data.addElement(u);
							try {
								//提醒JTable重新绘制
								defaultModel.fireTableDataChanged();
							}catch(NullPointerException e1) {
								JOptionPane.showMessageDialog(null, "程序出错，错误代码7", "警告",JOptionPane.WARNING_MESSAGE);
							}
							currentProgress += num;
						}
					}
				}
			}catch(NullPointerException e) {
				JOptionPane.showMessageDialog(null, "程序出错，错误代码8", "警告",JOptionPane.WARNING_MESSAGE);
			}
		}
	}
}