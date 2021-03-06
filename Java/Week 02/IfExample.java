public class IfExample {
	public static void main(String args[]) {
		
		// if
		int num1 = 52;
		int num2 = 24;
		if (num1 > num2) {
			System.out.println("num1 ���� �� Ů�ϴ�.");
			System.out.println("num1 = " + num1);
		}

		// if - else
		int num3 = 12;
		int num4 = 24;
		if (num3 > num4)
			System.out.println("num3 = " + num3);
		else
			System.out.println("num4 = " + num4);
		
		// if ��ø
		int num5 = 52;
		int num6 = 24;
		int num7 = 32;
		if (num5 > num6)
			if (num5 > num7)
				System.out.println("num5�� ���� Ů�ϴ�.");
		
		// Dangling Else Rule
		int num8 = 74;
		if (num8 < 10)
			System.out.println("num8�� ���� 10 �̸��Դϴ�.");
		else if (num8 < 100)
			System.out.println("num8�� ���� 10 �̻�, 100 �̸��Դϴ�.");
		else if (num8 < 1000)
			System.out.println("num8�� ���� 100 �̻�, 1000 �̸��Դϴ�.");
		else
			System.out.println("num8�� ���� 1000 �̻��Դϴ�.");
	}
}