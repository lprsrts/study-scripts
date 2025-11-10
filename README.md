# Academic Study Scripts

A comprehensive collection of computational scripts and visualizations developed throughout my academic career. This repository serves as a living documentation of coursework, research, and self-study in physics, mathematics, statistics, and related fields.

## 📚 Repository Structure

```
.
├── physics/
│   └── electromagnetism/       # EM field theory, Maxwell's equations
├── mathematics/
│   └── calculus/               # Vector calculus, differential equations
├── statistics/                 # Probability theory, statistical methods
├── output_images/              # Generated plots and visualizations
└── templates/                  # Template files for new scripts
```

## 📖 Current Contents

### Physics
#### Electromagnetism
- **CurlIdentityOfElectricField.py** - Visualization of vector field identities (curl E, curl curl E) using analytical solutions
- **GaussianSmoothedChargeDist.py** - Charge distribution modeling with Gaussian smoothing and gradient field visualization

### Statistics
- **ZentralerGrenzwert.py** - Central Limit Theorem demonstration with multiple probability distributions

## 🚀 Quick Start

### Prerequisites
```bash
pip install numpy matplotlib scipy
```

### Running Scripts
Navigate to the subject directory and run any script:
```bash
python physics/electromagnetism/CurlIdentityOfElectricField.py
```

Output visualizations are saved to `output_images/`.

## ➕ Adding New Scripts

### 1. Choose the Right Directory
Organize by subject and subtopic:
- **Physics**: `physics/mechanics/`, `physics/quantum/`, `physics/thermodynamics/`
- **Mathematics**: `mathematics/linear_algebra/`, `mathematics/differential_equations/`
- **Statistics**: Place directly in `statistics/` or create subdirectories as needed
- **New Subjects**: Create new top-level directories (e.g., `computer_science/`, `chemistry/`)

### 2. Script Naming Convention
Use descriptive PascalCase names:
- `HarmonicOscillatorSimulation.py`
- `FourierSeriesDecomposition.py`
- `MonteCarloIntegration.py`

### 3. Script Template
Use the template in `templates/script_template.py` which includes:
- Header with description, course info, date
- Proper imports and documentation
- Output directory handling
- Clear function organization

### 4. Documentation
Each script should have:
- **Header comment** explaining the concept/problem
- **Inline comments** for complex calculations
- **Output descriptions** (what plots/files are generated)

### 5. Update README
When adding new topics or significant scripts, update this README with:
- New directory structure
- Brief description of the script
- Any special requirements

## 📂 Subject Directory Guidelines

### Creating New Subdirectories
```bash
# Example: Adding a new physics subtopic
mkdir -p physics/fluid_dynamics
# Add a README.md in the subdirectory
echo "# Fluid Dynamics\n\nScripts related to fluid flow, Navier-Stokes equations, etc." > physics/fluid_dynamics/README.md
```

### Subject-Specific READMEs
Each major subdirectory should contain its own README.md with:
- Overview of the topic
- List of scripts with brief descriptions
- Relevant course codes/names
- Key references or textbooks

## 🎓 Academic Context

This repository documents work from:
- University coursework and assignments
- Self-directed learning projects
- Research explorations
- Exam preparation and study aids

## 📊 Output Management

- All plots/images should be saved to `output_images/`
- Use descriptive filenames: `electric_field_curl_visualization.png`
- Consider organizing output by subject if volume grows: `output_images/physics/`, etc.

## 🔧 Development Tips

### Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Common Dependencies
Create/update `requirements.txt` as you add scripts:
```txt
numpy>=1.20.0
matplotlib>=3.3.0
scipy>=1.6.0
```

## 📝 Notes

- Scripts are educational in nature and may prioritize clarity over optimization
- Comments may be in multiple languages (English, German, Turkish) depending on course material
- Some scripts generate multiple output files - check console output for file paths

## 🤝 Contributing to Your Own Repository

Before each study session:
1. `git pull` to sync any changes
2. Create scripts in appropriate directories
3. Test and verify outputs
4. Commit with meaningful messages: `git commit -m "Add Schrödinger equation solver for quantum mechanics course"`
5. `git push` to backup your work

## 📅 Version History

Track major milestones:
- **2025-11-10**: Initial repository structure, organized by subject
- Add dates as you complete semesters or major topics

---

**License**: Personal academic work - all rights reserved unless otherwise specified.
