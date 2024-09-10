import java.util.Scanner;

public class Scanner_Test {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String name = scanner.next();
        int age = scanner.nextInt();
        double weight = scanner.nextDouble();

        System.out.println(name + " " + weight);
    }
}