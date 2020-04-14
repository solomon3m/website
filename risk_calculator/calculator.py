import pickle

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
from footer import Footer

from risk_calculator.features import build_feature_cards,features

nav = Navbar()
footer = Footer()

with open('assets/risk_calculators/rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

body = dbc.Container(
    [
        dbc.Row(
        [
            dbc.Col(
            [
              html.H2("Clinical Rick Calculator")
            ]
            ),
        ],
        ),
        dbc.Row(
        [
            dbc.Col(
            [
                html.Div(
                [
                    dcc.Markdown(
                         """Severe COVID-19 patients require our most limited health care resources,\
                          ventilators and intensive care beds. As a result, physicians have the hard \
                          responsibility to decide which patients should have priority access to these \
                          resources. To help them make an informed decision, we construct and publish \
                          patient risk calculators tailored for COVID-19 patients.
                         """,
                    ),
                    dcc.Markdown(
                         """ **Disclaimer:** A model is only as good as the data it is trained on. We will \
                         release new versions of the calculator as the amount of data we receive from \
                         our partner institutions increases. If you are a medical institution and are \
                         willing to contribute to our effort, feel free to reach out to us [here](/contact).
                         """,
                    ),
                    dcc.Markdown(
                         """ **Data** (as of 2020/04/10): Our model is trained on 496 patients from the Azienda \
                         Socio-Sanitaria Territoriale di Cremona [ASST Cremona](https://www.asst-cremona.it/) which includes the Ospedale \
                         di Cremona, Ospedale Oglio Po and other minor public hospitals in the Province of \
                         Cremona. Cremona is one of the most hit italian provinces in Lombardy in the Italian \
                         COVID-19 crisis with a total of several thousand positive cases to date. Given our training \
                         population, we are most confident about the relevance of our model to: (a) Western population; \
                         (b) Severe to acute patients; (c) Congested hospitals. \
                         """,
                    ),
                    dcc.Markdown(
                         """ **This is a developmental version. It is not intended for patient or clinician use.\
                          It is available only to solicit input about its future development.**
                         """,
                         ),
                ]
                )
            ]
            ),
        ],
        ),
        dbc.Row(
        [
            dbc.Col(
                html.H5('Insert the features below into the risk calculator.')
            ),
        ]),
        dbc.Row(build_feature_cards()),
        dbc.Row(dbc.Col(dbc.Button("Submit", color="primary",id="submit-features-calc",n_clicks=0))),
        dbc.Row(
            dbc.Col(
                [
                dcc.ConfirmDialog(
                    id='calc-input-error',
                ),
                dbc.Card(
                    [
                        dbc.CardBody(id="score-calculator-card-body")
                    ],
                    color="dark",
                    inverse=True,
                    style={"marginTop":20}
                    ),
                ],
                xs=12,
                sm=6,
                md=6,
                lg=3,
            ),
            justify="center",
        ),
    ],
    className="page-body"
)

def RickCalc():
    layout = html.Div([nav, body, footer], className="site")
    return layout

def valid_input(feature_vals):
    numeric = len(features["numeric"])
    for feat in range(numeric):
        val = feature_vals[feat]
        content = features["numeric"][feat]
        name = content["name"]
        min_val = content["min_val"]
        max_val = content["max_val"]
        if val is None:
            return False, "Please insert a numeric value for {}".format(name)
        if val < min_val or val > max_val:
            return False, "Please insert a numeric value for {} between {} and {}".format(name,min_val,max_val)
    return True,""

def predict_risk(feature_vals):
    score = 0.5
    card_content = [
        html.H4("The mortality risk score is:",className="score-calculator-card-content"),
        html.H4(score,className="score-calculator-card-content"),
    ]
    return card_content
