def get_data_cols():
    return [
        "Country",
        "Study Pop Size (N)",
        "Paper Title",
        "Peer-Reviewed? (As of Date Added)",
        "Study length (days)",
        "Overall study population or subgroup?",
        "Subgroup",
        "Median Age",
        "Hypertension",
        "Diabetes",
        "Cardiovascular Disease (incl. CAD)",
        "Cerebrovascular Disease",
        "Chronic kidney/renal disease",
        "Chronic obstructive lung (COPD)",
        "Fever (temperature ≥37·3°C)",
        "Cough",
        "Fatigue",
        "Diarrhoea",
        "Shortness of Breath (dyspnoea)",
        "Nausea or Vomiting",
        "Loss of Appetite/Anorexia",
        "White Blood Cell Count (10^9/L) - Median",
        "Lymphocyte Count (10^9/L) - Median",
        "Platelet Count (10^9/L) - Median",
        "C-Reactive Protein (mg/L)",
        "Hemoglobin (g/L) - Median",
        "Total Bilirubin (umol/L) - Median",
        "D-Dimer (mg/L)",
        "Albumin (g/L)",
        "Uses Kaletra (lopinavir–ritonavir)",
        "Uses Arbidol (umifenovir)",
        "Corticosteroid (including Glucocorticoid, Methylprednisolone)",
        "Invasive mechanical ventilation",
        "ARDS",
        "Hospital admission (%)",
        "Discharged (%)",
        "Mortality",
        "Projected Mortality (accounting for patients not currently discharged)"
    ]

def get_states():
    return {
        'US':'US','Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'American Samoa': 'AS',
        'Arizona': 'AZ', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT',
        'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
        'Guam': 'GU', 'Hawaii': 'HI', 'Iowa': 'IA', 'Idaho': 'ID', 'Illinois': 'IL',
        'Indiana': 'IN', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
        'Massachusetts': 'MA', 'Maryland': 'MD', 'Maine': 'ME', 'Michigan': 'MI',
        'Minnesota': 'MN', 'Missouri': 'MO', 'Northern Mariana Islands': 'MP',
        'Mississippi': 'MS', 'Montana': 'MT', 'National': 'NA', 'North Carolina': 'NC',
        'North Dakota': 'ND', 'Nebraska': 'NE', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
        'New Mexico': 'NM', 'Nevada': 'NV', 'New York': 'NY', 'Ohio': 'OH', 'Oklahoma': 'OK',
        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 'Rhode Island': 'RI',
        'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
        'Utah': 'UT', 'Virginia': 'VA', 'Virgin Islands': 'VI', 'Vermont': 'VT',
        'Washington': 'WA', 'Wisconsin': 'WI', 'West Virginia': 'WV', 'Wyoming': 'WY'
    }


# colors that align with inferno
def get_colors():
    return [
                '#000004',
                '#4a0c6b',
                '#a52c60',
                '#ed6925',
                '#f7d31d'
            ]
