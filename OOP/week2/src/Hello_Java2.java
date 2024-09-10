public class Hello_Java2 {
    public static int mul(int a, int b) {
        return a * b;
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub

        int i = 10;
        int j = 20;

        int result = mul(i, j);
        System.out.print(i+j);
        System.out.println("헬로 자바2" + " " + result);

        float f= 10.0f;
        double d = 10.0;

//        while(true) {
//            System.out.println("Hello World!");
//        }

//        String str = "대한민국";
        String str = new String("대한민국");
        System.out.println(str);
        // 상수
        final double PI = 3.141592;
        System.out.println(PI);

        // 원의 면적을 구하는 프로그램을 작성해보자.
    }
}