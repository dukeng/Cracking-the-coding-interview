

// 4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. 
// You may assume that each node has a link to its parent.

TreeNode inOrderSuccessor(TreeNode n){
	if (n == null){
		return null;
	}
	// If there is a right subtree, then find the left-most of that subtree and retrun
	if (n.right != null) {
		return leftMostNode(n.right);
	}else{
		TreeNode q = n;
		TreeNode x = q.parent;
		while(x != null && x.left != q){
			q = x;
			x = q.parent;
		}
		return x;
	}
}

// n is not null
TreeNode leftMostNode(TreeNode n){
	while(n.left != null){
		n = n.left;
	}
	return n;
}