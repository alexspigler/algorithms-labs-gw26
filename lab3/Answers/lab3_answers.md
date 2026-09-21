## Part 1: Binary Heaps and the Heapsort Structure

### 1.1 Trace — Sift-down `max_heapify_down([4, 10, 8, 5, 1, 2, 7], 0, 7)`

| Step | Current `i` | Value at `i` | Children (left, right) | Largest index | Action taken | Array afterward |
|---|---|---|---|---|---|---|
| 1 | 0 | 4 | `left=1` (10), `right=2` (8) | 1 | Swap `arr[0]` with `arr[1]` | `[10, 4, 8, 5, 1, 2, 7]` |
| 2 | 1 | 4 | `left=3` (5), `right=4` (1) | 3 | Swap `arr[1]` with `arr[3]` | `[10, 5, 8, 4, 1, 2, 7]` |
| 3 | 3 | 4 | `left=7` (none), `right=8` (none) | 3 | No swap — `i` is a leaf (`largest == i`), break | `[10, 5, 8, 4, 1, 2, 7]` |

### 1.2 Trace — Heapsort extraction on `[15, 12, 8, 6, 2, 3, 7]`

| Pass (`end`) | Swap root with `arr[end]` | Active heap size | Active heap after `max_heapify_down` | Sorted suffix | Full array afterward |
|---|---|---|---|---|---|
| 6 | Swap `15` with `7` | 6 | `[12, 7, 8, 6, 2, 3]` | `[15]` | `[12, 7, 8, 6, 2, 3, 15]` |
| 5 | Swap `12` with `3` | 5 | `[8, 7, 3, 6, 2]` | `[12, 15]` | `[8, 7, 3, 6, 2, 12, 15]` |
| 4 | Swap `8` with `2` | 4 | `[7, 6, 3, 2]` | `[8, 12, 15]` | `[7, 6, 3, 2, 8, 12, 15]` |
| 3 | Swap `7` with `2` | 3 | `[6, 2, 3]` | `[7, 8, 12, 15]` | `[6, 2, 3, 7, 8, 12, 15]` |
| 2 | Swap `6` with `3` | 2 | `[3, 2]` | `[6, 7, 8, 12, 15]` | `[3, 2, 6, 7, 8, 12, 15]` |
| 1 | Swap `3` with `2` | 1 | `[2]` | `[3, 6, 7, 8, 12, 15]` | `[2, 3, 6, 7, 8, 12, 15]` |

**Final sorted array returned by `heap_sort`:** `[2, 3, 6, 7, 8, 12, 15]`

**1.4A — Why a Max-Heap produces an ascending sort (and a Min-Heap a descending sort):**
In a max-heap the single largest remaining element always sits at the root (`arr[0]`). Each extraction swaps that root into the last unsorted slot (`arr[end]`) and then shrinks the active heap by one, freezing that element in place. So the largest value lands in the final position, the next-largest in the second-to-last position, and so on. The array fills from the back downward with smaller values, which read front-to-back in ascending order. A min-heap keeps the smallest element at the root instead; swapping it to the back fills the tail with ascending values, leaving the array in descending order front-to-back.

**1.4B — Where the extra time comes from during the sorting phase:**
`build_max_heap` is a one-time O(n) cost. The sorting phase then performs `n − 1` extractions, and each one does an O(1) root/end swap followed by a `max_heapify_down` call from index 0 over the active region. That sift-down walks the new root down the full height of the heap, which is O(log k) $\le$ O(log n) work per pass. Summed over the `n − 1` extractions, this repeated height-length sifting is the Θ(n log n) term. The extra log n factor is the cost of re-restoring the heap property after every extraction, not the initial build.

---

## Part 2: BST Pointer Insertion and Deletion

### 2.1 Trace — Insert `[40, 20, 60, 10, 30, 50, 70]`

| Key | Parent node | Child direction | In-order traversal afterward |
|---|---|---|---|
| 40 | None (Root) | Root | `[40]` |
| 20 | 40 | Left | `[20, 40]` |
| 60 | 40 | Right | `[20, 40, 60]` |
| 10 | 20 | Left | `[10, 20, 40, 60]` |
| 30 | 20 | Right | `[10, 20, 30, 40, 60]` |
| 50 | 60 | Left | `[10, 20, 30, 40, 50, 60]` |
| 70 | 60 | Right | `[10, 20, 30, 40, 50, 60, 70]` |

### 2.2 Trace — Delete `10`, then `20`, then `40`

Tree shape entering deletion: `40` root; left `20` (children `10`, `30`);
right `60` (children `50`, `70`).

| Target key | Deletion case | Successor key | Node spliced / replaced | In-order traversal afterward |
|---|---|---|---|---|
| 10 | 0 children (leaf) | None | 10 | `[20, 30, 40, 50, 60, 70]` |
| 20 | 1 child | None | 20 replaced by its only child 30 (30 splices up) | `[30, 40, 50, 60, 70]` |
| 40 | 2 children | 50 | 40 replaced by in-order successor 50 | `[30, 50, 60, 70]` |

**2.4A — Why the in-order successor can never have a left child:**
In a two-child deletion the successor is `y = tree_minimum(z.right)`, the minimum key of `z`'s right subtree, found by walking left from `z.right` until a node with no left child is reached. By construction `tree_minimum` stops exactly when `left` is `None`, so `y.left` is `None`. Logically, if `y` had a left child, that child would hold a smaller key and would itself be the minimum of the subtree, contradicting that `y` is the minimum. Therefore the successor has at most a right child.

