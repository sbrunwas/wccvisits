from dataclasses import dataclass
from typing import Dict, List, Optional

import streamlit as st


@dataclass(frozen=True)
class VaccineInfo:
    disease_name: str
    vis_url: str


@dataclass(frozen=True)
class VisitInfo:
    label: str
    vaccines: List[VaccineInfo]


VACCINES: Dict[str, VaccineInfo] = {
    "hepb": VaccineInfo(
        disease_name="Hepatitis B",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/hep-b.html",
    ),
    "rsv": VaccineInfo(
        disease_name="Respiratory Syncytial Virus (RSV)",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/rsv-immunization-infants.html",
    ),
    "dtap": VaccineInfo(
        disease_name="Diphtheria, Tetanus, and Pertussis",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/dtap.html",
    ),
    "ipv": VaccineInfo(
        disease_name="Polio",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/ipv.html",
    ),
    "hib": VaccineInfo(
        disease_name="Haemophilus influenzae type b (Hib)",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/hib.html",
    ),
    "pcv": VaccineInfo(
        disease_name="Pneumococcal Disease",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/pcv.html",
    ),
    "rv": VaccineInfo(
        disease_name="Rotavirus",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/rotavirus.html",
    ),
    "hepa": VaccineInfo(
        disease_name="Hepatitis A",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/hep-a.html",
    ),
    "mmr": VaccineInfo(
        disease_name="Measles, Mumps, and Rubella",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/mmr.html",
    ),
    "varicella": VaccineInfo(
        disease_name="Chickenpox (Varicella)",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/varicella.html",
    ),
    "hpv": VaccineInfo(
        disease_name="Human Papillomavirus (HPV)",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/hpv.html",
    ),
    "menacwy": VaccineInfo(
        disease_name="Meningococcal ACWY",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/mening.html",
    ),
    "tdap": VaccineInfo(
        disease_name="Tetanus, Diphtheria, and Pertussis (Tdap)",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/tdap.html",
    ),
    "menb": VaccineInfo(
        disease_name="Meningococcal B",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/mening-serogroup.html",
    ),
    "covid19": VaccineInfo(
        disease_name="COVID-19",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/covid-19.html",
    ),
    "flu": VaccineInfo(
        disease_name="Influenza (Flu)",
        vis_url="https://www.cdc.gov/vaccines/hcp/vis/vis-statements/flu.html",
    ),
}


