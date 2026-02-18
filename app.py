from dataclasses import dataclass
from typing import Dict, List, Optional

import streamlit as st


@dataclass(frozen=True)
class VisitInfo:
    label: str
    vaccines: List[str]


VISIT_SCHEDULE: Dict[str, VisitInfo] = {
    "birth": VisitInfo(
        label="Birth (0 months)",
        vaccines=[
            "HepB",
            "RSV (0–8 months eligibility dependent)",
        ],
    ),
    "2_months": VisitInfo(
        label="2 months",
        vaccines=[
            "DTaP",
            "Polio (IPV)",
            "HepB",
            "Hib",
            "PCV",
            "RV (Rotavirus)",
        ],
    ),
    "4_months": VisitInfo(
        label="4 months",
        vaccines=[
            "DTaP",
            "Polio (IPV)",
            "HepB (if 1st dose given at 2 months)",
            "Hib",
            "PCV",
            "RV",
        ],
    ),
    "6_months": VisitInfo(
        label="6 months",
        vaccines=[
            "DTaP",
            "Polio (IPV) (age 6–18 months)",
            "HepB (age 6–18 months; final dose rules)",
            "Hib",
            "PCV",
            "RV (if RotaTeq used / 3-dose series)",
        ],
    ),
    "12_months": VisitInfo(
        label="12 months",
        vaccines=[
            "HepA (start age 12–23 months)",
            "MMR (12–15 months)",
            "Var (Varicella) (12–15 months)",
            "Hib (12–15 months)",
            "PCV (12–15 months)",
        ],
    ),
    "15_months": VisitInfo(
        label="15 months",
        vaccines=[
            "DTaP (15–18 months)",
        ],
    ),
    "18_months": VisitInfo(
        label="18 months",
        vaccines=[
            "HepA (2nd dose 6–18 months after 1st)",
        ],
    ),
    "4_6_years": VisitInfo(
        label="4–6 years (48–72 months)",
        vaccines=[
            "DTaP",
            "Polio (IPV)",
            "MMR",
            "Varicella",
        ],
    ),
    "11_12_years": VisitInfo(
        label="11–12 years (132–144 months)",
        vaccines=[
            "HPV (2 doses; can start at age 9)",
            "MenACWY (MCV4)",
            "Tdap",
        ],
    ),
    "16_years": VisitInfo(
        label="16 years (192 months)",
        vaccines=[
            "MenACWY (MCV4) booster",
            "MenB (optional/indication/shared decision)",
        ],
    ),
}

COMMON_AGES = [
    "Birth",
    "2 months",
    "4 months",
    "6 months",
    "12 months",
    "15 months",
    "18 months",
    "4–6 years",
    "11–12 years",
    "16 years",
]


def to_months(age_value: int, unit: str) -> int:
    if unit == "years":
        return int(round(age_value * 12))
    return int(round(age_value))


def get_visit_key(age_months: int) -> Optional[str]:
    if age_months == 0:
        return "birth"
    if age_months == 2:
        return "2_months"
    if age_months == 4:
        return "4_months"
    if age_months == 6:
        return "6_months"
    if age_months == 12:
        return "12_months"
    if age_months == 15:
        return "15_months"
    if age_months == 18:
        return "18_months"
    if 48 <= age_months <= 72:
        return "4_6_years"
    if 132 <= age_months <= 144:
        return "11_12_years"
    if age_months == 192:
        return "16_years"
    return None


def main() -> None:
    st.title("Well-Child Vaccine Timing (CA 2025)")
    st.caption(
        "Prototype for educational use only. Not medical advice. "
        "Follow CDC/CDPH/AAP guidance for actual clinical decisions."
    )

    age_value = st.number_input("Age", min_value=0, step=1, value=0, format="%d")
    unit = st.selectbox("Unit", options=["months", "years"])
    include_ongoing = st.checkbox("Include ongoing/seasonal vaccines", value=True)

    age_months = to_months(age_value, unit)
    visit_key = get_visit_key(age_months)

    if visit_key is None:
        st.warning(
            "No exact routine-visit match for this age. Common well-child ages: "
            + ", ".join(COMMON_AGES)
            + "."
        )
        return

    visit = VISIT_SCHEDULE[visit_key]
    st.subheader(f"Vaccines due at this visit: {visit.label}")
    for vaccine in visit.vaccines:
        st.markdown(f"- {vaccine}")

    if include_ongoing and age_months >= 6:
        st.markdown("- COVID-19 vaccine(s)")
        st.markdown("- Flu vaccine every fall")


if __name__ == "__main__":
    main()
