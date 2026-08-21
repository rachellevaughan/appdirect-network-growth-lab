
import base64
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ------------------------------------------------------------
# Page config
# ------------------------------------------------------------
st.set_page_config(
    page_title="Network Growth Command Center | AppDirect × PartnerStack",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
LOGO = ASSETS / "appdirect-logo.png"
BOARDROOM = ASSETS / "appdirect-boardroom.jpg"

def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()

hero_img = b64(BOARDROOM)

# ------------------------------------------------------------
# Design system
# ------------------------------------------------------------
st.markdown(
    f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

      html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
      }}
      .stApp {{
        background:
          radial-gradient(circle at 10% 0%, rgba(71, 120, 255, .10), transparent 30%),
          #f7f9fc;
        color: #10213b;
      }}
      .block-container {{
        max-width: 1240px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
      }}
      [data-testid="stSidebar"] {{
        background: #081a33;
      }}
      [data-testid="stSidebar"] * {{
        color: #f7fbff;
      }}
      [data-testid="stSidebar"] img {{
        background: white;
        border-radius: 14px;
        padding: 10px;
      }}
      .hero {{
        position: relative;
        overflow: hidden;
        min-height: 390px;
        border-radius: 26px;
        margin: 0 0 1.3rem 0;
        padding: 3.4rem 3.6rem;
        background-image:
          linear-gradient(90deg, rgba(4,15,35,.96) 0%, rgba(4,15,35,.88) 43%, rgba(4,15,35,.35) 78%, rgba(4,15,35,.20) 100%),
          url("data:image/jpeg;base64,{hero_img}");
        background-size: cover;
        background-position: center;
        box-shadow: 0 18px 50px rgba(21, 42, 78, .16);
      }}
      .eyebrow {{
        display: inline-block;
        font-size: .78rem;
        font-weight: 800;
        letter-spacing: .12em;
        text-transform: uppercase;
        color: #89b8ff;
        margin-bottom: .85rem;
      }}
      .hero h1 {{
        color: white;
        max-width: 760px;
        font-size: clamp(2.3rem, 4vw, 4.6rem);
        line-height: .98;
        letter-spacing: -.045em;
        margin: 0;
      }}
      .hero p {{
        color: #d8e6fb;
        max-width: 680px;
        font-size: 1.05rem;
        line-height: 1.65;
        margin-top: 1.2rem;
      }}
      .hero-badges {{
        display: flex;
        gap: .55rem;
        flex-wrap: wrap;
        margin-top: 1.35rem;
      }}
      .hero-badge {{
        border: 1px solid rgba(255,255,255,.20);
        background: rgba(255,255,255,.08);
        backdrop-filter: blur(8px);
        color: white;
        padding: .48rem .78rem;
        border-radius: 999px;
        font-size: .82rem;
        font-weight: 600;
      }}
      .section-kicker {{
        color: #4d73b9;
        font-size: .76rem;
        font-weight: 800;
        letter-spacing: .10em;
        text-transform: uppercase;
        margin-top: .5rem;
      }}
      .section-title {{
        font-size: 2rem;
        line-height: 1.15;
        letter-spacing: -.03em;
        font-weight: 800;
        color: #10213b;
        margin: .25rem 0 .55rem 0;
      }}
      .section-copy {{
        color: #5a6c86;
        font-size: .98rem;
        max-width: 900px;
        margin-bottom: 1.2rem;
      }}
      .metric-card {{
        background: white;
        border: 1px solid #e7edf5;
        border-radius: 18px;
        padding: 1.15rem 1.2rem;
        min-height: 142px;
        box-shadow: 0 8px 24px rgba(20,45,85,.06);
      }}
      .metric-label {{
        color: #667a97;
        font-size: .78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .06em;
      }}
      .metric-value {{
        color: #10213b;
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -.04em;
        margin-top: .35rem;
      }}
      .metric-note {{
        color: #6f829d;
        font-size: .82rem;
        margin-top: .35rem;
      }}
      .insight-card {{
        background: linear-gradient(135deg,#0c2344 0%,#143d70 100%);
        border-radius: 20px;
        padding: 1.5rem 1.5rem;
        color: white;
        min-height: 205px;
      }}
      .insight-card h3 {{
        color: white;
        font-size: 1.1rem;
        margin-top: .2rem;
      }}
      .insight-card p {{
        color: #dbe8fa;
        font-size: .91rem;
        line-height: 1.55;
      }}
      .fit-card {{
        background: white;
        border: 1px solid #e3eaf4;
        border-radius: 18px;
        padding: 1.25rem 1.25rem;
        height: 100%;
      }}
      .fit-card h4 {{
        color: #17365f;
        margin: 0 0 .45rem 0;
      }}
      .fit-card p {{
        color: #61748f;
        font-size: .9rem;
        line-height: 1.55;
      }}
      .role-chip {{
        display:inline-block;
        background:#e9f2ff;
        color:#285b9f;
        border-radius:999px;
        padding:.34rem .68rem;
        margin:.18rem .15rem .18rem 0;
        font-size:.78rem;
        font-weight:700;
      }}
      .recommendation {{
        border-left: 4px solid #3b82f6;
        background: #eef5ff;
        padding: 1rem 1.1rem;
        border-radius: 0 14px 14px 0;
        color:#16365f;
        margin: .45rem 0;
      }}
      .small-note {{
        color:#7b8ca5;
        font-size:.78rem;
      }}
      div[data-testid="stMetric"] {{
        background: white;
        border: 1px solid #e4eaf2;
        padding: 1rem;
        border-radius: 16px;
      }}
      div[data-testid="stExpander"] {{
        background: white;
        border: 1px solid #e4eaf2;
        border-radius: 14px;
      }}
      .footer {{
        border-top:1px solid #dfe7f1;
        margin-top:2.3rem;
        padding-top:1.2rem;
        color:#71839b;
        font-size:.82rem;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Synthetic network data
# ------------------------------------------------------------
np.random.seed(24)
weeks = pd.date_range("2026-01-05", periods=28, freq="W-MON")
base_activations = np.linspace(122, 181, len(weeks)) + np.random.normal(0, 10, len(weeks))
activation_rate = np.linspace(0.31, 0.39, len(weeks)) + np.random.normal(0, .014, len(weeks))
gmv = np.linspace(1.55, 2.35, len(weeks)) + np.random.normal(0, .12, len(weeks))
commission = gmv * np.linspace(.115, .124, len(weeks)) + np.random.normal(0, .012, len(weeks))

weekly = pd.DataFrame({
    "week": weeks,
    "activated_partners": np.maximum(base_activations, 85).round().astype(int),
    "activation_rate": np.clip(activation_rate, .25, .46),
    "gmv_m": np.maximum(gmv, 1.1),
    "commission_m": np.maximum(commission, .10),
})

segments = pd.DataFrame({
    "Partner segment": ["Agency", "Affiliate", "Consultancy", "Technology", "Reseller"],
    "Invited": [1840, 2410, 960, 710, 1280],
    "Activated": [702, 748, 445, 311, 511],
    "30d GMV / activated ($K)": [8.4, 3.1, 14.8, 18.5, 11.2],
    "90d retention": [.76, .61, .84, .88, .81],
    "Median days to first sale": [18, 27, 12, 10, 15],
})
segments["Activation rate"] = segments["Activated"] / segments["Invited"]

top_partnerships = pd.DataFrame({
    "Partnership": ["CloudOps Pro", "Northstar Digital", "RevScale", "Catalyst Labs", "StackBridge", "LaunchIQ", "Orbit Partners", "VectorWorks"],
    "Segment": ["Technology","Agency","Consultancy","Reseller","Technology","Affiliate","Agency","Consultancy"],
    "GMV ($K)": [612, 488, 431, 389, 335, 304, 278, 251],
    "GMV growth": [.21,.08,.28,.14,.17,-.04,.19,.11],
    "Activation health": [92, 81, 95, 85, 89, 57, 87, 84],
})

experiments = pd.DataFrame({
    "Initiative": [
        "Segmented onboarding by partner type",
        "7 day first value activation sprint",
        "High-intent vendor ↔ partner matching",
        "Reactivation campaign for dormant partners",
        "Generic onboarding email expansion",
    ],
    "Primary metric": ["Activation rate","Time to first sale","Activated GMV","Reactivation rate","Activation rate"],
    "Expected impact": ["High","High","High","Medium","Low"],
    "Confidence": ["High","Medium","Medium","Medium","Low"],
    "Decision": ["Scale","Pilot","Pilot","Test","Stop / redesign"],
})

# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------
with st.sidebar:
    st.image(str(LOGO), use_container_width=True)
    st.markdown("### Network Growth Analyst")
    st.caption("Candidate portfolio • Toronto")
    st.markdown("---")
    page = st.radio(
        "Navigate",
        [
            "Executive view",
            "Activation diagnostic",
            "Network economics",
            "Growth experiments",
            "Forecast lab",
            "Why Rachelle",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("**Built to demonstrate**")
    st.markdown(
        """
        <span class="role-chip">SQL Driven Analytics</span>
        <span class="role-chip">Marketplace Analytics</span>
        <span class="role-chip">Forecasting</span>
        <span class="role-chip">Experimentation</span>
        <span class="role-chip">Executive Storytelling</span>
        """,
        unsafe_allow_html=True,
    )
    st.caption("All metrics presented in this demonstration are based on simulated data and are intended solely for illustrative and analytical purposes.")

# ------------------------------------------------------------
# Hero
# ------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">AppDirect × PartnerStack · Candidate Portfolio</div>
      <h1>Turn network signals into growth decisions.</h1>
      <p>
        An executive ready analytical prototype showing how I would diagnose partner activation,
        identify the partnerships that matter most, test growth hypotheses, and translate network
        data into clear actions for GTM, RevOps, Marketing and Customer Success.
      </p>
      <div class="hero-badges">
        <span class="hero-badge">Two-sided marketplace thinking</span>
        <span class="hero-badge">Activation → GMV → retention</span>
        <span class="hero-badge">Decision focused analytics</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

latest = weekly.iloc[-1]
prev = weekly.iloc[-2]
gmv_growth = latest["gmv_m"] / weekly.iloc[-5]["gmv_m"] - 1
act_delta = latest["activation_rate"] - weekly.iloc[-5]["activation_rate"]

# ------------------------------------------------------------
# Pages
# ------------------------------------------------------------
if page == "Executive view":
    st.markdown('<div class="section-kicker">01 · Leadership snapshot</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">What should leadership know this week?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Start with the signal, quantify the size of the opportunity, then make the decision explicit.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    cards = [
        ("Partner activation", f"{latest['activation_rate']:.1%}", f"{act_delta:+.1%} vs. 4 weeks ago"),
        ("Activated partners", f"{latest['activated_partners']:,}", "weekly cohort"),
        ("Network GMV", f"${latest['gmv_m']:.2f}M", f"{gmv_growth:+.1%} vs. 4 weeks ago"),
        ("Commission volume", f"${latest['commission_m']:.2f}M", "illustrative weekly volume"),
    ]
    for col, (label, value, note) in zip([c1,c2,c3,c4], cards):
        with col:
            st.markdown(
                f"""<div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-note">{note}</div>
                </div>""",
                unsafe_allow_html=True,
            )

    st.write("")
    left, right = st.columns([1.55, 1])
    with left:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=weekly["week"], y=weekly["gmv_m"],
            mode="lines+markers", name="GMV ($M)",
            line=dict(width=3),
        ))
        fig.update_layout(
            title="Weekly network GMV",
            height=360,
            margin=dict(l=20,r=20,t=55,b=20),
            paper_bgcolor="white",
            plot_bgcolor="white",
            yaxis_title="$M",
            xaxis_title="",
            legend=dict(orientation="h", y=1.1),
        )
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(gridcolor="#edf1f6")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown(
            """
            <div class="insight-card">
              <div class="eyebrow">Executive point of view</div>
              <h3>Prioritize quality of activation, not activation volume alone.</h3>
              <p>
                 Technology and consultancy partners demonstrate stronger activation velocity, retention, and early GMV contribution per activated partner. These results suggest an opportunity to prioritize matching, onboarding, and customer success resources toward higher value partner cohorts, while refining activation strategies for segments demonstrating lower economic yield.
              </p>
              <p><b>Recommended Action:</b> Scale segment specific onboarding, pilot high intent partner matching, and evaluate activation success based on downstream economic contribution, not activation volume alone.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("#### Three questions I would keep in the weekly operating rhythm")
    q1, q2, q3 = st.columns(3)
    for col, title, body in [
        (q1, "Where is activation breaking?", "Separate invite volume, onboarding completion, first value milestone, and first sale, by segment and vendor cohort."),
        (q2, "Is growth economically healthy?", "Track activated GMV, commission contribution, retention and concentration, not just top of funnel partner counts."),
        (q3, "What should we do next?", "Tie each finding to an owner, test, decision threshold and explicit scale / iterate / stop recommendation."),
    ]:
        with col:
            st.markdown(f'<div class="fit-card"><h4>{title}</h4><p>{body}</p></div>', unsafe_allow_html=True)

elif page == "Activation diagnostic":
    st.markdown('<div class="section-kicker">02 · Partner activation</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Find the activation gap worth solving.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">A two-sided marketplace needs more than aggregate conversion. Segmenting activation exposes where interventions can create the most downstream GMV.</div>',
        unsafe_allow_html=True,
    )

    seg = st.multiselect("Partner segments", segments["Partner segment"].tolist(), default=segments["Partner segment"].tolist())
    view = segments[segments["Partner segment"].isin(seg)].copy()

    fig = px.bar(
        view.sort_values("Activation rate"),
        x="Activation rate",
        y="Partner segment",
        orientation="h",
        text=view.sort_values("Activation rate")["Activation rate"].map(lambda x: f"{x:.1%}"),
        hover_data=["Invited","Activated","Median days to first sale","90d retention"],
        title="Activation rate by partner segment",
    )
    fig.update_layout(height=390, margin=dict(l=20,r=20,t=55,b=20), paper_bgcolor="white", plot_bgcolor="white")
    fig.update_xaxes(tickformat=".0%", gridcolor="#edf1f6")
    fig.update_yaxes(title="")
    st.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns([1.15, 1])
    with c1:
        heat = view.set_index("Partner segment")[["Activation rate","90d retention"]]
        heat["30d GMV efficiency"] = view.set_index("Partner segment")["30d GMV / activated ($K)"] / view["30d GMV / activated ($K)"].max()
        fig2 = px.imshow(
            heat,
            text_auto=".2f",
            aspect="auto",
            labels=dict(color="Relative / rate"),
            title="Activation quality matrix",
        )
        fig2.update_layout(height=360, margin=dict(l=20,r=20,t=55,b=20))
        st.plotly_chart(fig2, use_container_width=True)

    with c2:
        st.markdown("#### Hypothesis tree")
        st.markdown(
            """
            <div class="recommendation"><b>H1 · Relevance:</b> partners activate when the vendor/program fit is obvious enough to justify near term effort.</div>
            <div class="recommendation"><b>H2 · Time-to-value:</b> a shorter path to first qualified referral or sale improves 30/90 day retention.</div>
            <div class="recommendation"><b>H3 · Enablement:</b> onboarding content should differ for agencies, affiliates, resellers and technology partners.</div>
            <div class="recommendation"><b>H4 · Incentives:</b> commission attractiveness matters, but may be less important than partner-product fit in high value segments.</div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("The point is not to defend a hypothesis, it is to disprove weak ones quickly.")

elif page == "Network economics":
    st.markdown('<div class="section-kicker">03 · Marketplace health</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Separate network growth from network fragility.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Leadership needs to know not only whether GMV is rising, but what is driving it, where concentration risk sits, and which partnerships are compounding.</div>',
        unsafe_allow_html=True,
    )

    total = top_partnerships["GMV ($K)"].sum()
    ranked = top_partnerships.sort_values("GMV ($K)", ascending=False).copy()
    ranked["Share"] = ranked["GMV ($K)"] / total
    ranked["Cumulative share"] = ranked["Share"].cumsum()

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Top 3 GMV share", f"{ranked.head(3)['GMV ($K)'].sum()/total:.1%}")
    with c2:
        st.metric("Partnerships with >15% Growth", f"{(ranked['GMV growth'] > .15).sum()} / {len(ranked)}")
    with c3:
        st.metric("Low-health top partnership", ranked.sort_values("Activation health").iloc[0]["Partnership"])

    left, right = st.columns([1.35, 1])
    with left:
        fig = px.scatter(
            ranked,
            x="Activation health", y="GMV ($K)",
            size="GMV ($K)", color="Segment",
            hover_name="Partnership",
            hover_data={"GMV growth":":.1%"},
            title="Top partnership health vs. GMV contribution",
        )
        fig.update_layout(height=430, margin=dict(l=20,r=20,t=55,b=20), paper_bgcolor="white", plot_bgcolor="white")
        fig.update_xaxes(gridcolor="#edf1f6")
        fig.update_yaxes(gridcolor="#edf1f6")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig2 = px.bar(
            ranked,
            x="Partnership",
            y="GMV ($K)",
            text_auto=".0f",
            title="GMV concentration",
        )
        fig2.update_layout(height=430, margin=dict(l=20,r=20,t=55,b=20), paper_bgcolor="white", plot_bgcolor="white")
        fig2.update_xaxes(tickangle=-35, showgrid=False)
        fig2.update_yaxes(gridcolor="#edf1f6")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown(
        """
        <div class="recommendation"><b>Leadership recommendation:</b> Strengthen high GMV partnerships exhibiting declining activation health before deploying incremental resources toward partner acquisition. Sustaining the performance of high value relationships while managing retention and concentration risk creates a stronger foundation for efficient network expansion.</div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Growth experiments":
    st.markdown('<div class="section-kicker">04 · Cross-functional growth</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Make every initiative earn the right to scale.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Growth analytics should inform initiatives from the outset by defining the hypothesis, target segment, success metrics, and decision criteria. Enabling teams to move confidently from experimentation to scale, iteration, or course correction.</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(
        experiments,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Initiative": st.column_config.TextColumn(width="large"),
            "Decision": st.column_config.TextColumn(width="medium"),
        },
    )

    exp_name = st.selectbox("Choose an initiative to pressure test", experiments["Initiative"])
    baseline = st.slider(
    "Baseline Success Rate",
    min_value=0.0,
    max_value=100.0,
    value=22.0,
    step=0.5,
    help="Illustrative baseline assumption used to evaluate the incremental impact of the selected growth initiative."
) / 100
    lift = st.slider("Required Relative Lift to Scale", 1.0, 30.0, 8.0, .5) / 100
    exposed = st.number_input("Test Population (Partners)", min_value=100, max_value=50000, value=3500, step=100)

    expected_incremental = exposed * baseline * lift
    st.markdown(
        f"""
        <div class="insight-card">
          <div class="eyebrow">Decision design</div>
          <h3>{exp_name}</h3>
          <p>At a {baseline:.1%} baseline and a {lift:.1%} minimum relative lift, the test must generate roughly
          <b>{expected_incremental:,.0f} incremental successful outcomes</b> across {exposed:,} exposed partners
          before downstream GMV / retention validation.</p>
          <p><b>Next check:</b> verify that incremental activation translates into durable 30 and 90 day GMV, rather than one time activity.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Forecast lab":
    st.markdown('<div class="section-kicker">05 · Strategic modeling</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Translate activation assumptions into an economic forecast.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">The model provides transparency into key assumptions, enabling leadership to distinguish evidence based insights from directional estimates.</div>',
        unsafe_allow_html=True,
    )

    a, b, c, d = st.columns(4)
    with a:
        monthly_invites = st.number_input("Monthly partner invites", 1000, 50000, 9000, 250)
    with b:
        act_rate = st.slider(
    "Activation rate",
    min_value=0.0,
    max_value=100.0,
    value=36.0,
    step=0.5,
    help="Illustrative assumption — adjust to explore alternative activation scenarios."
        ) / 100
    with c:
        gmv_per = st.number_input("90 day GMV / activated ($)", 1000, 50000, 11500, 500)
    with d:
        commission_rate = st.slider(
    "Illustrative commission rate",
    min_value=0.0,
    max_value=50.0,
    value=12.0,
    step=0.5,
    help="Illustrative assumption for scenario analysis; not representative of PartnerStack's actual commission structure."
        ) / 100

    horizon = np.arange(1, 13)
    activated = monthly_invites * act_rate
    ramp = np.minimum(horizon / 3, 1)
    monthly_gmv = activated * gmv_per * ramp / 3
    monthly_commission = monthly_gmv * commission_rate
    forecast = pd.DataFrame({
        "Month": horizon,
        "GMV": monthly_gmv,
        "Commission volume": monthly_commission,
    })

    m1, m2, m3 = st.columns(3)
    m1.metric("Activated partners / month", f"{activated:,.0f}")
    m2.metric("Forecasted 12 month GMV", f"${forecast['GMV'].sum()/1_000_000:,.1f}M")
    m3.metric("Forecasted 12 month Commission Volume", f"${forecast['Commission volume'].sum()/1_000_000:,.1f}M")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=forecast["Month"], y=forecast["GMV"]/1_000_000, name="GMV ($M)"))
    fig.add_trace(go.Scatter(x=forecast["Month"], y=forecast["Commission volume"]/1_000_000, name="Commission ($M)", mode="lines+markers", yaxis="y2"))
    fig.update_layout(
        title="12 Month GMV & Commission Volume Forecast",
        height=420,
        margin=dict(l=20,r=20,t=55,b=20),
        paper_bgcolor="white", plot_bgcolor="white",
        xaxis_title="Month",
        yaxis=dict(title="GMV ($M)", gridcolor="#edf1f6"),
        yaxis2=dict(title="Commission ($M)", overlaying="y", side="right", showgrid=False),
        legend=dict(orientation="h", y=1.1),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Sensitivity: what matters most?")
    sens_rates = np.array([act_rate - .05, act_rate, act_rate + .05])
    sens_rates = np.clip(sens_rates, .05, .9)
    sensitivity = pd.DataFrame({
        "Scenario": ["-5 pts activation", "Base", "+5 pts activation"],
        "Activation rate": sens_rates,
        "12 mo GMV ($M)": [
            (monthly_invites * r * gmv_per * np.minimum(horizon/3, 1) / 3).sum()/1_000_000
            for r in sens_rates
        ],
    })
    st.dataframe(
        sensitivity,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Activation rate": st.column_config.NumberColumn(format="%.1f%%"),
            "12 mo GMV ($M)": st.column_config.NumberColumn(format="$%.2f"),
        }
    )
    st.caption("Illustrative scenario analysis. A production model would leverage PartnerStack’s internal data to incorporate cohort performance, seasonality, vendor mix, and retention dynamics.")

elif page == "Why Rachelle":
    st.markdown('<div class="section-kicker">06 · Candidate fit</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">The role asks for exactly the intersection I work in.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Business judgment + hands-on analytics + cross-functional influence + executive communication. This portfolio is designed to show the work product, not just claim the skills.</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    fit_cards = [
        (
            "Analytical rigor",
            "Master of Management Analytics training plus hands on SQL, BigQuery, Python, forecasting, segmentation, experimentation and BI. Comfortable moving from raw data to a quantified point of view."
        ),
        (
            "Commercial orientation",
            "Managed analytics around ~$25M in client investment, built ROI and KPI frameworks, and translated performance signals into recommendations on where to allocate spend and management attention."
        ),
        (
            "Cross-functional influence",
            "Experience partnering with marketing, analytics, client and operational stakeholders shaping the question, defining the metric, building the readout and presenting recommendations to decision makers."
        ),
    ]
    for col, (title, body) in zip([c1,c2,c3], fit_cards):
        with col:
            st.markdown(f'<div class="fit-card"><h4>{title}</h4><p>{body}</p></div>', unsafe_allow_html=True)

    st.write("")
    st.markdown("### Role requirement → evidence I would bring")
    mapping = pd.DataFrame({
        "AppDirect / PartnerStack need": [
            "Own weekly network growth analysis",
            "SQL + BigQuery / BI",
            "Form and validate hypotheses",
            "Forecast strategic initiatives",
            "Translate analysis for leadership",
            "Connect analytics to GTM / OKRs",
            "Shape tests with Marketing / CS",
        ],
        "My evidence": [
            "Recurring KPI frameworks, performance diagnostics and executive reporting",
            "SQL / BigQuery plus Databricks, Tableau, Python and analytics engineering workflows",
            "Segmentation, predictive modeling, scenario analysis and evidence-led recommendations",
            "Forecasting, ROI modeling and scenario analysis tied to business decisions",
            "Executive storytelling that turns complexity into a clear point of view",
            "Client-facing work linking analytics to commercial objectives and resource allocation",
            "Cross-functional campaign analytics, measurement design and optimization recommendations",
        ],
        "Fit": ["Strong","Strong","Strong","Strong","Strong","Strong","Strong"],
    })
    st.dataframe(mapping, hide_index=True, use_container_width=True)

    st.markdown(
        """
        <div class="insight-card">
          <div class="eyebrow">My operating principle</div>
          <h3>Use data to make the next decision easier.</h3>
          <p>I would bring a bias toward quantified answers, visible assumptions and clear decisions:
          what changed, why it changed, how confident we are, and whether the business should scale,
          iterate, or stop.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("What I would want to learn in my first 30 days"):
        st.markdown(
            """
            - How PartnerStack defines **activated partner**, healthy partnership and network-quality thresholds today.
            - Which vendor and partner segments create the strongest **time-to-first-value → retention → GMV** flywheel.
            - Where existing reporting creates friction for GTM, RevOps, Marketing or Customer Success.
            - Which growth hypotheses leadership believes most strongly—and which are least supported by evidence.
            - What one recurring decision I can make materially faster or better by improving the analytical operating rhythm.
            """
        )

st.markdown(
    """
    <div class="footer">
      Candidate portfolio for the AppDirect / PartnerStack Network Growth Analyst role. 
      All network metrics, partner names and forecasts shown in this demo are synthetic and were created solely to demonstrate analytical approach.
    </div>
    """,
    unsafe_allow_html=True,
)
