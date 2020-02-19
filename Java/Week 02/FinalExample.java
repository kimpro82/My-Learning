public class FinalExample {
	public static void main(String args[]) {
		final double pi; // final : 변수값을 한번만 대입 가능
		double radius = 2.0;
		pi = 3.14; // 한번 대입
		double circum = 2 * pi * radius;
		System.out.println(circum);

		/* error
		pi = 3.141592; // 두번째 대입 시도
		double area = pi * radius * radius;
		System.out.println(area);
		*/
	}
}
