# Pharmacometrics in Drug Development

**Presenter:** Elba Raimúndez  
**Event:** Hasenauer Lab Retreat · September 2026

---

## Summary

This presentation introduces pharmacometrics (PMx) to an audience already familiar with mechanistic modelling and parameter estimation, framing the discipline as the application of those same tools to a concrete clinical question: *how does a drug behave inside a human body, and what dose is the right one?*

The talk is structured in five sections:

### 01 · What is Pharmacometrics?

Pharmacometrics integrates biology, pharmacology, physiology and pathophysiology into mathematical and statistical models to describe and quantify drug–patient interactions. It sits at the intersection of QSP, PBPK and PK/PD modelling. Every project follows the same iterative loop: **Data → Model → Insight → Decision**.

### 02 · How does PMx impact drug development?

PMx informs decisions across the full drug development pipeline — from dose selection in early clinical trials to regulatory submissions. The core value is the ability to *run the trials we cannot*: experiments that are too expensive, too slow, or ethically impossible to conduct in patients.

### 03 · A day in the life of a pharmacometrician

Overview of the routine workflow: dataset preparation and quality control, exploratory analysis, model building and evaluation (VPCs, goodness-of-fit), simulation and reporting — and the cross-functional communication with clinical and regulatory teams that ties it all together.

### 04 · Case study: Tezepelumab in severe asthma

Based on [Ly et al., *J. Clin. Pharmacol.* 2021](https://doi.org/10.1002/jcph.1803).

Tezepelumab is a human monoclonal antibody (IgG2λ) blocking TSLP, an epithelial cytokine upstream of type 2 inflammation. Phase 2b (PATHWAY) tested three doses against placebo (70, 210, 280 mg) with statistically indistinguishable asthma exacerbation rate reductions (62–71%). The case illustrates:

- Population PK modelling and exposure–response analysis for both AER and FEV₁/FeNO endpoints
- How a practically non-identifiable EC₅₀ (193% RSE, 56-fold CI) can still support a *defensible* dose selection — 210 mg Q4W sits robustly on the plateau across all parameter draws
- The selected dose (210 mg Q4W SC) was confirmed as optimal and advanced to Phase 3

**Key lessons:**
1. Treatment arm alone is not sufficient — exposure–response modelling provides the answer
2. Uncertainty in a parameter ≠ uncertainty in the decision
3. The question drives the model — and the team

### 05 · Agentic AI in Pharmacometrics

Materials from the ISoP AI/ML SIG workshop · PAGE 2026 · Dubrovnik.

PMx workflows are code-intensive (NONMEM, R, nlmixr2, mrgsolve) and tasks are repetitive but highly domain-specific. GenAI flips the bottleneck: pharmacometricians speak the domain; AI accelerates the code. Demonstrated impact areas include dataset QC, publication-ready figures, model code conversion, and automated reporting.

---

## Three take-aways

1. **Models let us run the trials we cannot** — every project follows Data → Model → Insight → Decision
2. **Uncertainty in a parameter ≠ uncertainty in the decision** — the tezepelumab EC₅₀ was unidentifiable yet 210 mg Q4W was unambiguously optimal
3. **The question drives the model — and the team** — defining the inferential target precisely is half the analysis

---

## References

- Ly et al., *J. Clin. Pharmacol.* 2021;61(7):901–912 · [DOI: 10.1002/jcph.1803](https://doi.org/10.1002/jcph.1803) · PMID: 33368307
- Emson et al., *Respir. Res.* 2020;21:265 · PMID: 33050900
- ISoP AI/ML SIG workshop materials · PAGE 2026: [github.com/AIML-SIG/2026-page-workshop-materials](https://github.com/AIML-SIG/2026-page-workshop-materials)
