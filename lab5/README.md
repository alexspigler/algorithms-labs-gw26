---
layout: default
title: Lab 5
nav_order: 6
---

# CSCI 3212 Lab 5: AVL Tree Deletion and Rebalancing

In this lab, you will extend your AVL tree implementation from Lab 4 by implementing
deletion with post-deletion rebalancing. You will trace and implement AVL deletion,
analyze why deletions require more complex rebalancing than insertions, and
empirically compare insertion and deletion cost.

This lab reuses the pointer-based linked AVL trees and rotation infrastructure
from Lab 4. Deletion follows the same three BST deletion cases (0, 1, 2 children),
then rebalances every ancestor of the deleted node on the way up toward the root.
Unlike insertion, a single deletion can trigger **multiple independent rotations**
at different ancestors.

## Files and deliverables

| File | Your work |
|---|---|
| `README.md` | Complete the trace tables and written responses in your lab notes or a copy of this file |
| `avl_practice.py` | Implement `avl_delete` and complete the rebalancing loop; rotation functions from Lab 4 are provided |
| `lab_checks.py` | Provided checks and profiling demonstration; do not edit |

- [ ] Part 1: AVL deletion strategy, rebalancing pass conceptual understanding
- [ ] Part 2: Deletion traces (single rotation, double rotation, multiple rotations)
- [ ] Part 3: Implement `avl_delete` with post-deletion rebalancing
- [ ] Part 4: Analyze and compare insertion vs. deletion cost
- [ ] Run the practice file and resolve all failed checks.

Keep the function names and parameters unchanged. The provided checks inspect
pointer identities, in-order traversals, parent references, node heights, and
balance factors directly.

---

## Part 1: AVL Deletion Strategy

### Why deletion is harder than insertion

