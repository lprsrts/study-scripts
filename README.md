# Academic Study Scripts

Computational scripts and visualizations for physics, mathematics, and statistics coursework.

## Structure

```
.
├── physics/
│   └── electromagnetism/
├── mathematics/
│   └── calculus/
├── statistics/
├── output_images/
└── templates/
```

## Contents

### Physics
- **physics/electromagnetism/CurlIdentityOfElectricField.py** - Vector field curl identities
- **physics/electromagnetism/GaussianSmoothedChargeDist.py** - Charge distribution with gradient fields

### Statistics
- **statistics/ZentralerGrenzwert.py** - Central Limit Theorem demonstration

## Usage

```bash
pip install -r requirements.txt
python physics/electromagnetism/CurlIdentityOfElectricField.py
```

Output saved to `output_images/`.

## Adding Scripts

Organize by subject and topic:
- Physics: `physics/mechanics/`, `physics/quantum/`
- Mathematics: `mathematics/linear_algebra/`, `mathematics/differential_equations/`
- Statistics: `statistics/` or create subdirectories

Use PascalCase: `HarmonicOscillator.py`, `FourierSeries.py`

Template available at `templates/script_template.py`.
