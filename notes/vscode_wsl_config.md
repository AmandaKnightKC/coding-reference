
# VS Code WSL: Recovery & Environment Setup Notes

Notes from troubleshooting and restoring VS Code WSL development environment_

## 🧩 VS Code Disappearance

- VS Code was unexpectedly uninstalled (possibly by Windows updates or system cleanup).
- Reinstalled VS Code and reconnected to WSL.

## 🔌 Extension Management

- Extensions reinstalled:
  - `ms-python.python`, `ms-toolsai.jupyter`, `github.copilot`, etc.
- Saved extensions list to `extensions.txt` for reproducibility.
- [x] Consider adding `extensions.txt` to every future repo.

## ⚙️ Key Settings Configured

- `settings.json`:
  - Default terminal: WSL
  - Format on save: Enabled
  - Minimap: Disabled

## 📦 Conda vs Virtualenv

-- Conda: better for data science, dependency resolution, Jupyter
-- venv: lightweight, Python-native

Using Conda exclusively for this environment

## ✅ Summary

- VS Code fully restored
- Extensions saved and tracked
- MySQL access verified
- WSL + Conda environment rebuilt and functional
