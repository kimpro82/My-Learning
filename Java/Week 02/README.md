## My Java Class - 2st week : Basic Grammar


### `Declaration` & `Assignment` Statement

```JAVA
public class SimpleAdder {
	public static void main(String args[]) {
		int num;
		num = 10 + 20;
		System.out.println(num);
		if (num>10)
			System.out.println("계산 결과가 10보다 큽니다");
	}
}
```

> 30  
> 계산 결과가 10보다 큽니다


### `if` Statements : `if` `if ~ else` `Nested if` `if ~ else if`

```JAVA
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
```

> num1 값이 더 큽니다.  
> num1 = 52  
> num4 = 24  
> num5가 제일 큽니다.  
> num8의 값은 10 이상, 100 미만입니다.


### `while` Statement & `comment`

```JAVA
public class HelloJava10 { // 오른쪽으로 주석
	public static void main(String args[]) {
		int num = 0;
		while (num < 10) {
			System.out.println("Hello, Java");
			num += 1;
		}
	}
}
```

> Hello, Java  
> Hello, Java  
> ……  
> Hello, Java


### Local Variable
- can mix the location of local variable's declaration and assignment only before use it

```JAVA
public class DecExample3 {
	public static void main(String args[]) {
		short num1 = 12;
			System.out.println(num1);
		double num2 = 12.75;
			System.out.println(num2);
		char ch = 'A';
			System.out.println(ch);
		}
	}
```

> 12  
> 12.75  
> A

- Local variables can't be used out of the block.

```JAVA
public class DecExample4 {
	public static void main(String args[]) {
		{
			int num = 10; // method 안에서 선언하면 지역변수
		}
		System.out.println(num); // num 못 불러온다
	}
}
```

> Exception in thread "main" java.lang.Error: Unresolved compilation problem:  
> 	num cannot be resolved to a variable  
> 	at DecExample4.main(DecExample4.java:6)


### `final` Statement
- `final` keyword enables variables to be assigned just once

```JAVA
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
```

> 12.56


### **Composite Operators**

```JAVA
public class AssignmentExample {
	public static void main(String args[]) {
		int num = 17;
		System.out.println(num);
		num += 1;
		System.out.println(num);
		num -= 2;
		System.out.println(num);
		num *= 3;
		System.out.println(num);
		num /= 4;
		System.out.println(num);
		num %= 5;
		System.out.println(num);
		
		int num2 = 0;
		num2++;
		System.out.println(num2);
		++num2;
		System.out.println(num2);
		num2--;
		System.out.println(num2);
		--num2;
		System.out.println(num2);
	}
}
```

> 17
18
16
48
12
 
> 2
1
2
1
0


### **Array**

```JAVA
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
```

> 10
20
30

> 10
20
30

> 10
20
30
50

> 1
6
12

> 10
3
5
3

### `switch ~ case` Statement
- If there's no `break`, it runs all the `case` sequentially
```JAVA
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
```

> case 3  
> B or b


### **Loop** Statements : `while` `do ~ while` `for` `for ~ break` `for ~ continue`

```JAVA
public class WhileForContinueExample {
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
```

> while loop
0
1
2
3
4
5
6
7
8
9

> do-while loop
0
1
2
3
4
5
6
7
8
9
10

> for loop
0
1
2
3
4
5
6
7
8
9

> for loop 2
10
20
30
40
50

> for loop 3 - advanced
10
20
30
40
50

> for loop & break 1
0
1
2
3
4
5

> for loop & break 2
(0,0)
(0,1)
(0,2)
(0,3)
(0,4)
(1,0)
(1,1)
(1,2)
(1,3)
(2,0)
(2,1)
(2,2)
(2,3)
(2,4)

> for loop & break 3 - with using label
(0,0)
(0,1)
(0,2)
(0,3)
(0,4)
(1,0)
(1,1)
(1,2)
(1,3)
Done.

> for loop & Continue
0
1
2
3
4
6
7
8
9
Done.

> for loop & Continue 2
(0,0)
(0,1)
(0,2)
(0,3)
(0,4)
(1,0)
(1,1)
(1,2)
(2,0)
(2,1)
(2,2)
(2,3)
(2,4)
Done.
