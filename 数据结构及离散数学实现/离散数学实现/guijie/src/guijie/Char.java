package guijie;

/**文字 
 * p: 今天是下雨
 * q： 今天带伞
 * @author lenovo
 *
 */
public class Char {
	private String name;
	private String who;
	private String what;
	private boolean is=true;
	private String desc;
	private Char reverseSelf;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Char getReverseSelf() {
		return reverseSelf;
	}
	public void setReverseSelf(Char reverseSelf) {
		this.reverseSelf = reverseSelf;
	}
	public String getWho() {
		return who;
	}
	public void setWho(String who) {
		this.who = who;
	}
	public String getDesc() {
		return desc;
	}
	public void setDesc(String desc) {
		this.desc = desc;
	}
	public String getWhat() {
		return what;
	}
	public void setWhat(String what) {
		this.what = what;
	}
	public boolean isIs() {
		return is;
	}
	public void setIs(boolean is) {
		this.is = is;
	}
	public Char(String who, String what, boolean is) {
		super();
		this.who = who;
		this.what = what;
		this.is = is;
	}
	public Char() {
		super();
		
	}
}