In Lab 4, AVL insertion was structured as: **insert → walk ancestors up → fix at most one violation**.
A single insertion creates a single "problem zone" (the inserted key's ancestors),
and one rotation fixes the entire subtree.

AVL deletion is fundamentally different:

1. **Multiple violation zones:** Deleting a node can cause imbalances at multiple
   ancestors simultaneously.
2. **Cascading rebalancing:** After fixing an imbalance at ancestor $z$ with a rotation,
   the rotated subtree may have a different height than before. This can cause a new
   imbalance higher up.
3. **Propagate further:** Unlike insertion (which stops after one rotation), deletion
   must check every ancestor all the way to the root. After each rotation, the
   rebalancing loop continues.

**Key insight:** An insertion at height $h$ changes the subtree's height by at most 1
locally, stopping rebalancing immediately. A deletion can propagate height changes
all the way to the root.

### Post-deletion rebalancing strategy

```text
AVL-DELETE(T, key)
  z = BST-DELETE(T, key)          // Perform BST deletion; z is the deleted node (or None)
  current = parent_of_deleted     // Start rebalancing from the parent of the deleted node
  while current != None
    UPDATE-HEIGHT(current)        // Recompute height after structural change
    bf = BALANCE-FACTOR(current)
    if |bf| >= 2                  // Imbalance detected
      // Determine which case (LL, RR, LR, RL) and rotate
      // Unlike insertion, the key is NOT available—use bf signs instead
      if bf > 1                   // Left-heavy
        if BALANCE-FACTOR(current.left) >= 0
          ROTATE-RIGHT(T, current)          // LL
          current = current.parent          // Move up after rotation
        else
          ROTATE-LEFT-RIGHT(T, current)     // LR
          current = current.parent          // Move up after rotation
      else if bf < -1             // Right-heavy
        if BALANCE-FACTOR(current.right) <= 0
          ROTATE-LEFT(T, current)           // RR
          current = current.parent          // Move up after rotation
        else
          ROTATE-RIGHT-LEFT(T, current)     // RL
          current = current.parent          // Move up after rotation
    current = current.parent      // Continue to next ancestor
  return z
```

**Critical difference from insertion:** After a rotation in insertion, the rebalancing
stops immediately. In deletion, we must continue up the tree. The rotated subtree may
have a different height, creating imbalances higher up.

### 1.1 Short answer: BST deletion reminder

**TODO 1.1:** Briefly recall the three deletion cases from Lab 3/4:
- What happens when the target node has 0 children?
- What happens when the target node has 1 child?
- What happens when the target node has 2 children, and why is the in-order successor used?

- 0 children: Disconnect the leaf from its parent. If it is the root, the tree becomes empty.
- 1 child: Replace the node with its child and update the child's parent pointer. If the node is the root, its child becomes the root.
- 2 children: Replace the node with its in-order successor, the smallest node in its right subtree. If the successor is farther down, replace it with its right child first. The successor preserves BST order because it is the smallest key greater than the deleted key.

### 1.2 Short answer: Height change after deletion

**TODO 1.2:** When you delete a leaf node from an AVL tree:
- Does the leaf's parent's height change? By how much?
- Can the grandparent's height change?
- Can the imbalance propagate to the root?

- The parent's height either stays the same or decreases by 1, depending on the height of its other subtree.
- Yes. If the parent's subtree becomes shorter, the grandparent's height can also decrease by 1.
- Yes. Height changes and imbalances can continue up to the root, so we check each ancestor.

---

## Part 2: AVL Deletion Traces

### Example: AVL tree from Lab 4 insertions

Recall the AVL tree built by inserting `[30, 10, 20]` iteratively (from Lab 4, Part 4.2).
After all insertions, the tree is:

```
      20
     /  \
   10    30
```

All nodes are balanced: 20 has BF=0, 10 has BF=0, 30 has BF=0.

### 2.1 Trace: Single rotation after deletion

**TODO 2.1:** Delete key `10` from the tree above. Trace the rebalancing:

1. Perform BST deletion of 10 (it's a leaf). What is the tree after deletion?
2. Rebalance from the parent of the deleted node (20).
3. What is the balance factor at 20?
4. Identify the violation signature (LL, RR, LR, or RL) and the required rotation.
5. After rotation, is the tree still imbalanced? If so, continue rebalancing.
6. Draw the final tree and record the in-order traversal.

| Step | Action | Tree state | Unbalanced node | BF | Signature | Rotation | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Delete 10 | 20 root, 30 right child | - | - | - | - | Leaf deletion |
| 2 | Rebalance from 20 | 20 root, 30 right child | None | -1 at 20 | None | None | Already balanced |
| 3 | After rotation | 20 root, 30 right child; no rotation needed | None | -1 at 20, 0 at 30 | - | - | Final state |

After deleting 10, BF(20) = -1 - 0 = -1, which is still allowed. There is no violation or rotation, and 20 has no parent to check.

```text
20
  \
   30
```

In-order traversal: `[20, 30]`.

### 2.2 Trace: Double rotation after deletion

Build a new AVL tree by inserting `[20, 10, 30, 5, 15, 25, 35]` in balanced order.

The tree should look like:
```
        20
       /  \
      10   30
     / \   / \
    5  15 25 35
```

All nodes are balanced (you can verify balance factors are in {-1, 0, 1}).

**TODO 2.2:** Delete key `5` from this tree. Trace the rebalancing:

1. Perform BST deletion of 5 (it's a leaf).
2. Rebalance from the parent of the deleted node (10).
3. What is the balance factor at 10 after 5 is deleted?
4. Identify the violation and required rotation(s).
5. After the first rotation, is the tree still imbalanced at 20? Continue if needed.
6. Draw the final tree and record the in-order traversal.

| Step | Action | Current node | BF before | Signature | Rotation applied | BF after |
|---|---|---|---|---|---|---|
| 1 | Delete 5 | 10 | -1 | None | None | -1 |
| 2 | Rebalance parent | 20 | 0 | None | None | 0 |
| 3 | Continue up | (if needed) | N/A | None | None; reached root | N/A |

The BF values in the table are after deletion, before and after checking each node. BF(10) = -1 - 0 = -1, and its height stays 1. BF(20) = 1 - 1 = 0. No single or double rotation is needed.

```text
        20
       /  \
      10   30
       \   / \
       15 25 35
```

In-order traversal: `[10, 15, 20, 25, 30, 35]`.

### 2.3 Trace: Multiple rebalancing passes

Insert the keys `[40, 20, 60, 10, 30, 50, 70]` to build a complete balanced BST.

**TODO 2.3:** Delete key `20`. This is a 2-child deletion (has both 10 and 30 as children).
Trace the rebalancing:

1. Find the in-order successor of 20 (minimum of right subtree: 30).
2. Perform the transplant: replace 20 with 30.
3. Rebalance from the parent of the deleted node onward.
4. At each step, identify any violation and apply the necessary rotation.
5. Continue until no more imbalances exist.

| Step | Current node | BF | Imbalanced? | Rotation | After rotation |
|---|---|---|---|---|---|
| 1 | 60 | 0 | No | None | Unchanged; not on the rebalancing path |
| 2 | 40 (if needed) | 0 | No | None | 40 remains the root |

The successor is 30, so it replaces 20 and takes 10 as its left child. The actual rebalancing path starts at 30, then goes to 40; the supplied row for 60 is not part of that path. BF(30) = 0 - (-1) = 1, and BF(40) = 1 - 1 = 0. Neither node needs a rotation.

```text
        40
       /  \
      30   60
     /     / \
    10    50 70
```

In-order traversal: `[10, 30, 40, 50, 60, 70]`.

---

## Part 3: Implementation

Open `avl_practice.py` and implement the deletion function:

### 3.1 Implement AVL deletion

**TODO 3.1:** Complete `avl_delete(tree, key)` in `avl_practice.py`.

The skeleton is provided. Complete the rebalancing loop to:
1. Identify the parent of the deleted node to start rebalancing from.
2. Walk up from that node to the root, checking and fixing each ancestor.
3. Return the deleted node (or `None` if key not found).

Your implementation must:
- Correctly identify the rebalancing start point for all three BST deletion cases.
- Update heights and balance factors as you walk up.
- Recognize and apply the correct rotation for each violation signature (LL, RR, LR, RL).
- **Continue rebalancing at every ancestor** (unlike insertion, which stops after one rotation).

Provided helpers (already implemented):
- `transplant(tree, u, v)` - updates tree pointers
- `tree_minimum(node)` - finds minimum in subtree
- `tree_search(node, key)` - searches for key
- `balance_factor(node)` - returns BF
- `rotate_left(tree, node)`, `rotate_right(tree, node)` - single rotations
- `rotate_left_right(tree, node)`, `rotate_right_left(tree, node)` - double rotations
- `update_height(node)` - recalculates node's height

```bash
python3 avl_practice.py
```

---

## Part 4: Insertion vs. Deletion Comparison

Once deletion is working, the test suite runs a profiling experiment:
insert and delete 1000 random keys into an AVL tree,
measuring the number of rotations triggered by each operation.

### 4.1 Short answer: Why is deletion costlier?

**TODO 4.1:** Based on your implementation and understanding of the algorithm:

1. Why can a single deletion trigger multiple rotations at different ancestors,
   whereas a single insertion triggers at most one rotation?
2. What property of rotations ensures that insertion stops after one fix?
3. Does a deletion ever need to rebalance higher than the root? Explain.

1. After deletion, a rotation can leave the subtree shorter than it was before deletion, so another ancestor may become unbalanced. Insertion needs at most one rebalancing fix: one single rotation or one double rotation (two single rotations).
2. The insertion fix restores the subtree's height to what it was before insertion while preserving BST order. Higher ancestors therefore do not need another fix.
3. No. The root has no parent. After checking and fixing the root if needed, rebalancing is finished.

### 4.2 Short answer: Real-world implications

**TODO 4.2:** Consider a scenario where an application frequently insertions and deletions
in an AVL tree (e.g., a priority queue or cache).

1. Based on the rotation cost, would you expect insertions or deletions to be slower?
2. If deletions become a bottleneck, what alternative data structure (from this course)
   might handle deletions more efficiently?

1. Deletion has the larger worst-case rotation cost, so it can be slower. Both insertion and deletion still take O(log n) worst-case time; deletion is not necessarily slower on every input.
2. For a priority queue, a binary heap may work better. Removing the minimum or maximum takes O(log n) time by replacing the root with the last element and sifting down, without AVL rotations. This fits removing the top-priority item; finding an arbitrary key in a heap can take O(n).

---

## Final check

Run the practice file from within the `lab5/` directory:

```bash
python3 avl_practice.py
```

- Any unfinished function reports `[TODO]`.
- Any logic error or failed assertion reports `[FAIL]`.
- Any fully working function reports `[PASS]`.

The practice file exits with a nonzero exit code if any check is unfinished or
failing. When all checks pass, the command returns exit code `0`.

The profiling output compares insertion vs. deletion rotation counts on random keys
and provides empirical evidence of why deletion is costlier.
