import matplotlib.pyplot as plt

twelve_lead = plt.figure()

lead_names = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
leads = dict.fromkeys(lead_names)  # Dictionary of leads
n_rows = 3
n_cols = 4

def add_leads():
    count = 0

    for col in range(n_cols):
        print("Column ", col)
        for row in range(n_rows):
            print("Row", row)
            name = lead_names[col*n_rows + row]
            print(name)

            ax = twelve_lead.add_axes([(0.1 + col*0.22), (1 - (1+row)*0.3), 0.16, 0.2])
            ax.set_title(name)
            print(name)
            leads.update({name: ax})


    print(leads)

