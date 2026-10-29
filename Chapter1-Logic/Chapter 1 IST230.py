def execute_with_sample_inputs():
    """Runs explicit test cases with custom parameters."""
    print("\n========================================================")
    print("       RUNNING INDIVIDUAL SAMPLE INPUT TESTS")
    print("========================================================")
   
    # Test Case 1: Evaluating standard values
    p1, q1 = True, False
    print(f"Sample Input Set 1: p = {p1}, q = {q1}")
    print(f" -> Negation(p):         {negation(p1)}")
    print(f" -> Conjunction(p ∧ q):   {conjunction(p1, q1)}")
    print(f" -> Disjunction(p ∨ q):   {disjunction(p1, q1)}")
    print(f" -> Exclusive Or(p ⊕ q):  {exclusive_or(p1, q1)}")
    print(f" -> Conditional(p → q):   {conditional(p1, q1)}   <-- (Should be False!)")
    print(f" -> Biconditional(p ↔ q): {biconditional(p1, q1)}")
    print("-" * 50)

    # Test Case 2: Checking Vacuous Truth (p is False)
    p2, q2 = False, True
    print(f"Sample Input Set 2 (Vacuous Truth Test): p = {p2}, q = {q2}")
    print(f" -> Conditional(p → q):   {conditional(p2, q2)}    <-- (Should be True!)")
    print(f" -> Biconditional(p ↔ q): {biconditional(p2, q2)}")


if __name__ == "__main__":
    print("IST 230 Lab - Chapter 1 Master Script Execution")
    execute_with_sample_inputs()

def negation(p: bool) -> bool:
    """
    returns not p
    """

def conjunction(p: bool, q: bool) -> bool:
    """
    Returns the logical conjunction of p and q (p ∧ q).
    """
    return p and q

def disjunction(p: bool, q: bool) -> bool:
    """
    Returns the logical disjunction of p and q (p ∨ q).
    """
    return p or q

def exclusive_or(p: bool, q: bool) -> bool:
    """
    Returns the exclusive OR of p and q (p ⊕ q).
    Evaluates to True if exactly one of the inputs is True.
    """
    return (p and not q) or (not p and q)

def conditional(p: bool, q: bool) -> bool:
    """
    Returns the implication p → q.
    Remember the rule from Section 1.3: This is False ONLY when 
    the hypothesis (p) is True and the conclusion (q) is False.
    """
    return not p or q
    
def biconditional(p: bool, q: bool) -> bool:
    """
    Returns the biconditional evaluation of p and q (p ↔ q).
    """
    return p == q

def run_truth_table_generator():
    """
    Loops through all 4 structural binary truth assignments 
    and displays the completed evaluations.
    """
    print(f"{'p':<6} | {'q':<6} | {'¬p':<6} | {'p ∧ q':<6} | {'p → q':<12} | {'q → p (Conv)':<13}")
    print("-" * 60)
    
    # Truth matrix combinations
    combinations = [(True, True), (True, False), (False, True), (False, False)]
    
    for p, q in combinations:
        try:
            # These will evaluate correctly once students fill in the blocks above
            not_p = negation(p)
            and_op = conjunction(p, q)
            imp_op = conditional(p, q)
            conv_op = conditional(q, p) # Converse logic
            
            print(f"{str(p):<6} | {str(q):<6} | {str(not_p):<6} | {str(and_op):<6} | {str(imp_op):<12} | {str(conv_op):<13}")
        except Exception:
            print(f"{str(p):<6} | {str(q):<6} | [Functions Not Implemented Yet]")

if __name__ == "__main__":
    print("IST 230 Lab - Chapter 1 Evaluation Matrix")
    run_truth_table_generator()