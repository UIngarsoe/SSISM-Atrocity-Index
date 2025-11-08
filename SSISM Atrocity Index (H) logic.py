# SSISM Atrocity Index (H) logic.py
# Date: 2025-11-08
# Purpose: Reproducible Python implementation of the core SSISM Atrocity Index (H) logic.
# IMPORTANT: Key operational parameters (weights, thresholds, model coefficients) are obscured
# or generalised for public release while maintaining functional integrity.

import math

# --- CORE SSISM CONSTANTS (HIDDEN/ABSTRACTED PARAMETERS) ---
# These are the operational weightings w_S, w_O, w_G, but named to abstract their true values.
WEIGHT_SET_ALPHA = 0.50  # Corresponds to w_S (Satellite Imagery Dominance)
WEIGHT_SET_BETA  = 0.25  # Corresponds to w_O (OSINT)
WEIGHT_SET_GAMMA = 0.25  # Corresponds to w_G (Ground Data)

# Core Sigmoid Transformation Parameters (Hidden)
# These are the SSISM's core beta_0 and beta_1 for the Logistic Function.
# Their actual values are protected for future operational SSISM use.
SSISM_BETA_INIT  = -3.5   # β_0 (Initial Risk Bias)
SSISM_BETA_H_MOD = 6.0    # β_1 (H-Score Impact Multiplier)

# --- 1. ATROCITY INDEX FORMULA (H) ---
def calculate_atrocity_index(s_score, o_score, g_score):
    """
    Calculates the Total Atrocity Index (H) based on the three verified components.
    H = (Alpha * S) + (Beta * O) + (Gamma * G)
    """
    H = (WEIGHT_SET_ALPHA * s_score) + \
        (WEIGHT_SET_BETA * o_score) + \
        (WEIGHT_SET_GAMMA * g_score)
    return round(H, 3)

# --- 2. SSISM ACCOUNTABILITY TRANSFORMATION ---
def ssism_accountability_likelihood(H_score):
    """
    Transforms H-Score (Z) into Accountability Likelihood (Phi_A) using Sigmoid.
    Φ_A = 1 / (1 + exp(-(β_0 + β_1*H)))
    """
    Z_score = SSISM_BETA_INIT + (SSISM_BETA_H_MOD * H_score)
    phi_A = 1 / (1 + math.exp(-Z_score))
    return round(phi_A, 3)

# --- HYPOTHETICAL EXECUTION (Myanmar Scenario) ---
# S_Final = 0.406, O_Normalized = 0.717, G_Normalized = 0.749
S_DATA_INPUT = 0.406
O_DATA_INPUT = 0.717
G_DATA_INPUT = 0.749

# 1. Calculate H
H_RESULT = calculate_atrocity_index(S_DATA_INPUT, O_DATA_INPUT, G_DATA_INPUT)
print(f"[{'S_DATA_INPUT'}]    | Normalized Imagery Score: {S_DATA_INPUT}")
print(f"[{'O_DATA_INPUT'}]    | Normalized OSINT Score: {O_DATA_INPUT}")
print(f"[{'G_DATA_INPUT'}]    | Normalized Ground Score: {G_DATA_INPUT}")
print("---")
print(f"SSISM Atrocity Index (H) = {H_RESULT}")

# 2. Calculate Accountability Likelihood (Phi_A)
PHI_A_RESULT = ssism_accountability_likelihood(H_RESULT)
print(f"SSISM Accountability Likelihood (Φ_A) = {PHI_A_RESULT}")

# 3. Check Mandatory Action Threshold (0.20)
if PHI_A_RESULT > 0.20:
    print("\n*** CRITICAL ALERT: MANDATORY VERIFICATION PROTOCOL RECOMMENDED ***")
    print(f"The Human Cost Score ({H_RESULT}) has driven Accountability Likelihood (Φ_A) above 0.20.")
else:
    print("\nALERT: Standard monitoring continues.")
