public class matrix {
    public static void main(String[] args) {
        int matrix[][] = new int[4][4];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                matrix[i][j] = (int) (Math.random() * 10);
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();

        }
        multiply(matrix);
        addition(matrix);
        substraction(matrix);


    }

    public static int multiply(int matrix[][]) {
        int resultMultiply = matrix[0][0] * matrix[1][1] * matrix[2][2] * matrix[3][3];
        System.out.println("Результат умножения: " + resultMultiply);
        return resultMultiply;


    }

    public static int addition(int matrix[][]) {
        int resultAddition = matrix[0][1] + matrix[0][2] + matrix[0][3] + matrix[1][2] + matrix[1][3] + matrix[2][3];
        System.out.println("Результат сложения: " + resultAddition);
        return resultAddition;


    }

    public static int substraction(int matrix[][]) {
        int resultsubstraction = matrix[1][0] - matrix[2][0] - matrix[2][1] - matrix[3][0] - matrix[3][1] - matrix[3][2];
        System.out.println("Результат вычитания: " + resultsubstraction);
        return resultsubstraction;
    }

}
