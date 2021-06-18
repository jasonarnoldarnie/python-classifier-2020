import matplotlib.pyplot as plt

twelve_lead = plt.figure()

lead_names = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
leads = dict.fromkeys(lead_names)  # Dictionary of leads


def add_leads():
    for name in lead_names:
        ax = twelve_lead.add_axes([0.15, 0.1, 0.3, 0.3]) # TODO don't plot them all on top of eachotherf
        ax.set_title(name)
        print(name)
        leads.update({name: ax})
    print(leads)

