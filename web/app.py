import faicons as fa
import plotly.express as px

# Load data and compute static values
from shared import app_dir, tips
from shinywidgets import render_plotly

from shiny import reactive, render
from shiny.express import input, ui

from datetime import datetime

bill_rng = (min(tips.total_bill), max(tips.total_bill))

#from db import get_last_n_rows
#PRICE_DATA =  get_last_n_rows(7*24)   # Last 7 days

from api import get_forecast
PRICE_DATA = get_forecast()

import joblib

model = joblib.load(app_dir / 'model/model.joblib')
PRICE_DATA['predictions'] = model.predict(PRICE_DATA.drop(columns=['Aika','Hinta_snt_per_kWh']))

date_rng = (PRICE_DATA['Aika'].min().strftime('%Y-%m-%d'),
            PRICE_DATA['Aika'].max().strftime('%Y-%m-%d'))

# Add page title and sidebar
ui.page_opts(title="Electricity Spot Price Prediction", fillable=True)

with ui.sidebar(open="desktop"):
    ui.input_date_range(
        id="total_days",
        label="Date Range",
        min='2024-01-01',
        max=date_rng[1],
        start=date_rng[0],
        end=date_rng[1],
    )
    
    ui.input_slider(
        "total_bill",
        "Bill amount",
        min=bill_rng[0],
        max=bill_rng[1],
        value=bill_rng,
        pre="$",
    )
    ui.input_checkbox_group(
        "time",
        "Food service",
        ["Lunch", "Dinner"],
        selected=["Lunch", "Dinner"],
        inline=True,
    )
    ui.input_action_button("reset", "Reset filter")

# Add main content
ICONS = {
    "user": fa.icon_svg("user", "regular"),
    "wallet": fa.icon_svg("wallet"),
    "currency-dollar": fa.icon_svg("dollar-sign"),
    "ellipsis": fa.icon_svg("ellipsis"),
    "calender":fa.icon_svg("calendar-days"),
}

with ui.layout_columns(fill=False):

    with ui.value_box(showcase=ICONS["calender"]):
        "Today"

        @render.express
        def date_today():
            datetime.today().strftime('%b %d, %Y')

    with ui.value_box(showcase=ICONS["user"]):
        "Total tippers"

        @render.express
        def total_tippers():
            tips_data().shape[0]

    with ui.value_box(showcase=ICONS["wallet"]):
        "Average tip"

        @render.express
        def average_tip():
            d = tips_data()
            if d.shape[0] > 0:
                perc = d.tip / d.total_bill
                f"{perc.mean():.1%}"

    with ui.value_box(showcase=ICONS["currency-dollar"]):
        "Average bill"

        @render.express
        def average_bill():
            d = tips_data()
            if d.shape[0] > 0:
                bill = d.total_bill.mean()
                f"${bill:.2f}"


with ui.layout_columns(col_widths=[12]):
    


    with ui.card(full_screen=True):
        with ui.card_header(class_="d-flex justify-content-between align-items-center"):
            "Electricity Spot Price"
            with ui.popover(title="Add a color variable", placement="top"):
                ICONS["ellipsis"]
                ui.input_radio_buttons(
                    "scatter_color",
                    None,
                    ["none", "sex", "smoker", "day", "time"],
                    inline=True,
                )

        @render_plotly
        def scatterplot():
            """
            color = input.scatter_color()
            return px.scatter(
                tips_data(),
                x="total_bill",
                y="tip",
                color=None if color == "none" else color,
                trendline="lowess",
            )
            """
            return px.line(
                price_data(),
                x="Aika",
                y=['predictions'],
                markers=True,
            )


ui.include_css(app_dir / "styles.css")

# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------


@reactive.calc
def tips_data():
    bill = input.total_bill()
    idx1 = tips.total_bill.between(bill[0], bill[1])
    idx2 = tips.time.isin(input.time())
    return tips[idx1 & idx2]


@reactive.calc
def price_data():
    return PRICE_DATA

@reactive.effect
@reactive.event(input.reset)
def _():
    ui.update_slider("total_bill", value=bill_rng)
    ui.update_checkbox_group("time", selected=["Lunch", "Dinner"])
