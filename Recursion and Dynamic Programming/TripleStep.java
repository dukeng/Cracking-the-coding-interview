// 
// 8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
// Implement a method to count how many possible ways the child can run up the stairs.

// Use memoization to store values that have already been created

int countWays(int n){
	int[] memo = new int[n + 1];
	Arrays.fill(memo, - 1);
	return countWays(n, memo)
}

int countWays(int n, int[] memo){
	if(n < 0){
		return 0;
	}else if (n == 0){
		return 1;
	}else if (memo[n]  > -1){
		return memo[n];
	}else { // new entry
		memo[n] = countWays(n -1, memo) + countWays(n - 2, memo) + countWays(n - 3, memo);
		return memo[n];
	}
}