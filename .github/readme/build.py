"""Build terminal-style SVG art and result text from actual notebook evidence."""
import json
from pathlib import Path
import subprocess
import sys
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MONO = "ui-monospace,Consolas,'Liberation Mono',monospace"
GLYPHS = {
    "M": ["#   #", "## ##", "# # #", "#   #", "#   #", "#   #", "#   #"],
    "L": ["#    ", "#    ", "#    ", "#    ", "#    ", "#    ", "#####"],
    "A": [" ### ", "#   #", "#   #", "#####", "#   #", "#   #", "#   #"],
    "B": ["#### ", "#   #", "#   #", "#### ", "#   #", "#   #", "#### "],
    " ": ["     "] * 7,
}
THEMES = {
    "dark": {"fg": "#e6edf3", "muted": "#8b949e", "accent": "#80e0ff", "green": "#79d6a4", "line": "#30363d"},
    "light": {"fg": "#1f2328", "muted": "#667085", "accent": "#0969a6", "green": "#1a7f37", "line": "#d0d7de"},
}


def text(x, y, value, theme, kind="fg", size=14):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{theme[kind]}">{escape(str(value))}</text>'


def banner(theme):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="850" height="205" viewBox="0 0 850 205" role="img" aria-label="ML LAB"><g font-family="{MONO}">']
    for letter_index, letter in enumerate("ML LAB"):
        for y, row in enumerate(GLYPHS[letter]):
            for x, char in enumerate(row):
                if char == "#":
                    p.append(f'<rect x="{108 + (letter_index * 6 + x) * 18}" y="{24 + y * 18}" width="15" height="15" rx="1" fill="{theme["accent"]}" opacity="{1 - y * 0.07}"/>')
    p += [text(108, 185, "hafiz@ml-lab:~$ learn --with-evidence", theme, "muted", 15), "</g></svg>"]
    return "\n".join(p)


def card(theme, a, b):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="850" height="305" viewBox="0 0 850 305" role="img" aria-label="Two worked machine-learning labs and measured evidence"><g font-family="{MONO}">']
    p += [text(28, 32, "./experiment --trace", theme, "accent", 16),
          text(28, 67, "01 / features", theme), text(28, 95, "inspect -> engineer -> select", theme, "muted", 13),
          text(28, 145, "02 / supervised", theme), text(28, 173, "split -> fit -> evaluate -> save", theme, "muted", 13),
          text(28, 224, "[ok] two executed notebooks", theme, "green", 13),
          text(28, 252, "12 source files / seed 42", theme, "muted", 13),
          f'<line x1="403" y1="25" x2="403" y2="269" stroke="{theme["line"]}"/>',
          text(438, 32, "hafiz@ml-lab:~$ cat ./evidence", theme, "accent", 14)]
    rows = [
        ("runtime", "python 3.12 / .venv"),
        ("features", f"{a['feature_auc']['raw + engineered']:.3f} validation auc"),
        ("selection", f"{a['student_mae']['lasso']:.3f} lasso mae"),
        ("titanic", f"{b['titanic_final']['test_roc_auc']:.3f} final test auc"),
        ("bike/hour", f"{b['bike_hourly']['mae']:.1f} rentals mae"),
        ("models", "pipeline + json card"),
    ]
    for i, (key, value) in enumerate(rows):
        p += [text(438, 72 + i * 28, key, theme, "muted", 13), text(555, 72 + i * 28, value, theme, "fg", 13)]
    p += [text(438, 268, "[ok] reproducible course experiments", theme, "green", 12), "</g></svg>"]
    return "\n".join(p)


