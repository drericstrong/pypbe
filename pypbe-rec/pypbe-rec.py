### PyPBE Recommendation Bokeh Simulator
### Written By: Eric Strong
### Last Updated: 2017/08/15

import os
import pandas as pd
from pypbe.core import PBE
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models.tools import SaveTool
from bokeh.models.ranges import Range1d
from bokeh.models.annotations import Label
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource as CDS
from bokeh.models.widgets.tables import DataTable, TableColumn
from bokeh.models.widgets import Slider, Button, RadioButtonGroup, Div

###-----------------------------------------------------------------------###
###------------------------PARAMETER DEFAULTS-----------------------------###
### This section contains defaults and ranges for the Bokeh controls and  ###
### may be modified without concern, if required.                         ###
###-----------------------------------------------------------------------###
# Syntax is "default, range:[Lower, Upper, Step]"
d_pbe, r_pbe = 15, [0, 100, 1] # Point Buy Equivalent
d_s, d_ss = "PF", ["PF", "3e", "4e", "5e"] # Systems

###-----------------------------------------------------------------------###
###----------------------GRAPHICAL USER INTERFACE-------------------------###
### This code defines the Bokeh controls that are used for the user       ###
### interface. All the defaults for the controls are above. This code     ###
### should not need to be modified.                                       ### 
###-----------------------------------------------------------------------###
# Main Control Buttons
plot_sim = Button(label="Simulate")
up_sys = RadioButtonGroup(labels=d_ss, active=0)
up_pbe = Slider(title="Point Buy Equivalent", value=d_pbe, 
               start=r_pbe[0], end=r_pbe[1], step=r_pbe[2], width=1200)
# Data Tables
dt_pbe_cols = [TableColumn(field="desc", title="Description"),
               TableColumn(field="typ", title="Typical Roll"),
               TableColumn(field="mvs", title="Mean"),
               TableColumn(field="stds", title="Std"),
               TableColumn(field="p5", title="5%"),
               TableColumn(field="p95", title="95%")]
source_dt_pbe = CDS()
dt_pbe = DataTable(source=source_dt_pbe, columns=dt_pbe_cols, editable=False,
                   selectable=True, width=1200, height=350)
# Plots- Raw Array and PBE Histogram
plot_pbe = figure(plot_height=350, plot_width=1200, logo=None, 
                  title="Point Buy Equivalent Histogram", 
                  toolbar_location="above", y_axis_label='Probability',
                  x_axis_label='Point Buy Equivalent', 
                  tools="pan,box_zoom,wheel_zoom,hover")
plot_pbe.add_tools(SaveTool(name="pbe_hist.jpg"))

###-----------------------------------------------------------------------###
###----------------------PBE CALCULATION FUNCTIONS------------------------###
### This section contains low-level calculations for the Point Buy        ###
### Equivalent functions.                                                 ###
###-----------------------------------------------------------------------###
def sim(num_dice, dice_type, keep_dice, add_val, num_attr, keep_attr, reroll, 
        num_arrays, num_hist, pbe_map):
    pbe = PBE(num_dice, dice_type, add_val, num_attr, num_arrays, reroll,
              keep_dice, keep_attr, pbe_map)
    pbe.roll_mc((int(10**6)))    
    txtbox = pbe._build_text(pbe.arr_res["means"], pbe.arr_res["5percentile"],
                             pbe.arr_res["95percentile"])
    return pbe.arr_res, pbe.pbe_res, txtbox

def find_ranges(arr_res, pbe_res):
    raw_xmin = 0
    raw_xmax = len(d_arr["raw_bins"][-1])
    raw_ymin = 0
    raw_ymax = 1.05*max([max(x) for x in arr_res["raw_bins"]])
    pbe_xmin = pbe_res["raw_bins"][:,0].min()
    pbe_xmax = pbe_res["raw_bins"][:,0].max()
    pbe_ymin = 0
    pbe_ymax = 1.05*pbe_res["raw_bins"][:,1].max()
    return ([raw_xmin, raw_xmax, raw_ymin, raw_ymax], 
            [pbe_xmin, pbe_xmax, pbe_ymin, pbe_ymax])

