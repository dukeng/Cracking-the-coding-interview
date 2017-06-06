/**
 * 4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
 */
public class MinimalTree {



  public static TreeNode createMinimalBST(int[] array){
    return createMinimalBST(array, 0 , array.length - 1);
  }

  private static TreeNode createMinimalBST(int[] array, int start, int end){
    if(end < start){
      return null;
    }
    int mid = (start + end ) / 2;
    TreeNode n = new TreeNode(array[mid]);
    n.left = createMinimalBST(array, start, mid - 1);
    n.right = createMinimalBST(array, mid + 1, end);
    return n;
  }

  public static void main(String[] args){
    int[] input = {};
    TreeNode output = createMinimalBST(input);
    output.traverse();
  }

}
