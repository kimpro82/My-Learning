public class FinalExample {
	public static void main(String args[]) {
		final double pi; // final : �������� �ѹ��� ���� ����
		double radius = 2.0;
		pi = 3.14; // �ѹ� ����
		double circum = 2 * pi * radius;
		System.out.println(circum);

		/* error
		pi = 3.141592; // �ι�° ���� �õ�
		double area = pi * radius * radius;
		System.out.println(area);
		*/
	}
}
