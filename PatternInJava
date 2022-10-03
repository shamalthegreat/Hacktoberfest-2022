public class hollowAlphabetPyramid {
  public static void main(String[] args) {
    
    int size = 5, alpha = 65, num = 0;
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size - i - 1; j++) {
        System.out.print(" ");
      }
      for (int k = 0; k < 2 * i + 1; k++) {
        if (i == 0 || i == size - 1) {
          System.out.print((char)(alpha+num++));
        } else {
          if (k == 0 || k == 2 * i) {
            System.out.print((char)(alpha+num++));
          } else {
            System.out.print(" ");
          }
        }
      }
      System.out.println();
    }
  }
}
