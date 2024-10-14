import java.util.Scanner;

public class CircleArea {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		final double PI = 3.14;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("반지름을 입력하세요.");
		
		double radius = sc.nextDouble();
		double Area = radius*radius*PI;
		
		System.out.println(Area);
		}

}
