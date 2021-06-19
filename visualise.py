import matplotlib.pyplot as plt




lead_names = ['I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
leads = dict.fromkeys(lead_names)  # Dictionary of lead names and corresponding axes
n_rows = 3
n_cols = 4

def add_twelve_lead_axes():
    twelve_lead = plt.figure()
    for col in range(n_cols):
        for row in range(n_rows):
            name = lead_names[col*n_rows + row]
            ax = twelve_lead.add_axes([(0.1 + col*0.22), (1 - (1+row)*0.3), 0.16, 0.2])
            ax.set_title(name)
            leads.update({name: ax})


def plot_twelve_lead(data):
    add_twelve_lead_axes()
    assert len(data) == len(lead_names)
    count = 0
    for name in lead_names:
        ax = leads[name]
        ax.plot(data[count])
        leads.update({name: ax})
        count = count + 1

def plot_lead_single(data, lead_name):
    single_lead = plt.figure()
    ax = single_lead.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.set_title(lead_name)
    ax.plot(data[lead_names.index(lead_name)])

