package InfoManage;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

//有关数据库的操作
public class DataBase{
	//时区报错:set global time_zone='+8:00';
	private static final String url = "jdbc:mysql://localhost:3306/studentinfo?&useSSL=false";
	private static final String username = "root";
	private static final String password = "980517";
	
	//获取数据库操作对象
	public static Connection getCon() throws SQLException, ClassNotFoundException {
		Connection con = null;
		Class.forName("com.mysql.cj.jdbc.Driver");
		con = DriverManager.getConnection(url,username, password);
		return con;
	}
	
	//根据ID获取数据库中的信息
	public static String getInfo(Connection con, String id, String str) throws SQLException{
		Statement stmt = con.createStatement();
		ResultSet rs = stmt.executeQuery("select "+ str +" from studentinfo where ID = '" + id +"'");
		while(rs.next()) 
			return rs.getString(1);
		return null;
	}
	
	//传入sql语句获取
	public static ResultSet getSelect(Connection con, String sql) {
			ResultSet rs = null;
			Statement statement;
			try {
				statement = con.createStatement();//获取数据库查询结果存储对象
				rs = statement.executeQuery(sql);//执行 sql 语句
			}catch(SQLException e) {
				e.printStackTrace();
			}
		return rs;
		
	}
}