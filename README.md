# HEP Analyzer Results

Repository of analysis outputs produced with the [**hep_analyzer**](https://github.com/missionnowin/hep_analyzer) framework – an analyzer for **OSCAR**, **HepMC** and **phsd.dat** event formats.

---

## Purpose

The goal of this repository is to:

- Keep **versioned, reproducible analysis results** separate from the analysis code.
- Preserve enough **configuration and metadata** so that any result can be re‑generated with `hep_analyzer`.

Typical contents include:

- Final plots (PNG/PDF/SVG) of kinematic spectra, angular distributions, multiplicities, etc.
- Numerical tables (CSV/TXT/Markdown) for use in LaTeX or external tools.
- Intermediate processed data (ROOT, NPZ, CSV…) produced by `hep_analyzer` pipelines.
- Configuration snapshots and logs describing how each set of results was obtained.

---

## Repository structure

The exact structure may evolve over time, but the intended layout is:

- **`studies/`**  
  Physics analyses grouped by **system / energy / purpose**. Each study is self‑contained.
  
  Examples (for illustration):
  - `studies/auau_3gev_urqmd/`
  - `studies/auau_11gev_phqmd/`
  - `studies/pp_7tev_reference/`
  - `studies/method_cumulative_effects/`

- **`common/`**  
  Shared colormaps, style files, small utilities or reference data that multiple studies use (optional).

Within each `studies/<study_name>/` directory, the recommended layout is:

- **`config/`** – configs used by `hep_analyzer` for this study (YAML/JSON/TOML, etc.).
- **`data/`** – intermediate processed data (binned histograms, reduced ntuples, cached selections).
- **`plots/`** – publication‑ready figures (PNG, PDF, SVG).
- **`tables/`** – numerical tables for key observables (CSV/TXT/MD).
- **`logs/`** – run logs, environment dumps, checksums, anything useful for reproducibility.
- **`notes/`** – short markdown notes, TODOs, caveats, per‑study README.

Not all subdirectories must exist for every study; only those that are relevant are created.

---

## Naming conventions

To make results self‑describing and script‑friendly:

- **Study directories** encode the system, energy and (optionally) generator/model, for example:
  - `auau_3gev_urqmd/`
  - `auau_11gev_phqmd/`
  - `pp_7tev_reference/`

- **Configuration files** describe what they do:
  - `config/auau_3gev_urqmd_central.yaml`
  - `config/auau_3gev_urqmd_minbias.yaml`
  - `config/pp_7tev_baseline.yaml`

- **Plots** encode observable, particle species, and selection:
  - `plots/theta_protons_centrality_0_5.png`
  - `plots/pt_pions_0_5_rapidity_0_1.pdf`

- **Tables** mirror what appears in figures:
  - `tables/multiplicity_vs_centrality_protons.csv`
  - `tables/mean_pt_vs_nch_pions.txt`

These conventions are guidelines rather than strict rules, but consistent naming makes it much easier to:

- Locate a given observable.
- Compare runs with different generators/settings.
- Reuse the same results in multiple documents.

---

## How to use this repository
### Browsing analyses

For each study under `studies/`:

1. Start with `README.md` or `notes/overview.md` if present – it should describe:
   - What is being studied.
   - Generators/data sources and main selections.
   - Which plots/tables correspond to which physics questions.

2. Look into `plots/` for the main figures used in documents.

3. Use `tables/` for importing numerical results into LaTeX or other analysis tools.

4. Inspect `config/` to see exactly how `hep_analyzer` was configured.

5. Check `logs/` (and any environment files) for:
   - `hep_analyzer` version / commit.
   - Generator versions.
   - Command lines, seeds, and environment details.

---

## Related repositories

- **Main analysis code:**  
  [missionnowin/hep_analyzer](https://github.com/missionnowin/hep_analyzer)  
  Analyzer for OSCAR, HepMC and `phsd.dat` formats. Use this to generate the results stored here.

Additional analysis or generator repositories can be linked from individual study notes as needed.

---

## Contact & Support

For questions about specific analyses, reproducibility issues, or missing information, please open an issue in this repository or the main [hep_analyzer](https://github.com/missionnowin/hep_analyzer) repository.
