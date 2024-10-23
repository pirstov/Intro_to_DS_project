"""
with ui.card(full_screen=True):
    ui.card_header("Tips data")

    @render.data_frame
    def table():
        return render.DataGrid(tips_data())
"""

"""
with ui.card(full_screen=True):
    with ui.card_header(class_="d-flex justify-content-between align-items-center"):
        "Tip percentages"
        with ui.popover(title="Add a color variable"):
            ICONS["ellipsis"]
            ui.input_radio_buttons(
                "tip_perc_y",
                "Split by:",
                ["sex", "smoker", "day", "time"],
                selected="day",
                inline=True,
            )

    @render_plotly
    def tip_perc():
        from ridgeplot import ridgeplot

        dat = tips_data()
        dat["percent"] = dat.tip / dat.total_bill
        yvar = input.tip_perc_y()
        uvals = dat[yvar].unique()

        samples = [[dat.percent[dat[yvar] == val]] for val in uvals]

        plt = ridgeplot(
            samples=samples,
            labels=uvals,
            bandwidth=0.01,
            colorscale="viridis",
            colormode="row-index",
        )

        plt.update_layout(
            legend=dict(
                orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5
            )
        )

        return plt
"""
