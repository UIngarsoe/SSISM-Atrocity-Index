SSISM_Atrocity_Index_Formula_Article.py
Date: 2025-11-08
Author: U Ingar Soe, based on the SSISM methodology 

-------------------------------------------------------------------------------------
LICENSE NOTICE
This code and the underlying methodology (SSISM Atrocity Index) is licensed under:
CREATIVE COMMONS ATTRIBUTION-NONCOMMERCIAL-SHAREALIKE 4.0 INTERNATIONAL (CC BY-NC-SA 4.0)
This grants non-exclusive rights for use by NGOs, UN agencies, Universities, and
Educational Institutions for non-commercial research, education, and humanitarian purposes.
Commercial use or for-profit deployment is strictly prohibited without explicit written permission.
-------------------------------------------------------------------------------------

"""
THE SSISM ATROCITY INDEX (H) FOR ACCOUNTABILITY IN HUMANITARIAN CRISES

Abstract
The SSISM Atrocity Index (H) is a quantitative model designed to transform the 'invisible cost' of
geopolitical inaction (e.g., UN Security Council Vetoes) into a measurable, politically actionable
score (H). This model is a Weighted Composite Score that acts as the Total Risk Score (Z) input
for a Logistic Regression-based Accountability System, similar to the SSISM V Smart Advisor.

I. The Atrocity Index (H) - Weighted Composite Score

The total Human Cost Score (H) is the sum of three independently validated and normalized components:
Satellite Imagery (S), Verified Open-Source Intelligence (O), and Official Ground Data (G).

Equation 1: Total Atrocity Index (H)
H = (w_S * S_Final) + (w_O * O_Normalized) + (w_G * G_Normalized)
Where:
w_S + w_O + w_G = 1.0 (Total Weight)

Current Recommended Weights based on Verifiability:
W_S = 0.50  # Satellite Imagery (Highest Verifiability/Independence)
W_O = 0.25  # Verified OSINT (Human Context + Confidence Scoring)
W_G = 0.25  # Ground Data (Official Scale/Scope)

II. Component: Satellite Imagery Score (S_Final)

The S_Final Score is the primary driver, focused on catastrophic events and mass movement. It is
calculated from a preliminary weighted sum (S) amplified by a time-sensitive Urgency Multiplier (U_Sat).

Equation 2a: Preliminary Imagery Score (S)
S = Sum(W_Severity_i * C_Normalized_i)
Where C_Normalized_i = Detected Count / Max Critical Count for indicator 'i'.

Core Severity Weights (W_Severity_i):
W_Grave   = 0.40  # New Grave Sites (Mass Casualty)
W_Tents   = 0.35  # New Refugee Tents/Camps (Mass Displacement)
W_Hosp    = 0.15  # Hospitals Destroyed (Critical Infrastructure Loss)
W_Sch     = 0.10  # Schools Destroyed (Future Loss)
(Sum of W_Severity_i = 1.0)

Equation 2b: Final Imagery Score (S_Final)
S_Final = S * U_Sat
Where U_Sat (Urgency Multiplier) > 1.0 for rapid population movement (Night-Light Data Anomaly).

III. Component: SSISM Accountability Transformation (For Action)
The derived Atrocity Index (H) is transformed into an **Accountability Likelihood (Φ_A)** using a
Logistic Regression Sigmoid function, mirroring the SSISM V Smart Advisor's core mechanism.

Equation 3: Accountability Likelihood (Sigmoid Function)
Φ_A = 1 / (1 + exp(-Z))
Where Z = Total Risk Score, and in this application, Z is a function of H:
Z = β_0 + (β_1 * H)

SSISM PRINCIPLE: H is the Z (Total Risk Score) for Accountability.
# Φ_A < 0.2 is the recommended trigger for a 'Mandatory Verification Protocol'
# (e.g., a formal, immediate UN General Assembly resolution or a public R2P declaration).
"""

import math

def calculate_h_score(s_final, o_normalized, g_normalized):
    """Calculates the Atrocity Index (H) based on weighted components."""
    W_S, W_O, W_G = 0.50, 0.25, 0.25
    H = (W_S * s_final) + (W_O * o_normalized) + (W_G * g_normalized)
    return round(H, 3)

--- Hypothetical Scenario Test ---
H_TEST = calculate_h_score(s_final=0.406, o_normalized=0.717, g_normalized=0.749)
print(f"Test H Score (Myanmar Scenario): {H_TEST}") # Should be 0.569

def ssism_accountability_transformation(H_score, beta_0=-3.5, beta_1=6.0):
    """
    Transforms the H-Score (Total Risk Score Z) into an Accountability Likelihood (Phi_A)
    using the Logistic Regression Sigmoid function.
    NOTE: beta_0 and beta_1 are core SSISM parameters; these values are illustrative for this academic release.
    """
    Z = beta_0 + (beta_1 * H_score)
    Phi_A = 1 / (1 + math.exp(-Z))
    return round(Phi_A, 3)

--- Accountability Likelihood Calculation ---
PHI_A_TEST = ssism_accountability_transformation(H_TEST)
print(f"Accountability Likelihood (Φ_A): {PHI_A_TEST}")

# H_TEST = 0.569 --> Z = -3.5 + (6.0 * 0.569) = -3.5 + 3.414 = -0.086
# Phi_A = 1 / (1 + exp(0.086)) = 1 / (1 + 1.0898) = 0.4786

if PHI_A_TEST < 0.200:
    print("\nACTION: Accountability Likelihood is LOW. Mandatory Verification Protocol is NOT triggered.")
else:
    print(f"\nACTION: Accountability Likelihood (Φ_A={PHI_A_TEST}) is HIGH.")
    print("This crosses the 0.2 threshold, indicating a STRONG requirement for immediate, public, and mandatory verification/action protocol.")
