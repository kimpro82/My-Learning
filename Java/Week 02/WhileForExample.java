
public class WhileForExample {
	public static void main(String args[]) {

		// while loop
		System.out.println("while loop");
		int cnt = 0;
		while (cnt < 10) {
			System.out.println(cnt);
			cnt++;
			
		// while (true) - infinite loop
			
		// do-while loop
		System.out.println("\ndo-while loop");
		int cnt2 = 0;
		do {
			System.out.println(cnt2);
			cnt2++;
		} while (cnt2 < 10);
		System.out.println(cnt2);
		}
		
		// for loop
		System.out.println("\nfor loop");
		for (int cnt3=0; cnt3 < 10; cnt3++)
			System.out.println(cnt3);
		
		// for loop 2
		System.out.println("\nfor loop 2");
		int arr[] = {10,20,30,40,50};
		for (int cnt4=0; cnt4 < arr.length; cnt4++) {
			System.out.println(arr[cnt4]);
		}
		
		// for loop 3 - advanced
		System.out.println("\nfor loop 3 - advanced");
		int arr2[] = {10,20,30,40,50};
		for (int num : arr2) {
			System.out.println(num);
		}

		// for loop 4 - break
		System.out.println("\nfor loop 4 - using break");
		for (int cnt5=0; cnt5<10; cnt5++) {
			System.out.println(cnt5);
			if (cnt5==5) // not = but ==
				break;
		}
		
		// for loop 5 - break 2
		System.out.println("\nfor loop 5 - using break");
		for (int cnt5=0; cnt5<10; cnt5++) {
			System.out.println(cnt5);
			if (cnt5==5) // not = but ==
				break;
				}
				
				
	}
}
