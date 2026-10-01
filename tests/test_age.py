import json
from pathlib import Path
import re
import subprocess
import unittest

from f1stats.generate import build_template_env


def driver(name, age=None, debut_age=None, seasons=None):
    return {
        "name": f"Driver {name}", "family_name": name,
        "age": age, "debut_age": debut_age, "f1_seasons": seasons,
        "dob": "2000-01-01" if age is not None else "",
        "debut_year": 2020 if seasons is not None else None,
        "team_css": "test-team", "team_hex": "#ffffff", "team_display": "Test Team",
    }


class AgePageTests(unittest.TestCase):
    def render(self, drivers):
        data = {"year": 2026, "season_start": "2026-03-08", "generated": "2026-10-01",
                "drivers": drivers}
        html = build_template_env().get_template("age.html").render(data=data)
        scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
        self.assertEqual(len(scripts), 1)
        result = subprocess.run(
            ["node", str(Path(__file__).with_name("age_runtime.cjs"))],
            input=scripts[0], text=True, capture_output=True, check=True,
        )
        return html, json.loads(result.stdout)

    def assert_stats(self, result, mean, median, debut):
        for name, value in (("mean-age", mean), ("median-age", median), ("mean-debut", debut)):
            self.assertEqual(str(result["stats"][f"stat-{name}"]["textContent"]), value)

    def test_mixed_known_and_unknown_values(self):
        # Each metric has an independent missing value; unknown debut drivers stay in the table.
        drivers = [driver("Unknown"), driver("Older", 40, 24, 17),
                   driver("Young", 20, 18, 3), driver("NoDebut", 30),
                   driver("NoAge", None, 20, 8)]
        html, result = self.render(drivers)
        self.assert_stats(result, "30.0", "30", "20.7")
        rows = re.findall(r'<td class="driver-name">(.*?)</td>', html)
        self.assertEqual(rows, ["Driver Young", "Driver NoAge", "Driver Older",
                                "Driver Unknown", "Driver NoDebut"])
        self.assertIn("Unknown</td>", html)
        self.assertIn("33% of drivers with known ages", html)
        self.assertIn("2 of 3 drivers with known debut ages (67%)", html)
        self.assertIn("17 seasons in F1", html)
        self.assertEqual(result["charts"]["ageChart"]["bars"], 3)
        self.assertEqual(result["charts"]["debutChart"]["bars"], 3)
        self.assertNotIn("None", html)

    def test_unknown_debut_preserves_known_current_age(self):
        html, result = self.render([driver("Newcomer", 19), driver("Known", 28, 18, 11)])
        self.assert_stats(result, "23.5", "23.5", "18.0")
        self.assertIn('debutAge:null, seasons:null', html)
        self.assertEqual(result["charts"]["ageChart"]["bars"], 2)
        self.assertEqual(result["charts"]["debutChart"]["bars"], 1)

    def test_empty_grid(self):
        html, result = self.render([])
        self.assert_stats(result, "—", "—", "—")
        self.assertEqual(html.count('class="stat-sm">Not available'), 4)
        self.assertIn("Debut ages are not available yet.", html)
        for chart in result["charts"].values():
            self.assertEqual(chart, {"bars": 0, "labels": []})

    def test_all_values_unknown(self):
        html, result = self.render([driver("UnknownA"), driver("UnknownB")])
        self.assert_stats(result, "—", "—", "—")
        self.assertEqual(html.count('class="driver-name"'), 2)
        self.assertEqual(html.count('class="stat-sm">Not available'), 4)
        for chart in result["charts"].values():
            self.assertEqual(chart, {"bars": 0, "labels": []})

    def test_known_values_and_duplicate_ages(self):
        _, result = self.render([driver("A", 20, 18, 3), driver("B", 20, 18, 3),
                                 driver("C", 33, 23, 11), driver("D", 40, 24, 17)])
        self.assert_stats(result, "28.3", "26.5", "20.8")
        self.assertEqual(result["charts"]["ageChart"]["bars"], 3)
        self.assertEqual(result["charts"]["debutChart"]["bars"], 3)

    def test_driver_names_are_serialized_as_javascript_strings(self):
        name = 'O\'Name "Quoted" \\ Backslash'
        _, result = self.render([driver(name, 20, 18, 3)])
        self.assert_stats(result, "20.0", "20", "18.0")
        self.assertIn(name, result["charts"]["debutChart"]["labels"])