###-----------------------------------------------------------------------###
###------------------DATA SOURCES AND INITIALIZATION----------------------###
### This section defines the data sources which will be used in the Bokeh ###
### plots. To update a Bokeh plot in the server, each of the sources will ###
### be modified in the CALLBACKS section.                                 ###
###-----------------------------------------------------------------------###
basedir = os.path.dirname(os.path.abspath(__file__))
df_3e = pd.read_csv(basedir + '//pypbe-rec_results_3e.csv')
df_4e = pd.read_csv(basedir + '//pypbe-rec_results_4e.csv')
df_pf = pd.read_csv(basedir + '//pypbe-rec_results_pf.csv')
# Generating some initial data for the plots, based on the user defaults
d_arr, d_pbe, tb = sim(3, 6, 3, 0, 6, 6, 0, 1, int(10**6), "pf")
maxval_pbe = 1.05 * max(d_pbe["raw_bins"][:, 1])
# Defining the Bokeh data sources
source_pbe = CDS(data=dict(x=d_pbe["raw_bins"][:, 0], 
                           y=d_pbe["raw_bins"][:, 1]/2,
                           yh=d_pbe["raw_bins"][:, 1]))
source_pbe_mean = CDS(data=dict(x=[d_pbe["means"], d_pbe["means"]],
                                y=[0, maxval_pbe]))
# Associating the sources with a line on a plot
plot_pbe.rect('x', 'y', width = 1, height='yh', source=source_pbe,
              fill_color="blue")
plot_pbe.line('x', 'y', source=source_pbe_mean, line_width=4, line_alpha=0.6,
              line_color='orange')
# Defining the x and y ranges objects for the plots
d_rawr, d_pber = find_ranges(d_arr, d_pbe)
xrange_pbe = Range1d(bounds=[None, None], start=d_pber[0], end=d_pber[1])
yrange_pbe = Range1d(bounds=[0, 1], start=d_pber[2], end=d_pber[3])
# Associating the ranges with each of the previously-defined plots
plot_pbe.x_range = xrange_pbe
plot_pbe.y_range = yrange_pbe
# Updating the data tables
pbe_m = [str(round(d_pbe["means"],2))]
pbe_s = [str(round(d_pbe["stds"],2))]
pbe_5 = [str(round(d_pbe["5percentile"],2))]
pbe_95 = [str(round(d_pbe["95percentile"],2))]
source_dt_pbe.data = dict(mvs=pbe_m, stds=pbe_s, p5=pbe_5, p95=pbe_95)
# Labels
label_fpb = Label(text="Fair Point Buy:15", x=70, y=280, 
                  x_units='screen', y_units='screen')
plot_pbe.add_layout(label_fpb)

###-----------------------------------------------------------------------###
###----------------------------CALLBACKS----------------------------------###
### This section defines the behavior of the GUI as the user interacts    ###
### with the controls.                                                    ###
###-----------------------------------------------------------------------###
# Behavior when the "Simulate" button is clicked    
def update_plot():
    test = 1
#    pbe_map = d_ss[up_sys.active]
#    arr_res, pbe_res, txt = sim(num_dice, dice_type, keep_dice, add_val, num_attr,
#                                keep_attr, reroll, num_arrays, num_hist, pbe_map)
#    maxval_pbe2 = 1.05 * max(pbe_res["raw_bins"][:, 1])
#  
#    # Back to clean(er) code again
#    source_pbe.data = dict(x=pbe_res["raw_bins"][:, 0], 
#                           y=pbe_res["raw_bins"][:, 1]/2,
#                           yh=pbe_res["raw_bins"][:, 1])
#    source_pbe_mean.data = dict(x=[pbe_res["means"], pbe_res["means"]],
#                                y=[0, maxval_pbe2])
#    # Update the ranges
#    rawr, pber = find_ranges(arr_res, pbe_res)
#    xrange_pbe.start, xrange_pbe.end = pber[0], pber[1]
#    yrange_pbe.start, yrange_pbe.end = pber[2], pber[3]
#    # Update the data tables
#    pbe_m = [round(pbe_res["means"],2)]
#    pbe_s = [round(pbe_res["stds"],2)]
#    pbe_5 = [round(pbe_res["5percentile"],2)]
#    pbe_95 = [round(pbe_res["95percentile"],2)]
#    source_dt_pbe.data = dict(mvs=pbe_m, stds=pbe_s, p5=pbe_5, p95=pbe_95)
#    # Update the labels
#    label_fpb.text = "Fair Point Buy:{}".format(int(round(pbe_m[0])))

# Button callbacks, using the above functions
plot_sim.on_click(update_plot)

###-----------------------------------------------------------------------###
###----------------------------PAGE LAYOUT--------------------------------###
### This section defines the basic layout of the GUI.                     ###
###-----------------------------------------------------------------------###
pbet = Div(text="<h2>Point Buy Equivalent Recommender</h2>", width=1200)
row_inputs = row(plot_sim, up_sys)
row_page = column(pbet, row_inputs, up_pbe, dt_pbe, plot_pbe, width=1200)
curdoc().add_root(row_page)
curdoc().title = "Point Buy Equivalent Recommender (Powered by PyPBE)"