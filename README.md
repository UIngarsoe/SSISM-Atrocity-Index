⚖️ SSISM Atrocity Index (H) for Accountability

This repository contains the foundational code and documentation for the SSISM Atrocity Index (H), a mathematical framework designed to quantify the Human Cost of Veto (HCV) or political inaction in humanitarian crises. This model translates verifiable crisis data into a single, actionable score to support accountability and transparency.

Inspired by the philosophical defence system of the SSISM V Smart Advisor, the Index transforms the total risk score (H) into an Accountability Likelihood (Φ_A) using Logistic Regression, providing an objective trigger for mandatory verification protocols.

 📁 Repository Contents

 `SSISM_Atrocity_Index_Formula_Article.py`: Contains the complete mathematical equations and detailed academic description of the Index components and weights.
 `SSISM_Github_Post.py`: The operational Python file used for execution and testing, demonstrating the Index calculation with a hypothetical crisis scenario.

---

 🧠 The Core Formula

The Atrocity Index ($\mathbf{H}$) is a Weighted Composite Score that aggregates three independently verified data streams:

$$\mathbf{H} = (w_S \cdot S_{Final}) + (w_O \cdot O_{Normalized}) + (w_G \cdot G_{Normalized})$$

| Component | Description | Recommended Weight |
| $\mathbf{S}_{Final}$ | Satellite Imagery Score: Physical evidence (destroyed infrastructure, mass grave sites, refugee camps, and population movement/urgency). | 0.50 |
| $\mathbf{O}_{Normalised}$ | Verified OSINT Score: Cross-checked reports from trusted sources (NGOs, verified journalists) weighted by Confidence. | 0.25 |
| $\mathbf{G}_{Normalised}$ | Official Ground Data: Standardised metrics from UN agencies (UNHCR, IOM), WHO, and FEWS NET (Famine Level, Displacement Count). | 0.25 |

The resulting $\mathbf{H}$ score feeds into the SSISM Logistic Regression model to calculate the Accountability Likelihood ($\mathbf{\Phi}_A$) (see the Article file for the full equation).

---

 📜 License and Usage (CRITICAL)

 Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

This project is released under the CC BY-NC-SA 4.0 license.

 You are Free to: Share, adapt, and build upon the material.
 You MUST: Give appropriate credit (Attribution) and share any adaptations under the identical license (ShareAlike).
 You MAY NOT: Use this material for Commercial Purposes (NonCommercial).

This license explicitly permits use by NGOs, UN agencies, Universities, and Educational Institutions for non-commercial research, education, and humanitarian purposes.

Please review the full legal code before use.

---
