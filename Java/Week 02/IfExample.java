
public class IfExample {
	public static void main(String args[]) {
		
		// if
		System.out.println("if");		
		int num1 = 52;
		int num2 = 24;
		if (num1 > num2) {
			System.out.println("num1 값이 더 큽니다.");
			System.out.println("num1 = " + num1);
		}

		// if - else
		System.out.println("\nif-else");
		int num3 = 12;
		int num4 = 24;
		if (num3 > num4)
			System.out.println("num3 = " + num3);
		else
			System.out.println("num4 = " + num4);
		
		// if 중첩
		System.out.println("\nif 중첩");
		int num5 = 52;
		int num6 = 24;
		int num7 = 32;
		if (num5 > num6)
			if (num5 > num7)
				System.out.println("num5가 제일 큽니다.");
		
		// Dangling Else Rule
		System.out.println("\nDangling Else Rule");
		int num8 = 74;
		if (num8 < 10)
			System.out.println("num8의 값은 10 미만입니다.");
		else if (num8 < 100)
			System.out.println("num8의 값은 10 이상, 100 미만입니다.");
		else if (num8 < 1000)
			System.out.println("num8의 값은 100 이상, 1000 미만입니다.");
		else
			System.out.println("num8의 값은 1000 이상입니다.");
	}
}
