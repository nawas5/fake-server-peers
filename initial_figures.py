import plotly.express as px
import os

def initial_figure_simulation():
    fig = px.scatter(x=[0, 0, 1, 1], y=[0, 1, 0, 1])
    fig.update_layout(xaxis=dict(range=[0, 1]))
    fig.update_layout(yaxis=dict(range=[0, 1]))
    fig.update_traces(marker=dict(color="white", size=6))
    # чтобы создать окошко

    fig.update_layout(
        coloraxis_showscale=False,
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        # убрали линии сетки
        autosize=True
    )

    # убираем значения с графика по осям
    fig.update_xaxes(showticklabels=False, title_text="")
    fig.update_yaxes(showticklabels=False, title_text="")

    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.update_layout(modebar=dict(bgcolor="rgba(0, 0, 0, 0)"))
    image_path = os.path.join(os.getcwd(), "assets/Rooms12x6.jpg")

    from PIL import Image

    img = Image.open(image_path)

    fig.add_layout_image(
        dict(
            source=img,
            xref="x",
            yref="y",
            x=0,
            y=1,
            sizex=1,
            sizey=1,
            sizing="stretch",
            opacity=0.7,
            layer="below",
        )
    )

    # оставит краюшки у этой штуки
    fig.update_yaxes(scaleanchor="x", scaleratio=0.70)

    fig.update_layout(autosize=True)

    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=False, showticklabels=False),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)"
        # сделали другим размером
        # чтобы добавить отступы от края
    )
    return fig
