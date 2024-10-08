import java.lang.ArithmeticException;
import java.util.Scanner;

public class DivideByZero {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("나뉨수를 입력하시오> ");
        int dividend = scanner.nextInt();
        System.out.println("나눗수를 입렷하시오> ");
        int divisor = scanner.nextInt();
        try {
            System.out.println(dividend+"를 "+divisor+"로 나누면 몫은 " + dividend / divisor + "입니다.");
        } catch (ArithmeticException e) {
            System.out.println("0은 나눗수로 사용할 수 없습니다..");
        };
        scanner.close();
    }
}
