
public class SwitchExample {
	public static void main(String args[]) {
		
		// switch 1
		int num = 3;
		switch (num) {
			case 1 :
				System.out.println("case 1");
				break;
			case 2 :
				System.out.println("case 2");
				break;
			case 3 :
				System.out.println("case 3");
				break;
			default :
				System.out.println("default");
				break;
		}

		// switch 2 - 둘 이상의 값에 대해 같은 처리
		char ch = 'b';
		switch (ch) {
			case 'A' : // not ; but :
			case 'a' :
				System.out.println("A or a");
				break;
			case 'B' :
			case 'b' :
				System.out.println("B or b");
				break;
			default :
				System.out.println("Nothing");
				break;		
		}
	}
}
