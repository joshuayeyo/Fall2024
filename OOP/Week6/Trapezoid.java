import java.util.Scanner;

public class Trapezoid {
    int bottom_width;
    int top_width;
    int height;

    public double getArea() {
        return 0.5*height*(bottom_width+top_width);
    }

    public static void main(String[] args) {
        Trapezoid t = new Trapezoid();
        Scanner scanner = new Scanner(System.in);
        System.out.println("사다리꼴의 면적을 구하는 프로그램입니다.");

        System.out.print("아래 길이를 입력하세요> ");
        t.bottom_width = scanner.nextInt();
        System.out.print("위의 길이를 입력하세요> ");
        t.top_width = scanner.nextInt();
        System.out.print("높이를 입력하세요> ");
        t.height = scanner.nextInt();

        System.out.println("사다리꼴의 면적은> " + t.getArea());
    }
}
