# Hash Functions and Load Factor

## 1. Properties of an Effective Hash Function

An **effective hash function** is crucial for applications like data retrieval, cryptography, and checksums. The key properties include:

### **Core Properties**

1. **Determinism**
   - The same input always produces the same output
   - Essential for consistency and reliability

2. **Uniformity (Good Distribution)**
   - Hash values are uniformly distributed across the hash space
   - Minimizes clustering and collisions

3. **Efficiency**
   - Quick and computationally inexpensive to compute
   - Fast execution is critical for practical applications

4. **Avalanche Effect**
   - A small change in input (even a single bit) produces drastically different output
   - Ensures sensitivity to input variations

5. **Collision Minimization**
   - Different inputs should ideally produce different outputs
   - While collisions are inevitable, good functions minimize their likelihood

### **Cryptographic Properties** (for security-critical applications)

6. **Pre-image Resistance (Hard to Invert)**
   - Computationally infeasible to reconstruct input from hash output

7. **Second Pre-image Resistance**
   - Difficult to find different input producing the same hash

8. **Collision Resistance**
   - Hard to find any two different inputs hashing to the same value

---

## 2. Load Factor (α)

### **Definition**

The **load factor** is the ratio of stored elements to available buckets:

```
Load Factor (α) = n / m
```

Where:
- **n** = number of elements stored
- **m** = number of buckets/slots available

**Example:** 200 elements in 500 buckets = α = 0.4

### **Importance**

| Aspect | Impact |
|--------|--------|
| **Performance Indicator** | Reflects how efficiently the hash table uses space and affects operation speed |
| **Collision Rate** | Higher α = more collisions = slower operations (O(n) worst case) |
| **Resize Trigger** | When α exceeds threshold (typically 0.7–0.75), table is rehashed to maintain efficiency |
| **Memory vs. Speed Trade-off** | Low α = more memory, fewer collisions; High α = conserves memory, more collisions |

### **Practical Implications**

- **α < 0.5**: Good performance, more memory usage
- **α ≈ 0.7–0.75**: Sweet spot for most implementations (Java HashMap, Python dict)
- **α > 1.0**: More collisions likely, degraded performance, requires careful collision handling

Maintaining an optimal load factor ensures the hash table operates efficiently with minimal collisions and balanced memory usage.
