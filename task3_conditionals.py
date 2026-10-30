# task3_conditionals.py
# LGPD Compliance Checker — Conditionals Practice
# Sample data (simulating extracted policy info)
policy_name = "TechCorp Privacy Policy"
article_7_present = True
article_8_present = False
article_18_present = True
clause_count = 42
compliance_score = 0.73
threshold = 0.75
has_dpo = False
processes_sensitive_data = True
# 1. BASIC IF
# TODO: If article_7_present is True, print "Art. 7 (legal basis) found"

if article_7_present is True:
    print("Art 7 (legal basis) found")
else:
    print("Art. 7 MISSING - critical gap")


# TODO: Else print "Art. 7 MISSING — critical gap"
# 2. IF / ELSE
# TODO: If compliance_score >= threshold, print "PASS: Score {compliance_score:.0%} meets threshold {threshold:.0%}"
# TODO: Else print "FAIL: Score {compliance_score:.0%} below threshold {threshold:.0%}"
# 3. IF / ELIF / ELSE (multiple conditions)
# TODO: Check clause_count:
#   - >= 50: print "Comprehensive policy ({clause_count} clauses)"
#   - >= 20: print "Moderate policy ({clause_count} clauses)"
#   - else: print "Sparse policy ({clause_count} clauses) — may miss details"
# 4. LOGICAL OPERATORS (and, or, not)
# TODO: If processes_sensitive_data AND not has_dpo:
#   print "WARNING: Sensitive data processed but no DPO appointed (Art. 41)"
# TODO: If article_7_present OR article_8_present OR article_18_present:
#   print "At least one key article present"
# TODO: If not article_8_present:
#   print "Art. 8 (consent) missing — verify consent mechanisms"
# 5. NESTED CONDITIONALS
# TODO: If compliance_score >= threshold:
#       If has_dpo:
#           print "FULL COMPLIANCE"
#       Else:
#           print "COMPLIANT but missing DPO"
#     Else:
#       print "NON-COMPLIANT"
# 6. TERNARY EXPRESSION (one-liner)
# TODO: status = "COMPLIANT" if compliance_score >= threshold else "NON-COMPLIANT"
# TODO: print(f"Status: {status}")
# 7. PRACTICAL: Article checker function
# TODO: Write a function check_article(article_num: int, present: bool) -> str
#   Returns "Art. {n} OK" if present else "Art. {n} MISSING"
# TODO: Call it for articles 7, 8, 18 and print results