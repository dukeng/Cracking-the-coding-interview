
/*
  4.4 Check Balanced: Implement a function to check if a binary tree is balanced. 
  For the purposes of this question, a balanced tree is defined to be a tree such that 
  the heights of the two subtrees of any node never differ by more than one.
*/


int checkHeight(TreeNode root){
	if (root == null) return -1; // return this so that the empty branch is on the level of the parent's node
	int leftHeight = checkHeight(root.left);
	if (leftHeight == Integer.MIN_VALUE) return Integer.MIN_VALUE; // pass error up to node

	int rightHeight = checkHeight(root.right);
	if (rightHeight == Integer.MIN_VALUE) return Integer.MIN_VALUE; // pass error up to node

	int heightDiff = leftHeight - rightHeight; // We can reuse Integer.MIN_VALUE to make left and right branches work
	if(Math.abs(heightDiff) > 1){
		return Integer.MIN_VALUE; // pass error up
	} else{
		return Math.max(leftHeight, rightHeight) + 1;
	}
}

boolean isBalanced(TreeNode root){
	return checkHeight(root) != Integer.MIN_VALUE;
}