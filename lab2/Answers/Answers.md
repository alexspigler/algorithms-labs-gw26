### Task 1.1: Trace Bubble Sort Logic

Trace Bubble Sort manually on the array: `arr = [5, 2, 9, 1, 5, 6]` ($n = 6$).

Pass 1 is filled in below as a worked example. **Fill in the remaining passes (Pass 2, Pass 3, and Pass 4)** in the table below:

| Pass | Scanning Range | Comparison ($arr[j]$ vs $arr[j+1]$) | Action | Array State | Sorted Suffix |
|---|---|---|---|---|---|
| **1 (Example)** | $j=0 \dots 4$ | $5 > 2$ | SWAP | `[2, 5, 9, 1, 5, 6]` | |
| | | $5 \le 9$ | KEEP | `[2, 5, 9, 1, 5, 6]` | |
| | | $9 > 1$ | SWAP | `[2, 5, 1, 9, 5, 6]` | |
| | | $9 > 5$ | SWAP | `[2, 5, 1, 5, 9, 6]` | |
| | | $9 > 6$ | SWAP | `[2, 5, 1, 5, 6, 9]` | `[9]` |
| **2 (TODO)** | $j=0 \dots 3$ | $arr[0]$ vs $arr[1]$: | | | |
| | | $arr[1]$ vs $arr[2]$: | | | |
| | | $arr[2]$ vs $arr[3]$: | | | |
| | | $arr[3]$ vs $arr[4]$: | | `[                      ]` | `[       ]` |
| **3 (TODO)** | $j=0 \dots 2$ | $arr[0]$ vs $arr[1]$: | | | |
| | | $arr[1]$ vs $arr[2]$: | | | |
| | | $arr[2]$ vs $arr[3]$: | | `[                      ]` | `[          ]` |
| **4 (TODO)** | $j=0 \dots 1$ | $arr[0]$ vs $arr[1]$: | | | |
| | | $arr[1]$ vs $arr[2]$: | | `[                      ]` | `[             ]` |
| **Exit** | Did any swaps occur in Pass 4? Explain early stopping: | | | `[                      ]` | **Sorted!** |

```text
Total Comparisons performed: 
Total Swaps performed: 
```
*(Tip: You can verify your trace by running `python sorting_trace.py`)*
