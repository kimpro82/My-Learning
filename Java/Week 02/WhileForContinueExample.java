public class WhileForContinueExample {
	public static void main(String args[]) {

		// while loop
		System.out.println("while loop");
		int cnt = 0;
		while (cnt < 10) {
			System.out.println(cnt);
			cnt++;
		}

		// while (true) - infinite loop
			
		// do-while loop
		System.out.println("\ndo-while loop");
		int cnt2 = 0;
		do {
			System.out.println(cnt2);
			cnt2++;
		} while (cnt2 < 10);
			System.out.println(cnt2);
		
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

		// for loop & break 1
		System.out.println("\nfor loop & break 1");
		for (int cnt5=0; cnt5<10; cnt5++) {
			System.out.println(cnt5);
			if (cnt5==5) // not = but ==
				break;
		}
		
		// for loop & break 2
		System.out.println("\nfor loop & break 2");
		for (int row=0; row<3; row++) {
			for (int col=0; col<5 ; col++) {
				System.out.println("(" + row + "," + col + ")");
				if ((row==1)&&(col==3))
					break;
				}
		}
				
		// for loop & break 3 - with using label
		System.out.println("\nfor loop & break 3 - with using label");
		outerLoop: // label
			for (int row=0; row<3; row++) {
				for (int col=0; col<5 ; col++) {
					System.out.println("(" + row + "," + col + ")");
					if ((row==1)&&(col==3))
						break outerLoop;
				}
			}
			System.out.println("Done.");

		// for loop & Continue 1
		System.out.println("\nfor loop & Continue");
		for (int cnt6=0; cnt6<10; cnt6++) {
			if (cnt6==5)
				continue;
			System.out.println(cnt6);
		}
		System.out.println("Done.");

		// for loop & Continue 2
		System.out.println("\nfor loop & Continue 2");
		outerLoop2:
			for (int row=0; row<3; row++) {
				for (int col=0; col<5 ; col++) {
					if ((row==1)&&(col==3))
						continue outerLoop2;
					System.out.println("(" + row + "," + col + ")");
				}
			}
			System.out.println("Done.");

	}
}