**2.4B — Special pointer updates when deleting the root:**
When the deleted node `z` is the root it has no parent, so the child-pointer rewiring in `transplant` cannot go through a parent. Instead `transplant` detects `u.parent is None` and sets `tree.root` to the replacement node `v`, and it also sets `v.parent = None` so the new root has no dangling parent reference. In the two-child case the successor `y` becomes the new root: `transplant(tree, z, y)` repoints `tree.root` to `y` and sets `y.parent = None`. So two updates are essential. `tree.root` must be redirected to the replacement, and the replacement's `parent` must be cleared to `None` rather than left pointing at the removed root.

---

## Part 3: Structural Degeneration, Balance Factors, and Diagnostics

### 3.1 Trace — Search for key `7`: degenerate chain vs. balanced tree

Degenerate BST `[1, 2, 3, 4, 5, 6, 7]` (right-leaning chain) vs. balanced BST
`[4, 2, 6, 1, 3, 5, 7]`.

| Step | Degenerate: Node visited | Degenerate: Key comparison | Degenerate: Node depth | Balanced: Node visited | Balanced: Key comparison | Balanced: Node depth |
|---|---|---|---|---|---|---|
| 1 | 1 | `7 > 1` (go right) | 0 | 4 | `7 > 4` (go right) | 0 |
| 2 | 2 | `7 > 2` (go right) | 1 | 6 | `7 > 6` (go right) | 1 |
| 3 | 3 | `7 > 3` (go right) | 2 | 7 | `7 == 7` (found) | 2 |
| 4 | 4 | `7 > 4` (go right) | 3 | — | — | — |
| 5 | 5 | `7 > 5` (go right) | 4 | — | — | — |
| 6 | 6 | `7 > 6` (go right) | 5 | — | — | — |
| 7 | 7 | `7 == 7` (found) | 6 | — | — | — |

**Total comparisons — Degenerate: 7, Balanced: 3.**

### 3.2 Trace — Heights and Balance Factors

| Tree | Node key | Subtree height | Left child height | Right child height | Balance factor `BF` |
|---|---|---|---|---|---|
| 1 (LL) | 10 | 0 | -1 | -1 | 0 |
| 1 (LL) | 20 | 1 | 0 | -1 | +1 |
| 1 (LL) | 30 | 2 | 1 | -1 | +2 |
| 2 (RR) | 30 | 0 | -1 | -1 | 0 |
| 2 (RR) | 20 | 1 | -1 | 0 | -1 |
| 2 (RR) | 10 | 2 | -1 | 1 | -2 |
| 3 (LR) | 20 | 0 | -1 | -1 | 0 |
| 3 (LR) | 10 | 1 | -1 | 0 | -1 |
| 3 (LR) | 30 | 2 | 1 | -1 | +2 |
| 4 (RL) | 20 | 0 | -1 | -1 | 0 |
| 4 (RL) | 30 | 1 | 0 | -1 | +1 |
| 4 (RL) | 10 | 2 | -1 | 1 | -2 |

### 3.3 Trace — Violation Diagnostics

| Tree | Unbalanced node `z` | `BF(z)` | Child node inspected | Child `BF` | Signature | Restorative rotation call(s) |
|---|---|---|---|---|---|---|
| 1 | 30 | +2 | 20 | +1 | LL | `rotate_right(tree, 30)` |
| 2 | 10 | -2 | 20 (right child) | -1 | RR | `rotate_left(tree, 10)` |
| 3 | 30 | +2 | 10 (left child) | -1 | LR | `rotate_left(tree, 10)` then `rotate_right(tree, 30)`  (i.e. `rotate_left_right(tree, 30)`) |
| 4 | 10 | -2 | 30 (right child) | +1 | RL | `rotate_right(tree, 30)` then `rotate_left(tree, 10)`  (i.e. `rotate_right_left(tree, 10)`) |

**3.4A — Real-world patterns that build worst-case degenerate BSTs:**
Any data whose keys arrive already in sorted or reverse-sorted order. Common examples are time-series readings and pre-sorted datasets. When these are fed into the tree, every new key is larger (or smaller) than everything inserted so far, so it always attaches on the same side, producing a height-`(n − 1)` chain that behaves like linked list with O(n) search.

**3.4B — Why a single right rotation fails to balance Tree 3 (LR: 30, 10, 20):**
Tree 3 is a Left-Right zig-zag: `z = 30` is left-heavy (`BF = +2`) but its left child `10` is right-heavy (`BF = −1`), with the "middle" key `20` buried as the inner grandchild. A single `rotate_right(tree, 30)` lifts `10` to the root and sends `10`'s right subtree (the node `20`) across to become `30`'s left child, giving `10` as root with right child `30`, and `30` with left child `20` — the chain `10 → 30 → 20`. That is still height 2 with `BF(10) = −2`; the rotation merely converted the Left-Right imbalance into a Right-Left imbalance instead of removing it. A single rotation only fixes an LL (outer-heavy) shape. To fix LR you must first `rotate_left` on the left child `10` (turning LR into LL and bringing `20` up), then `rotate_right` on `30`.

---

**Told not to do Part 4**