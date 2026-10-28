# task2_variables.py
# LGPD Compliance Checker — Variables & Types Practice
# 1. STRING — text data (policy name, article text)
policy_name = "Privacy Policy v2.1"
article_text = "Art. 7 - O tratamento de dados pessoais somente poder ser realizado..."
# TODO: Create a variable `company_name` with value "TechCorp Ltda"

company_name = "TechCorp Ltda"

# TODO: Create a variable `policy_version` with value "3.0"

policy_version = "3.0"

# 2. INTEGER — whole numbers (article number, page count, clause count)
article_number = 7
page_count = 12
# TODO: Create `clause_count` = 45

clause_count = 45

# TODO: Create `required_articles` = 15

required_articles = 15

# 3. FLOAT — decimals (compliance score, version numbers)
compliance_score = 0.87
lgpd_version = 13.709
# TODO: Create `risk_score` = 0.34

risk_score = 0.34

# TODO: Create `threshold` = 0.75

threshold = 0.75

# 4. BOOLEAN — True/False (is_compliant, has_consent, is_sensitive_data)
is_compliant = True
has_consent = False
# TODO: Create `is_sensitive_data` = True

is_sensitive_data = True

# TODO: Create `needs_dpo` = False

needs_dpo = False

# 5. TYPE CHECKING — run and observe output
print("=== Type Checks ===\n")
print(f"policy_name: {type(policy_name)} = {policy_name}")
print(f"article_number: {type(article_number)} = {article_number}")
print(f"compliance_score: {type(compliance_score)} = {compliance_score}")
print(f"is_compliant: {type(is_compliant)} = {is_compliant}\n")
# TODO: Add print statements for your 4 new variables
# 6. TYPE CONVERSION

print(" ==== My own Variables Types ====\n")
print(f"company_name: {type(company_name)} = {company_name} & policy_version: {type(policy_version)} = {policy_version}")
print(f"clause_count: {type(clause_count)} = {clause_count} & required_articles: {type(required_articles)} = {required_articles}")
print(f"risk_score: {type(risk_score)} = {risk_score} & threshold: {type(threshold)} = {threshold}")
print(f"is_sensitive_data: {type(is_sensitive_data)} = {is_sensitive_data} & need_dpo: {type(needs_dpo)} = {needs_dpo}\n")

# TODO: Convert `article_number` to string, save as `article_str`

article_str = str(article_number)
print(f" === Types Conversions ===\n")
print(f"article_str: {type(article_str)} = {article_str}")

# TODO: Convert `compliance_score` to int (what happens?), save as `score_int`

score_int = int(compliance_score)
print(f"score_int: {type(score_int)} = {score_int}")

# TODO: Convert `threshold` to string, save as `threshold_str`

threshold_str = str(threshold)
print(f"threshold_str: {type(threshold_str)} = {threshold_str}\n")

print(f" ==== F-Strings ====\n")


# 7. F-STRINGS (formatted output)
# TODO: Print: "Policy: {policy_name}, Version: {policy_version}, Articles: {required_articles}"

print(f"Policy: {policy_name}, Version: {policy_version}, Articles: {required_articles}")

# TODO: Print: "Compliance: {compliance_score:.2%} (threshold: {threshold:.0%})"

print(f"Compliance: {compliance_score:.2%} (threshold: {threshold:.0%})")

# 8. USER INPUT (simulated — we'll use real input later)
# TODO: Simulate reading policy name from input:
user_input = input("Enter policy name: ")
# For now, just assign:
#user_policy = "User Privacy Policy"
# TODO: Print confirmation using f-string

print(f"You entered: {user_input}")