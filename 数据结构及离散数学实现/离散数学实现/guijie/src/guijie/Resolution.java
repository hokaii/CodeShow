package guijie;

import java.util.HashSet;
import java.util.Set;

public class Resolution {
	Set<State> stSets = new HashSet<>();
	Char chp = new Char();
	Char chNp = new Char();
	Char chq = new Char();
	Char chNq = new Char();
	Char chr = new Char();
	Char chNr = new Char();
	Char chs = new Char();
	Char chNs = new Char();
	State state1 = new State();
	State state2 = new State();
	State state3 = new State();
	State state4 = new State();
	State state5 = new State();

	public Resolution() {
		chp.setWhat("上学");
		chp.setWho("今天");
		chp.setIs(true);
		chp.setName("p");
		chp.setDesc("今天是否上学");
		chNp.setWhat("上学");
		chNp.setWho("今天");
		chNp.setIs(false);
		chNp.setDesc("今天是否上学");
		chNp.setName("!p");
		chp.setReverseSelf(chNp);
		chNp.setReverseSelf(chp);
		// 带书
		chq.setWhat("今天");
		chq.setWho("带书");
		chq.setIs(true);
		chq.setDesc("带书");
		chq.setName("q");

		chNq.setWhat("今天");
		chNq.setWho("带书");
		chNq.setIs(false);
		chNq.setDesc("带书");
		chNq.setName("!q");
		chq.setReverseSelf(chNq);
		chNq.setReverseSelf(chq);

		chr.setWhat("今天");
		chr.setWho("书包");
		chr.setIs(true);
		chr.setDesc("书包");
		chr.setName("r");

		chNr.setWhat("今天");
		chNr.setWho("书包");
		chNr.setIs(false);
		chNr.setName("!r");
		chNr.setDesc("书包");

		chr.setReverseSelf(chNr);
		chNr.setReverseSelf(chr);

		chs.setWhat("今天");
		chs.setWho("走路上学");
		chs.setIs(true);
		chs.setDesc("走路上学");
		chs.setName("s");

		chNs.setWhat("今天");
		chNs.setWho("走路上学");
		chNs.setIs(false);
		chNs.setName("!s");
		chNs.setDesc("走路上学");

		chs.setReverseSelf(chNs);
		chNs.setReverseSelf(chs);
		
		state1.add_character(chNp);
		state1.add_character(chq);
		state1.add_character(chr);

		state2.add_character(chNs);

		state2.add_character(chNr);

		state3.add_character(chp);

		state4.add_character(chs);

		state5.add_character(chNq);
		stSets.add(state1);
		stSets.add(state2);
		stSets.add(state3);
		stSets.add(state4);
		stSets.add(state5);
	}
	public static void main(String[] args) {
		Resolution main = new Resolution();
		main.guijie();
	}
	private void guijie() {
		while (true) {
			int hashcode = stSets.hashCode();
			boolean has = reso();
			if (hashcode == stSets.hashCode()) {
				System.out.println("归结结束：");
				if (has) {
					System.out.println("归结了空集");
				} else {
					System.out.println("归结失败");
				}
				break;
			}
		}
	}
	private boolean reso() {
		for (State st : stSets) {
			int hasCode = stSets.hashCode();
			for (Char ch : st.getCharSet()) {
				State l2Stment = getContainReverseCharacter(st, ch);
				if (l2Stment != null) {
					System.out.println();
					String strtemp="子句：" + st.toString() + " 和子句L2：" + l2Stment.toString() + " 互补文字为: " + ch.getName();
					State genStatement = generateNewStatement(st, l2Stment, ch);
					if(genStatement.getCharSet().size()>0){
						strtemp+=". 两个子句生成了子句："+genStatement.toString();
					}
					System.out.println(strtemp);
					if (genStatement.getCharSet().size() == 0) {
						return true;
					} else {
						if (stSets.add(genStatement)) {
							break;
						} else {
						}
					}
				}
				System.out.println();
				System.out.println();
			}
			if (hasCode != stSets.hashCode()) {
				break;
			}
		}
		return false;
	}

	// 给定一个子句和该子句中的一个文字，查找是否在子句集中存在一个子句，该子句中存在前面文字的取反
	private State getContainReverseCharacter(State firStatement, Char ch) {
		for (State ch_item : stSets) {
			if (ch_item.getCharSet().contains(ch.getReverseSelf())) {
				return ch_item;
			}
		}
		return null;
	}
	private State generateNewStatement(State l1Stment, State l2Stment, Char ch) {
		State genStatement = new State();
		for (Char ch_Item : l1Stment.getCharSet()) {
			if (!ch_Item.equals(ch)) {
				genStatement.add_character(ch_Item);
			}
		}
		for (Char chItem : l2Stment.getCharSet()) {
			if (!chItem.equals(ch.getReverseSelf())) {
				genStatement.add_character(chItem);
			}
		}
		return genStatement;
	}
}
