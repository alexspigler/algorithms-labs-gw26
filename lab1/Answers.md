# Proof

$4n^2 + 7n +6 = O(n^2)$

$n \ge 1$
$n^2 \ge n \Rightarrow 7n^2 \ge 7n$
$n^2 \ge 1 \Rightarrow 6n^2 \ge 6$
$4n^2 + 7n^2 + 6n^2 \ge 4n^2 + 7n + 6$
$17n^2 \ge 4n^2 + 7n + 6$

$\therefore 4n^2 + 7n +6 = O(n^2)$, $n_0 = 1$ and $c = 17$

---

# Proof w/ nontrivial $n_0$

$4n^2 + 7n +6 = O(n^2)$

$n \ge 7$
$n^2 \ge 7n$
$n^2 \ge 49 \Rightarrow n^2 \ge 6$
$4n^2 + n^2 + n^2 \ge 4n^2 +7n +6$
$6n^2 \ge 4n^2 + 7n +6$
$\therefore 4n^2 + 7n + 6 = O(n^2)$, $n_0 = 7$ and $c = 6$

---

# Proof Big-Omega

$\frac{3}{4}n^2 -6n = \Omega (n^2)$

Set $\frac{3}{4}n^2 - 6n \ge cn^2$, for all $n\ge n_0$
$6n \le \frac{3}{8}n^2 \Rightarrow 6 \le \frac{3}{8}n \Rightarrow 16 \le n \Rightarrow n_0 = 16$
$\frac{3}{4}n^2 - 6n \ge \frac{3}{4}n^2 - \frac{3}{8}n^2 \Rightarrow \frac{3}{4}n^2 - 6n \ge \frac{3}{8}n^2$
$\therefore \frac{3}{4}n^2 - 6n = \Omega(n^2)$, $n_0 = 16$ and $c = \frac{3}{8}$

---

# Big-Theta Proof

$f(n) = 5n^2 + 8n + 3 = \Theta(n^2)$

$n \ge 1 \Rightarrow n^2 \ge 1 \Rightarrow 3n^2 \ge 3$
$n^2 \ge n \Rightarrow 8n^2 \ge 8n$
$5n^2 + 8n^2 + 3n^2 \ge 5n^2 + 8n + 3$
$16n^2 \ge 5n^2 + 8n + 3$
$f(n) = O(n^2)$, $n_{0,1} = 1$, and $c_2 = 16$

$5n^2 + 8n + 3 \ge 5n^2$ for $n \ge 1$
$f(n) = \Omega(n^2)$, $n_{0,2} = 1$, and $c_1 = 5$

$n_0 = \text{max}({n_{0,1}, n_{0,2}}) = 1$
$c_1=5$, $c_2 = 16$
$f(n) = \Theta(n^2)$

---

# Answer the following questions

$$fib(n) = fib(n-1) + fib(n-2)$$
$$fib(0) = fib(1) = 1$$

1. 
$$fib(5) = fib(4) + fib(3)$$
$$= fib(3) + fib(2) + fib(2) + fib(1)$$
$$ = fib(2) + fib(1) + fib(2) + fib(2) + fib(1)$$
$$= 5$$

2.
$$fib(6) = fib(5) + fib(4)$$
$$= 5 + fib(3) + fib(2)$$
$$= 5 + fib(2) + fib(1) + fib(2)$$
$$= 5 + 3 = 8$$

3.
$$fib(7) = fib(6) + fib(5) = 8 + 5 = 13$$

4.
$$fib(8) = fib(7) + fib(6) = 13 + 8 = 21$$

5.
$$fib(9) = fib(8) + fib(7) = 21 + 13 = 34$$

---

1. Explain what the code above is doing.
A: It is a recursive function. It calls for the fibonacci value one below and two below the integer that was put in. And it then calculates that fibonacci value by calling the 2 values below it, and on and on until it hits 1 or 0, and then it sums all the results.

2. What happens if we remove the "if ... return ..." and only keep the last line?
A: It won't stop (and then just error out).  Because the recursive calls never end, it will be calling fibonacci(-20) and that doesn't make sense.

3. What is fibonacci(20)? how much time did it take to calculate that?
A: fibonacci(20) = 6765, calculating this took 1.2567e-03 seconds.

4. What is fibonacci(30)? how much time did it take to calculate that?
A: fibonacci(30) = 832040, calculating this took 8.0916e-02 seconds.

5. How much time did it take you to calculate fibonacci(40)? (this might take a while...)
A: fibonacci(40) = 102334155, calculating this took 7.1348e+00 seconds.

---