VISIT_SCHEDULE: Dict[str, VisitInfo] = {
    "birth": VisitInfo(
        label="Birth (0 months)",
        vaccines=[
            VACCINES["hepb"],
            VACCINES["rsv"],
        ],
    ),
    "2_months": VisitInfo(
        label="2 months",
        vaccines=[
            VACCINES["dtap"],
            VACCINES["ipv"],
            VACCINES["hepb"],
            VACCINES["hib"],
            VACCINES["pcv"],
            VACCINES["rv"],
        ],
    ),
    "4_months": VisitInfo(
        label="4 months",
        vaccines=[
            VACCINES["dtap"],
            VACCINES["ipv"],
            VACCINES["hepb"],
            VACCINES["hib"],
            VACCINES["pcv"],
            VACCINES["rv"],
        ],
    ),
    "6_months": VisitInfo(
        label="6 months",
        vaccines=[
            VACCINES["dtap"],
            VACCINES["ipv"],
            VACCINES["hepb"],
            VACCINES["hib"],
            VACCINES["pcv"],
            VACCINES["rv"],
        ],
    ),
    "12_months": VisitInfo(
        label="12 months",
        vaccines=[
            VACCINES["hepa"],
            VACCINES["mmr"],
            VACCINES["varicella"],
            VACCINES["hib"],
            VACCINES["pcv"],
        ],
    ),
    "15_months": VisitInfo(
        label="15 months",
        vaccines=[
            VACCINES["dtap"],
        ],
    ),
    "18_months": VisitInfo(
        label="18 months",
        vaccines=[
            VACCINES["hepa"],
        ],
    ),
    "4_6_years": VisitInfo(
        label="4–6 years (48–72 months)",
        vaccines=[
            VACCINES["dtap"],
            VACCINES["ipv"],
            VACCINES["mmr"],
            VACCINES["varicella"],
        ],
    ),
    "11_12_years": VisitInfo(
        label="11–12 years (132–144 months)",
        vaccines=[
            VACCINES["hpv"],
            VACCINES["menacwy"],
            VACCINES["tdap"],
        ],
    ),
    "16_years": VisitInfo(
        label="16 years (192 months)",
        vaccines=[
            VACCINES["menacwy"],
            VACCINES["menb"],
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


def to_months(age_value: float, unit: str) -> int:
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


def render_vaccine(vaccine: VaccineInfo) -> None:
    st.markdown(
        f"""
        <div class="vaccine-card">
            <div class="vaccine-title">{vaccine.disease_name}</div>
            <a class="vaccine-link" href="{vaccine.vis_url}" target="_blank">Read CDC VIS ↗</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def inject_styles() -> None:
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at 15% 20%, rgba(246, 252, 255, 0.95) 0%, rgba(246, 252, 255, 0) 45%),
                    radial-gradient(circle at 80% 5%, rgba(255, 245, 249, 0.9) 0%, rgba(255, 245, 249, 0) 40%),
                    linear-gradient(180deg, #f7fbff 0%, #f5f9f7 100%);
                color: #243042;
            }

            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
                max-width: 850px;
            }

            .hero {
                background: rgba(255, 255, 255, 0.76);
                border: 1px solid rgba(164, 191, 215, 0.35);
                box-shadow: 0 20px 45px rgba(85, 110, 140, 0.12);
                border-radius: 24px;
                padding: 1.25rem 1.5rem;
                margin: 0.3rem 0 1.15rem 0;
                backdrop-filter: blur(6px);
            }

            .hero h1 {
                margin: 0 0 0.4rem 0;
                color: #1f3a62;
                font-weight: 700;
                letter-spacing: 0.01em;
                font-size: 1.95rem;
            }

            .hero p {
                margin: 0;
                color: #435a78;
            }

            .section-title {
                margin-top: 0.35rem;
                color: #2f4865;
                font-weight: 600;
                font-size: 1.05rem;
                letter-spacing: 0.02em;
                text-transform: uppercase;
            }

            div[data-baseweb="input"] input,
            div[data-baseweb="select"] > div {
                border-radius: 14px !important;
                border: 1px solid rgba(141, 169, 199, 0.55) !important;
                background: rgba(255, 255, 255, 0.85) !important;
            }

            .vaccine-card {
                background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
                border: 1px solid rgba(151, 178, 205, 0.45);
                border-radius: 16px;
                box-shadow: 0 10px 24px rgba(86, 112, 143, 0.08);
                padding: 0.85rem 1rem;
                margin-bottom: 0.65rem;
            }

            .vaccine-title {
                font-size: 1.03rem;
                color: #28425e;
                font-weight: 600;
                margin-bottom: 0.2rem;
            }

            .vaccine-link {
                color: #486f9f !important;
                text-decoration: none;
                font-size: 0.92rem;
                font-weight: 500;
            }

            .vaccine-link:hover {
                color: #2f5d94 !important;
                text-decoration: underline;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    inject_styles()

    st.markdown(
        """
        <section class="hero">
            <h1>Well-Child Vaccine Timing</h1>
            <p>California 2025 · Educational reference tool for routine visit guidance.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Not medical advice. Follow CDC/CDPH/AAP guidance for clinical decisions.")

    st.markdown('<div class="section-title">Choose patient age</div>', unsafe_allow_html=True)
    control_col, spacer_col = st.columns([2.2, 1.0])
    with control_col:
        input_col, unit_col = st.columns([1.1, 1.0])
        with input_col:
            age_value = st.number_input("Age", min_value=0, step=1, value=0, format="%d")
        with unit_col:
            unit = st.selectbox("Unit", options=["months", "years"])
        include_ongoing = st.checkbox("Include ongoing/seasonal vaccines", value=True)
    with spacer_col:
        st.info("Tip: try exact well-child ages for routine schedule matches.")

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
    st.markdown(
        f'<div class="section-title">Vaccines due · {visit.label}</div>',
        unsafe_allow_html=True,
    )
    for vaccine in visit.vaccines:
        render_vaccine(vaccine)

    if include_ongoing and age_months >= 6:
        st.markdown('<div class="section-title">Ongoing / seasonal</div>', unsafe_allow_html=True)
        render_vaccine(VACCINES["covid19"])
        render_vaccine(VACCINES["flu"])


if __name__ == "__main__":
    main()
