package guijie;

import java.util.HashSet;
import java.util.Set;

public class State {
	private Set<Char> char_set = new HashSet<Char>();

	public Set<Char> getCharSet() {
		return char_set;
	}
	public void setCharSet(Set<Char> char_set) {
		this.char_set = char_set;
	}
	public State() {
		super();
	}
	public void add_character(Char add_ch) {
		// TODO Auto-generated method stub
		for (Char ch : char_set) {
			if (ch.getDesc().equals(add_ch.getDesc())) {
				throw new RuntimeException("同一个子句中存在两个相反的变量 p和非p");
			}
		}

		char_set.add(add_ch);

	}
	@Override
	public boolean equals(Object obj) {
		// TODO Auto-generated method stub

		if (obj == this)
			return true;
		if (!(obj instanceof State)) {
			return false;
		}
		State another = (State) obj;
		Set<Char> anotherchSet = another.getCharSet();
		for (Char ch : char_set) {
			if (!(anotherchSet.contains(ch))) {
				return false;
			}
		}
		for (Char ch : anotherchSet) {
			if (!(char_set.contains(ch))) {
				return false;
			}
		}
		return true;
	}
	@Override
	public int hashCode() {
		// TODO Auto-generated method stub
		int result = 17;
		for (Char ch : char_set) {
			result = 31 * result + ch.hashCode();
		}
		return result;
	}
	@Override
	public String toString() {
		String result="";
		for (Char ch : char_set) {
			result+=ch.getName()+" ∨ ";
		}
		if(result.length()>0){
			result=result.substring(0, result.length()-2);
		}
		return result;
	}
}
