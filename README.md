# AppDirect Network Growth Lab

### Turning partner network signals into actionable growth decisions

An interactive analytics portfolio developed to demonstrate how data can be used to evaluate **partner activation, network performance, marketplace economics, experimentation, and growth opportunities** within a B2B partner ecosystem.

The project explores how a Network Growth Analyst can move beyond reporting performance to identifying opportunities, testing hypotheses, quantifying potential impact, and translating analytical findings into clear recommendations for leadership.

> **Data Disclosure:** This demonstration uses simulated data to showcase analytical methodology, strategic thinking, and decision-making frameworks. It does not contain or represent actual AppDirect or PartnerStack performance data.

---

## Live Experience

Explore the interactive application or review the underlying methodology and source code.

**Interactive Live Demo: https://appdirect-network-growth-lab.streamlit.app/**

**View Source Code on GitHub: https://github.com/rachellevaughan/appdirect-network-growth-lab/**

---

## Preview

![AppDirect Network Growth Lab Preview](assets/app-preview.png)

*Executive view of the Network Growth Lab, designed to surface key network performance signals and translate them into actionable recommendations.*
<img width="1680" height="929" alt="Screenshot 2026-08-21 at 1 31 37 AM" src="https://github.com/user-attachments/assets/17d52d47-9280-461b-b944-070c8ea4db20" />
<img width="1680" height="929" alt="Screenshot 2026-08-21 at 1 32 33 AM" src="https://github.com/user-attachments/assets/12466650-96eb-4d8f-bc7a-e89261b8573a" />

---

## Executive Objective

The Network Growth Lab is designed around a central business question:

> **How can partner activation and marketplace performance data be translated into decisions that drive efficient, sustainable network growth?**

The application approaches this question through the relationship between:

**Partner Acquisition → Activation → Partnership Health → GMV → Commission Volume → Retention → Network Growth**

Rather than optimizing any individual metric in isolation, the analysis considers how partner quality, activation behaviour, economic contribution, and retention interact across the network.

---

## Analytical Modules

### 1. Executive View

Provides a leadership-level perspective on network performance, including partner activation, Gross Merchandise Value (GMV), commission volume, and emerging growth signals.

The objective is to move quickly from **what happened** to **what leadership should consider doing next**.

### 2. Activation Diagnostic

Examines differences in activation behaviour across partner segments to identify where activation strategies may be most effective.

The analysis considers:

* Activation rates
* Time to first value
* Early GMV contribution
* Partner retention
* Segment-level performance differences

The goal is to distinguish **activation volume from activation quality**.

### 3. Network Economics

Evaluates the economic health of the partner ecosystem by examining the relationship between partnership performance and GMV contribution.

The module considers:

* GMV concentration
* Partnership growth
* Activation health
* High-value partner performance
* Retention and concentration risk

This provides a more complete view of whether network growth is both **scalable and resilient**.

### 4. Growth Experiments

Demonstrates how analytics can inform growth initiatives before launch by establishing:

* A clear hypothesis
* Target partner segment
* Baseline outcome rate
* Required relative lift
* Test population
* Success metrics
* Decision criteria

The objective is to create a disciplined framework for determining whether an initiative should be **scaled, iterated, or discontinued**.

### 5. Forecast Lab

Translates partner-growth assumptions into an interactive economic forecast.

Users can explore how changes in variables such as:

* Monthly partner invitations
* Partner activation
* GMV per activated partner
* Illustrative commission assumptions

could influence projected network outcomes.

Key outputs include:

* Activated partners
* Projected 12 month GMV
* Projected 12 month commission volume
* Scenario sensitivity

> **Modeling Note:** This scenario analysis is illustrative. A production model would leverage PartnerStack's internal data to incorporate cohort performance, seasonality, vendor mix, retention dynamics, and other relevant network characteristics.

### 6. Candidate Fit

Connects the analytical approach demonstrated throughout the application with the capabilities required for a Network Growth Analyst, including:

* SQL driven analytics
* Marketplace analysis
* Forecasting and scenario modeling
* Hypothesis development
* Experimentation
* Cross-functional collaboration
* Executive communication
* Data-informed decision-making

---

## Analytical Philosophy

The project is built around a simple principle:

> **Use data to make the next decision easier.**

Effective network analytics should provide clarity on:

**What changed?**
**Why did it change?**
**How confident are we in the conclusion?**
**What is the potential business impact?**
**What should the organization do next?**

This approach emphasizes transparent assumptions, quantified recommendations, and a willingness to revise hypotheses when the evidence points elsewhere.

---

## Technology

The application was developed using:

* **Python** — analytical logic and data manipulation
* **Pandas** — data transformation and analysis
* **NumPy** — scenario modeling
* **Plotly** — interactive data visualization
* **Streamlit** — application interface and deployment

The analytical design is intended to demonstrate an approach that could be extended to production environments incorporating **SQL, BigQuery, Metabase, and internal marketplace data**.

---

## Running the Project Locally

Clone the repository:

```bash
git clone INSERT_GITHUB_URL_HERE
```

Navigate to the project directory:

```bash
cd appdirect-network-growth-lab
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Launch the Streamlit application:

```bash
streamlit run app.py
```

---

## Project Structure

```text
appdirect-network-growth-lab/
│
├── app.py
├── requirements.txt
├── README.md
│
└── assets/
    ├── appdirect-logo.png
    ├── appdirect-boardroom.jpg
    └── app-preview.png
```

---

## About This Project

This project was independently developed as a candidate portfolio piece for the **Network Growth Analyst opportunity with AppDirect's PartnerStack team**.

It is intended to demonstrate how I approach the intersection of **analytics, commercial strategy, experimentation, and executive decision support**.

The project is not affiliated with, endorsed by, or representative of internal analysis conducted by AppDirect or PartnerStack.

---

### Rachelle Vaughan, MMA

Master of Management Analytics
Smith School of Business, Queen's University

