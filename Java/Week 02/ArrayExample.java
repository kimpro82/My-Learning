
public class ArrayExample {
	public static void main(String args[]) {
		int arr[];
		arr = new int[10];
		arr[0] = 10;
		arr[1] = 20;
		arr[2] = arr[0] + arr[1];
		System.out.println(arr[0]);
		System.out.println(arr[1]);
		System.out.println(arr[2]);
		
		int table[][] = new int[3][4];
		table[0][0] = 10;
		table[1][1] = 20;
		table[2][3] = table[0][0] + table[1][1];
		System.out.println(table[0][0]);
		System.out.println(table[1][1]);
		System.out.println(table[2][3]);
		
		int arr2[] = {10, 20, 30, 40, 50};
		System.out.println(arr2[0]);
		System.out.println(arr2[1]);
		System.out.println(arr2[2]);
		System.out.println(arr2[4]);
		
		int table2[][] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
		System.out.println(table2[0][0]);
		System.out.println(table2[1][1]);
		System.out.println(table2[2][3]);
	
		System.out.println(arr.length);
		System.out.println(table.length);
		System.out.println(arr2.length);
		System.out.println(table2.length);
		}
	}	
