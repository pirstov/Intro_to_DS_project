from pathlib import Path

import pandas as pd

app_dir = Path(__file__).parent
tips = pd.read_csv(app_dir / "tips.csv")
holidays = pd.read_excel(app_dir / "public_holidays.xlsx")
