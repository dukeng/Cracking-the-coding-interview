// Data Structure class
public class TreeNode {
  public int value;
  public TreeNode left;
  public TreeNode right;
  public TreeNode(int value){
    this.value = value;
  }

  public void traverse(){
    inOrder(this);
  }

  public void inOrder(TreeNode node){
    if (node != null){
      inOrder(node.left);
      System.out.println((node.value));
      inOrder(node.right);
    }

  }
}
