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
		chp.setWhat("��ѧ");
		chp.setWho("����");
		chp.setIs(true);
		chp.setName("p");
		chp.setDesc("�����Ƿ���ѧ");
		chNp.setWhat("��ѧ");
		chNp.setWho("����");
		chNp.setIs(false);
		chNp.setDesc("�����Ƿ���ѧ");
		chNp.setName("!p");
		chp.setReverseSelf(chNp);
		chNp.setReverseSelf(chp);
		// ����
		chq.setWhat("����");
		chq.setWho("����");
		chq.setIs(true);
		chq.setDesc("����");
		chq.setName("q");

		chNq.setWhat("����");
		chNq.setWho("����");
		chNq.setIs(false);
		chNq.setDesc("����");
		chNq.setName("!q");
		chq.setReverseSelf(chNq);
		chNq.setReverseSelf(chq);

		chr.setWhat("����");
		chr.setWho("���");
		chr.setIs(true);
		chr.setDesc("���");
		chr.setName("r");

		chNr.setWhat("����");
		chNr.setWho("���");
		chNr.setIs(false);
		chNr.setName("!r");
		chNr.setDesc("���");

		chr.setReverseSelf(chNr);
		chNr.setReverseSelf(chr);

		chs.setWhat("����");
		chs.setWho("��·��ѧ");
		chs.setIs(true);
		chs.setDesc("��·��ѧ");
		chs.setName("s");

		chNs.setWhat("����");
		chNs.setWho("��·��ѧ");
		chNs.setIs(false);
		chNs.setName("!s");
		chNs.setDesc("��·��ѧ");

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
				System.out.println("��������");
				if (has) {
					System.out.println("����˿ռ�");
				} else {
					System.out.println("���ʧ��");
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
					String strtemp="�Ӿ䣺" + st.toString() + " ���Ӿ�L2��" + l2Stment.toString() + " ��������Ϊ: " + ch.getName();
					State genStatement = generateNewStatement(st, l2Stment, ch);
					if(genStatement.getCharSet().size()>0){
						strtemp+=". �����Ӿ��������Ӿ䣺"+genStatement.toString();
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

	// ����һ���Ӿ�͸��Ӿ��е�һ�����֣������Ƿ����Ӿ伯�д���һ���Ӿ䣬���Ӿ��д���ǰ�����ֵ�ȡ��
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
