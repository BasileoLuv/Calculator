public class Calculator {

    public static void main(String[] args) {
        double x;
        double y;
        String operator;

        x = Double.parseDouble(args[0]);
        operator = args[1];
        y = Double.parseDouble(args[2]);

        if (operator.equals("*")) {
            System.out.println("= " + (x * y));
        }
        if (operator.equals("/")) {
            System.out.println("= " + (x / y));
        }
        if (operator.equals("+")) {
            System.out.println("= " + (x + y));
        }
        if (operator.equals("-")) {
            System.out.println("= " + (x - y));
        }
    }
}