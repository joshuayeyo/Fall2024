import java.util.Scanner;

public class Circle_Area {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the radius of the circle> ");
        double radius = scanner.nextDouble();

        final double PI = 3.14;

        double area = radius * radius * PI;

        System.out.println(area);
    }
}