def main():
    a = json.loads((ROOT / "results/lab01/summary.json").read_text(encoding="utf-8"))
    b = json.loads((ROOT / "results/lab02/summary.json").read_text(encoding="utf-8"))
    predictor = subprocess.run([sys.executable, str(ROOT / "predict_passenger.py"),
        "--pclass", "2", "--sex", "female", "--age", "30", "--fare", "20"],
        check=True, text=True, capture_output=True)
    values = {
        "RAW_AUC": f"{a['feature_auc']['raw columns']:.3f}",
        "ENGINEERED_AUC": f"{a['feature_auc']['raw + engineered']:.3f}",
        "CV_AUC": f"{b['titanic_final']['cv_roc_auc']:.3f}",
        "TEST_AUC": f"{b['titanic_final']['test_roc_auc']:.3f}",
        "HOURLY_MAE": f"{b['bike_hourly']['mae']:.1f}",
        "DAILY_MAE": f"{b['bike_daily']['mae']:.1f}",
        "LASSO_MAE": f"{a['student_mae']['lasso']:.3f}",
        "LASSO_KEPT": str(a['lasso_retained']),
        "INSURANCE_MAE": f"{b['insurance']['linear regression']['mae']:,.2f}",
        "HEART_AUC": f"{b['heart']['roc_auc']:.3f}",
        "HEART_ACC": f"{b['heart']['accuracy']:.3f}",
        "FN_HIGH": str(b['cancer_thresholds'][0]['fn']),
        "FN_LOW": str(b['cancer_thresholds'][1]['fn']),
        "FP_LOW": str(b['cancer_thresholds'][1]['fp']),
        "CLI_OUTPUT": predictor.stdout.strip(),
    }
    template = (HERE / "template.md").read_text(encoding="utf-8")
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    (ROOT / "README.md").write_text(template, encoding="utf-8", newline="\n")
    for name, theme in THEMES.items():
        (HERE / f"banner-{name}.svg").write_text(banner(theme), encoding="utf-8")
        (HERE / f"card-{name}.svg").write_text(card(theme, a, b), encoding="utf-8")
    report = ["# Measured results / Labs 01 and 02", "", "Generated from the executed notebook summaries. Seed: 42.", "",
              "## Lab 01 / Feature engineering", "", "| Features | Validation ROC AUC |", "|---|---:|"]
    report += [f"| {name} | {value:.4f} |" for name, value in a["feature_auc"].items()]
    report += ["", "Raw and engineered features use identical row indices and logistic regression.",
               "Additional cabin and fare-per-family features do not improve this split further.", "",
               "## Lab 01 / Selection", "", "| Model | Validation MAE / grade points |", "|---|---:|"]
    report += [f"| {name} | {value:.4f} |" for name, value in a["student_mae"].items()]
    report += ["", f"Lasso retained {a['lasso_retained']} of {a['lasso_encoded_columns']} encoded columns.",
               "The G2 row is a deliberate leakage demonstration, not a valid enrolment forecast.",
               "The final row also excludes accumulated absences. All other candidate fields need",
               "a prediction-time availability check for real use.", "",
               "## Lab 02 / Regression", "", "| Model | Validation MAE | RMSE | R-squared |", "|---|---:|---:|---:|"]
    regressions = dict(b["insurance"])
    regressions["bike daily forest"] = b["bike_daily"]
    regressions["bike hourly forest"] = b["bike_hourly"]
    report += [f"| {name} | {scores['mae']:.3f} | {scores['rmse']:.3f} | {scores['r2']:.4f} |" for name, scores in regressions.items()]
    report += ["", "Insurance errors are dollars; bike errors are daily/hourly rentals.",
               "Bike validation contains the last 20% of the series, in time order.", "",
               "## Lab 02 / Classification", "", "| Model / evaluation | Accuracy | ROC AUC |", "|---|---:|---:|"]
    report += [f"| Titanic {name} / development validation | {scores['accuracy']:.4f} | {scores['roc_auc']:.4f} |" for name, scores in b["titanic_validation"].items()]
    report += [f"| Titanic tuned logistic / final test | {b['titanic_final']['test_accuracy']:.4f} | {b['titanic_final']['test_roc_auc']:.4f} |",
               f"| Heart disease / validation | {b['heart']['accuracy']:.4f} | {b['heart']['roc_auc']:.4f} |", "",
               f"Titanic baseline accuracy: {b['titanic_majority_baseline']:.4f}. Best grid: `{b['titanic_final']['best_parameters']}`.",
               f"Mean five-fold CV AUC: {b['titanic_final']['cv_roc_auc']:.4f}; 668 development rows and 223 reserved test rows.",
               "The handout reuses one split for Part C and the final test; the worked notebook",
               "reserves the final test before Part C, so its model-comparison results differ.", "",
               f"Breast-cancer validation ROC AUC: {b['cancer']['roc_auc']:.4f}; average precision: {b['cancer']['average_precision']:.4f}.", "",
               "## Lab 02 / Threshold decision", "", "| Threshold | TN | FP | FN | TP | Precision | Recall |", "|---|---:|---:|---:|---:|---:|---:|"]
    report += [f"| {s['threshold']:.2f} | {s['tn']} | {s['fp']} | {s['fn']} | {s['tp']} | {s['precision']:.4f} | {s['recall']:.4f} |" for s in b["cancer_thresholds"]]
    report += ["", "The lower threshold avoids two missed positives with no extra false alerts in this sample.",
               "This is validation evidence for the [coursework decision memo](../results/lab02/decision_memo.md).", "",
               "## Source evidence", "",
               "- [Lab 01 summary](../results/lab01/summary.json)",
               "- [Lab 02 summary](../results/lab02/summary.json)",
               "- [Feature comparison](../results/lab01/feature_comparison.csv)",
               "- [Student selection](../results/lab01/student_feature_selection.csv)",
               "- [Insurance metrics](../results/lab02/insurance_metrics.csv)",
               "- [Titanic CV table](../results/lab02/titanic_cv_results.csv)",
               "- [Titanic model card](../models/titanic_survival_card.json)",
               "- [Threshold counts](../results/lab02/cancer_thresholds.csv)", ""]
    (ROOT / "docs/results.md").write_text("\n".join(report), encoding="utf-8")
    print("Built README, dark/light art, and measured results report.")


if __name__ == "__main__":
    main()
