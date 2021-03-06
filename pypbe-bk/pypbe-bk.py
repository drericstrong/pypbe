### PyPBE Bokeh Simulator
### Written By: Eric Strong
### Last Updated: 2017/08/31

from pypbe.core import PBE
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models.tools import SaveTool
from bokeh.models.ranges import Range1d
from bokeh.models.annotations import Label
from bokeh.layouts import column, row, widgetbox
from bokeh.models import ColumnDataSource as CDS, CustomJS
from bokeh.models.widgets.tables import DataTable, TableColumn
from bokeh.models.widgets import Slider, Div, Button, RadioButtonGroup

###-----------------------------------------------------------------------###
###------------------------PARAMETER DEFAULTS-----------------------------###
### This section contains defaults and ranges for the Bokeh controls and  ###
### may be modified without concern, if required.                         ###
###-----------------------------------------------------------------------###
# Syntax is "default, range:[Lower, Upper, Step]"
d_nd, r_nd = 3, [1, 12, 1] # Number of Dice
d_dt, r_dt = 6, [2, 12, 1] # Dice Sides
d_kd, r_kd = 3, [1, 11, 1] # Dice to Keep
d_av, r_av = 0, [-8, 16, 1] # Add Value
d_na, r_na = 6, [1, 20, 1] # Number of Attributes
d_ka, r_ka = 6, [1, 10, 1] # Attributes to Keep
d_rr, r_rr = 0, [0, 11, 1] # Rerolls
d_nar, r_nar = 1, [1, 10, 1] # Number of Arrays
d_hi, r_hi = 4, [3, 5, 1] # Monte Carlo Histories
d_rl, r_rl = 1, [1, 20, 1] # Roll lower limit
d_rh, r_rh = 20, [1, 20, 1] # Roll higher limit
d_pl, r_pl = -21, [-21, 30, 1] # PBE lower limit
d_ph, r_ph = 61, [10, 61, 1] # PBE higher limit
d_s, d_ss = "PF", ["PF", "3e", "4e", "5e"] # Systems

###-----------------------------------------------------------------------###
###----------------------GRAPHICAL USER INTERFACE-------------------------###
### This code defines the Bokeh controls that are used for the user       ###
### interface. All the defaults for the controls are above. This code     ###
### should not need to be modified.                                       ### 
###-----------------------------------------------------------------------###
# Plots- Raw Array and PBE Histogram
plot_console = Div(text="", width=600)
plot_raw = figure(plot_height=350, plot_width=600, logo=None, 
                  title="Raw Roll Histogram", toolbar_location="above",
                  x_axis_label='Dice Roll', y_axis_label='Probability',
                  tools="pan,box_zoom,wheel_zoom,hover")
plot_raw.add_tools(SaveTool(name="raw_hist.jpg"))
plot_pbe = figure(plot_height=350, plot_width=600, logo=None, 
                  title="Point Buy Equivalent Histogram", 
                  toolbar_location="above", y_axis_label='Probability',
                  x_axis_label='Point Buy Equivalent', 
                  tools="pan,box_zoom,wheel_zoom,hover")
plot_pbe.add_tools(SaveTool(name="pbe_hist.jpg"))
label_logo = Div(text='<a href="https://github.com/drericstrong/pypbe#custom-parameters">Help</a>')
# Main Control Buttons
plot_sim = Button(label="Simulate")
plot_clear = Button(label="Clear")
plot_ctls = column(plot_sim, plot_clear, label_logo)
# User-Configurable Parameters
up_title = Div(text="System:")
up_sys = RadioButtonGroup(labels=d_ss, active=0)
up_nd = Slider(title="Number of Dice Per Attribute ('X' in 'XdY+Z')", 
               value=d_nd, start=r_nd[0], end=r_nd[1], step=r_nd[2])
up_dt = Slider(title="Dice Sides ('Y' in 'XdY+Z')", value=d_dt, 
               start=r_dt[0], end=r_dt[1], step=r_dt[2])
up_kd = Slider(title="Dice to Keep Per Attribute (best 'KdY' of 'XdY')", 
               value=d_kd, start=r_kd[0], end=r_kd[1], step=r_kd[2])
up_av = Slider(title="Modifier +/- ('Z' in 'XdY+Z')", value=d_av, 
               start=r_av[0], end=r_av[1], step=r_av[2])
up_na = Slider(title="Number of Attributes (STR, INT, WIS, etc.)", value=d_na, 
               start=r_na[0], end=r_na[1], step=r_na[2])
up_ka = Slider(title="Attributes to Keep (best 'X' of 'Y' attrs)", value=d_ka, 
               start=r_ka[0], end=r_ka[1], step=r_ka[2])
up_rr = Slider(title="Rerolls (reroll if <=Value)", value=d_rr, 
               start=r_rr[0], end=r_rr[1], step=r_rr[2])
up_nar = Slider(title="Number of Arrays (keeping the best one)", value=d_nar, 
                start=r_nar[0], end=r_nar[1], step=r_nar[2])
up_hi = Slider(title="Monte Carlo Histories (10^Value)", value=d_hi, 
               start=r_hi[0], end=r_hi[1], step=r_hi[2])
up_rl = Slider(title="Ability Score Lower Limit", value=d_rl, 
               start=r_rl[0], end=r_rl[1], step=r_rl[2])
up_rh = Slider(title="Ability Score Higher Limit", value=d_rh, 
               start=r_rh[0], end=r_rh[1], step=r_rh[2])
up_pl = Slider(title="PBE Lower Limit (-21=No Limit)", value=d_pl, 
               start=r_pl[0], end=r_pl[1], step=r_pl[2])
up_ph = Slider(title="PBE Higher Limit (61=No Limit)", value=d_ph, 
               start=r_ph[0], end=r_ph[1], step=r_ph[2])
up_ctls = widgetbox(up_title, up_sys, up_nd, up_dt, up_av, up_kd, up_na, up_ka, 
                    up_rr, up_nar, up_hi, up_rl, up_rh, up_pl, up_ph)
# Data Tables
dt_raw_title = Div(text="<b>Raw Roll Statistics</b>")
dt_raw_cols = [TableColumn(field="mvs", title="Mean"),
            TableColumn(field="stds", title="Std"),
            TableColumn(field="p5", title="5%"),
            TableColumn(field="p95", title="95%")]
source_dt_raw = CDS()
dt_raw = DataTable(source=source_dt_raw, columns=dt_raw_cols, editable=False,
                   selectable=True, width=300, height=260)
dt_pbe_title = Div(text="<b>Point Buy Equivalent Statistics</b>")
dt_pbe_cols = [TableColumn(field="mvs", title="Mean"),
               TableColumn(field="stds", title="Std"),
               TableColumn(field="p5", title="5%"),
               TableColumn(field="p95", title="95%")]
source_dt_pbe = CDS()
dt_pbe = DataTable(source=source_dt_pbe, columns=dt_pbe_cols, editable=False,
                   selectable=True, width=300, height=250)

###-----------------------------------------------------------------------###
###----------------------PBE CALCULATION FUNCTIONS------------------------###
### This section contains low-level calculations for the Point Buy        ###
### Equivalent functions.                                                 ###
###-----------------------------------------------------------------------###
def sim(num_dice, dice_type, keep_dice, add_val, num_attr, keep_attr, reroll, 
        num_arrays, num_hist, pbe_map, roll_low_limit, roll_high_limit,
        pbe_low_limit, pbe_high_limit):
    # Error Checking
    if keep_dice > num_dice:
        plot_console.text = "ERROR: <br>Number of dice to keep cannot " + \
            "be greater than the number of dice."
        raise ValueError()
    if keep_attr > num_attr:
        plot_console.text = "ERROR: <br>Number of attributes to keep cannot " + \
            "be greater than the number of attributes."
        raise ValueError()
    if reroll >= dice_type:
        plot_console.text = "ERROR (Reroll): <br>Any dice roll less than the 'Reroll' value (to " + \
            "the left) will be rerolled, but you have specified a 'Reroll' " + \
            "value greater than or equal to the number of sides on the dice, " + \
            "meaning every dice will be rerolled forever. Please reduce the " + \
            "'Reroll' value or increase the 'Dice Sides' value to resolve " + \
            "this issue."
        raise ValueError()
    # If the lowest possible value is below the lowest defined point buy,
    # PyPBE can't calculate it. Same for the highest value being above the
    # highest defined point buy.
    pbe_vect = PBE._find_pb_mapping(str(pbe_map).lower())
    low_pos_val = keep_dice * 1 + add_val
    high_pos_val = (dice_type * keep_dice) + add_val
    low_def_val = min(pbe_vect.keys())
    high_def_val = max(pbe_vect.keys())
    if low_pos_val < low_def_val:
        plot_console.text = "ERROR (Low Value): <br>A typical Point Buy system is based on " + \
            "rolling 3d6 per attribute, and therefore is only defined for rolls " + \
            "between 3 and 18. For example, you can buy an '18' attribute score, but " + \
            "you can't outright buy a '19' attribute score (before racial modifiers). " + \
            "According to your selections to the left, the lowest possible roll is " + \
            str(low_pos_val) + " (dice to keep per attribute + modifier), which is less " + \
            "than 3. To resolve this issue, please increase the number of dice to keep " + \
            "per attribute or the modifier so that the lowest possible roll is at least 3."
        raise ValueError()
    elif high_pos_val > high_def_val:
        plot_console.text = "ERROR (High Value): <br>A typical Point Buy system is based on " + \
            "rolling 3d6 per attribute, and therefore is only defined for rolls " + \
            "between 3 and 18. For example, you can buy an '18' attribute score, but " + \
            "you can't outright buy a '19' attribute score (before racial modifiers). " + \
            "According to your selections to the left, the highest possible roll is " + \
            str(high_pos_val) + " (dice to keep * dice sides + modifier), which is greater " + \
            "than 18. To resolve this issue, please decrease the number of dice to keep " + \
            "per attribute or the modifier so that the highest possible roll is no greater than 18."
        raise ValueError()
    # Check that the upper and lower roll limits are not impossible    
    if roll_low_limit is not None:
        if roll_low_limit >= high_pos_val:
            plot_console.text = "The highest possible value is " + \
                             str(high_pos_val) + ", but the roll_low_limit " + \
                             "was selected as " + str(roll_low_limit) + \
                             ". Please decrease the roll_low_limit."
            raise ValueError()
    if roll_high_limit is not None: 
        if roll_high_limit <= low_pos_val:
            plot_console.text = "The lowest possible value is " + \
                             str(low_pos_val) + ", but the roll_high_limit " + \
                             "was selected as " + str(roll_high_limit) + \
                             ". Please decrease the roll_high_limit."
            raise ValueError()                       
    # Run the simulation
    pbe = PBE(num_dice, dice_type, add_val, num_attr, num_arrays, reroll,
              keep_dice, keep_attr, pbe_map, None, roll_low_limit, roll_high_limit,
              pbe_low_limit, pbe_high_limit)
    pbe.roll_mc((int(10**num_hist)))    
    txtbox = pbe._build_text(pbe.arr_res["means"], pbe.arr_res["5percentile"],
                             pbe.arr_res["95percentile"])
    plot_console.text = ""
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
# Generating some initial data for the plots, based on the user defaults
d_arr, d_pbe, tb = sim(d_nd, d_dt, d_kd, d_av, d_na, d_ka, d_rr, d_nar, d_hi, 
                       d_s, None, None, None, None)
maxval_pbe = 1.05 * max(d_pbe["raw_bins"][:, 1])
# Defining the Bokeh data sources
source_roll1 = CDS(data=dict(x=range(0,len(d_arr["raw_bins"][0])), 
                             y=d_arr["raw_bins"][0]))
source_roll2 = CDS(data=dict(x=range(0,len(d_arr["raw_bins"][1])), 
                             y=d_arr["raw_bins"][1]))
source_roll3 = CDS(data=dict(x=range(0,len(d_arr["raw_bins"][2])), 
                             y=d_arr["raw_bins"][2]))
source_roll4 = CDS(data=dict(x=range(0,len(d_arr["raw_bins"][3])), 
                             y=d_arr["raw_bins"][3]))
source_roll5 = CDS(data=dict(x=range(0,len(d_arr["raw_bins"][4])), 
                             y=d_arr["raw_bins"][4]))
source_roll6 = CDS(data=dict(x=range(0,len(d_arr["raw_bins"][5])), 
                             y=d_arr["raw_bins"][5]))
source_roll7 = CDS(data=dict(x=[], y=[]))
source_roll8 = CDS(data=dict(x=[], y=[]))
source_roll9 = CDS(data=dict(x=[], y=[]))
source_roll10 = CDS(data=dict(x=[], y=[]))
source_pbe = CDS(data=dict(x=d_pbe["raw_bins"][:, 0], 
                           y=d_pbe["raw_bins"][:, 1]/2,
                           yh=d_pbe["raw_bins"][:, 1]))
source_pbe_mean = CDS(data=dict(x=[d_pbe["means"], d_pbe["means"]],
                                y=[0, maxval_pbe]))
# Associating the sources with a line on a plot
plot_raw.line('x', 'y', source=source_roll1, line_width=4, line_alpha=0.6,
              line_color='black')
plot_raw.line('x', 'y', source=source_roll2, line_width=4, line_alpha=0.6,
              line_color='blue')
plot_raw.line('x', 'y', source=source_roll3, line_width=4, line_alpha=0.6,
              line_color='orange')
plot_raw.line('x', 'y', source=source_roll4, line_width=4, line_alpha=0.6,
              line_color='green')
plot_raw.line('x', 'y', source=source_roll5, line_width=4, line_alpha=0.6,
              line_color='red')
plot_raw.line('x', 'y', source=source_roll6, line_width=4, line_alpha=0.6,
              line_color='purple')
plot_raw.line('x', 'y', source=source_roll7, line_width=4, line_alpha=0.6,
              line_color='olive')
plot_raw.line('x', 'y', source=source_roll8, line_width=4, line_alpha=0.6,
              line_color='yellow')
plot_raw.line('x', 'y', source=source_roll9, line_width=4, line_alpha=0.6,
              line_color='sienna')
plot_raw.line('x', 'y', source=source_roll10, line_width=4, line_alpha=0.6,
              line_color='grey')
plot_pbe.rect('x', 'y', width = 1, height='yh', source=source_pbe,
              fill_color="blue")
plot_pbe.line('x', 'y', source=source_pbe_mean, line_width=4, line_alpha=0.6,
              line_color='orange')
# Defining the x and y ranges objects for the plots
d_rawr, d_pber = find_ranges(d_arr, d_pbe)
xrange_raw = Range1d(bounds=[0, None], start=d_rawr[0], end=d_rawr[1])
yrange_raw = Range1d(bounds=[0, 1], start=d_rawr[2], end=d_rawr[3])
xrange_pbe = Range1d(bounds=[None, None], start=d_pber[0], end=d_pber[1])
yrange_pbe = Range1d(bounds=[0, 1], start=d_pber[2], end=d_pber[3])
# Associating the ranges with each of the previously-defined plots
plot_raw.x_range = xrange_raw
plot_raw.y_range = yrange_raw
plot_pbe.x_range = xrange_pbe
plot_pbe.y_range = yrange_pbe
# Updating the data tables
raw_m = [str(round(x,2)) for x in d_arr["means"]]
raw_s = [str(round(x,2)) for x in d_arr["stds"]]
raw_5 = [str(int(x)) for x in d_arr["5percentile"]]
raw_95 = [str(int(x)) for x in d_arr["95percentile"]]
pbe_m = [str(round(d_pbe["means"],2))]
pbe_s = [str(round(d_pbe["stds"],2))]
pbe_5 = [str(round(d_pbe["5percentile"],2))]
pbe_95 = [str(round(d_pbe["95percentile"],2))]
source_dt_raw.data = dict(mvs=raw_m, stds=raw_s, p5=raw_5, p95=raw_95)
source_dt_pbe.data = dict(mvs=pbe_m, stds=pbe_s, p5=pbe_5, p95=pbe_95)
# Labels
label_fpb = Label(text="Fair Point Buy:3", x=70, y=280, 
                  x_units='screen', y_units='screen')
plot_pbe.add_layout(label_fpb)

###-----------------------------------------------------------------------###
###----------------------------CALLBACKS----------------------------------###
### This section defines the behavior of the GUI as the user interacts    ###
### with the controls.                                                    ###
###-----------------------------------------------------------------------###
# Behavior when the "Simulate" button is clicked    
def update_plot():
    # Pulling the values from each of the controls
    num_dice = up_nd.value
    dice_type = up_dt.value
    keep_dice = up_kd.value
    add_val = up_av.value
    num_attr = up_na.value
    keep_attr = up_ka.value
    reroll = up_rr.value
    num_arrays = up_nar.value
    num_hist = up_hi.value
    pbe_map = d_ss[up_sys.active]
    roll_low_limit = up_rl.value
    roll_high_limit = up_rh.value
    pbe_low_limit = up_pl.value
    pbe_high_limit = up_ph.value
    # Use the far end of the scales in the sliders indicates no limit
    if roll_low_limit == 1:
        roll_low_limit = None
    if roll_high_limit == 20:
        roll_high_limit = None    
    if pbe_low_limit == -21:
        pbe_low_limit = None
    if pbe_high_limit == 61:
        pbe_high_limit = None          
    # Update Sources. This code is awful. There's got to be a better way to
    # do this, but having to support between 1-8 lines seems difficult with
    # Bokeh.
    arr_res, pbe_res, txt = sim(num_dice, dice_type, keep_dice, add_val, 
                                num_attr, keep_attr, reroll, num_arrays, 
                                num_hist, pbe_map, roll_low_limit,
                                roll_high_limit, pbe_low_limit, pbe_high_limit)
    maxval_pbe2 = 1.05 * max(pbe_res["raw_bins"][:, 1])
    # This code hurt me to write, emotionally
    if len(arr_res["raw_bins"])>0:
        source_roll1.data = dict(x=range(0,len(arr_res["raw_bins"][0])), 
                                 y=arr_res["raw_bins"][0])
    else:
        source_roll1.data = dict(x=[], y=[])
    if len(arr_res["raw_bins"])>1:
        source_roll2.data = dict(x=range(0,len(arr_res["raw_bins"][1])), 
                                 y=arr_res["raw_bins"][1])
    else:
        source_roll2.data = dict(x=[], y=[])
    if len(arr_res["raw_bins"])>2:    
        source_roll3.data = dict(x=range(0,len(arr_res["raw_bins"][2])), 
                                 y=arr_res["raw_bins"][2])
    else:
        source_roll3.data = dict(x=[], y=[])    
    if len(arr_res["raw_bins"])>3:     
        source_roll4.data = dict(x=range(0,len(arr_res["raw_bins"][3])), 
                                 y=arr_res["raw_bins"][3])
    else:
        source_roll4.data = dict(x=[], y=[]) 
    if len(arr_res["raw_bins"])>4:             
        source_roll5.data = dict(x=range(0,len(arr_res["raw_bins"][4])), 
                                 y=arr_res["raw_bins"][4])
    else:
        source_roll5.data = dict(x=[], y=[]) 
    if len(arr_res["raw_bins"])>5:    
        source_roll6.data = dict(x=range(0,len(arr_res["raw_bins"][5])), 
                                 y=arr_res["raw_bins"][5])
    else:
        source_roll6.data = dict(x=[], y=[]) 
    if len(arr_res["raw_bins"])>6:    
        source_roll7.data = dict(x=range(0,len(arr_res["raw_bins"][6])), 
                                 y=arr_res["raw_bins"][6])
    else:
        source_roll7.data = dict(x=[], y=[]) 
    if len(arr_res["raw_bins"])>7:         
        source_roll8.data = dict(x=range(0,len(arr_res["raw_bins"][7])), 
                                 y=arr_res["raw_bins"][7])
    else:
        source_roll8.data = dict(x=[], y=[]) 
    if len(arr_res["raw_bins"])>8:         
        source_roll9.data = dict(x=range(0,len(arr_res["raw_bins"][8])), 
                                 y=arr_res["raw_bins"][8])
    else:
        source_roll9.data = dict(x=[], y=[]) 
    if len(arr_res["raw_bins"])>9:         
        source_roll10.data = dict(x=range(0,len(arr_res["raw_bins"][9])), 
                                 y=arr_res["raw_bins"][9])
    else:
        source_roll10.data = dict(x=[], y=[])      
    # Back to clean(er) code again
    source_pbe.data = dict(x=pbe_res["raw_bins"][:, 0], 
                           y=pbe_res["raw_bins"][:, 1]/2,
                           yh=pbe_res["raw_bins"][:, 1])
    source_pbe_mean.data = dict(x=[pbe_res["means"], pbe_res["means"]],
                                y=[0, maxval_pbe2])
    # Update the ranges
    rawr, pber = find_ranges(arr_res, pbe_res)
    xrange_raw.start, xrange_raw.end = rawr[0], rawr[1]
    yrange_raw.start, yrange_raw.end = rawr[2], rawr[3]
    xrange_pbe.start, xrange_pbe.end = pber[0], pber[1]
    yrange_pbe.start, yrange_pbe.end = pber[2], pber[3]
    # Update the data tables
    raw_m = [round(x,2) for x in arr_res["means"]]
    raw_s = [round(x,2) for x in arr_res["stds"]]
    raw_5 = [round(x,2) for x in arr_res["5percentile"]]
    raw_95 = [round(x,2) for x in arr_res["95percentile"]]
    pbe_m = [round(pbe_res["means"],2)]
    pbe_s = [round(pbe_res["stds"],2)]
    pbe_5 = [round(pbe_res["5percentile"],2)]
    pbe_95 = [round(pbe_res["95percentile"],2)]
    source_dt_raw.data = dict(mvs=raw_m, stds=raw_s, p5=raw_5, p95=raw_95)
    source_dt_pbe.data = dict(mvs=pbe_m, stds=pbe_s, p5=pbe_5, p95=pbe_95)
    # Update the labels
    label_fpb.text = "Fair Point Buy:{}".format(int(round(pbe_m[0])))

# Behavior when the "Clear" button is clicked
def clear_plot():
    # Remove all the data from the plots
    source_roll1.data = dict(x=[], y=[])
    source_roll2.data = dict(x=[], y=[])
    source_roll3.data = dict(x=[], y=[])
    source_roll4.data = dict(x=[], y=[])
    source_roll5.data = dict(x=[], y=[])
    source_roll6.data = dict(x=[], y=[])
    source_roll7.data = dict(x=[], y=[])
    source_roll8.data = dict(x=[], y=[])
    source_roll9.data = dict(x=[], y=[])
    source_roll10.data = dict(x=[], y=[])
    source_pbe.data = dict(x=[], y=[], yh=[])
    source_pbe_mean.data = dict(x=[], y=[])
    # Return the ranges to normal
    xrange_raw.start = 0
    xrange_raw.end = 18
    yrange_raw.start = 0
    yrange_raw.end = 1
    xrange_pbe.start = 0
    xrange_pbe.end = 1
    yrange_pbe.start = 0
    yrange_pbe.end = 1
    # Clear the data tables
    source_dt_raw.data = dict(mvs=[], stds=[], p5=[], p95=[])
    source_dt_pbe.data = dict(mvs=[], stds=[], p5=[], p95=[])

# Button callbacks, using the above functions
plot_sim.on_click(update_plot)
plot_clear.on_click(clear_plot)

# Download the raw rolls data
js_raw = CustomJS(args=dict(source=source_dt_raw), code="""
            var data = source.get('data');
            var filetext = 'mean,std,5 perc,95 perc\\n';
            for (i=0; i < data['mvs'].length; i++) {
                var currRow = [data['mvs'][i].toString(),
                              data['stds'][i].toString(),
                              data['p5'][i].toString(),
                              data['p95'][i].toString().concat('\\n')];

                var joined = currRow.join();
                filetext = filetext.concat(joined);
            }

            var filename = 'raw_stats.csv';
            var blob = new Blob([filetext], { type: 'text/csv;charset=utf-8;' });

            //addresses IE
            if (navigator.msSaveBlob) {
                navigator.msSaveBlob(blob, filename);
            }

            else {
                var link = document.createElement("a");
                link = document.createElement('a')
                link.href = URL.createObjectURL(blob);
                link.download = filename
                link.target = "_blank";
                link.style.visibility = 'hidden';
                link.dispatchEvent(new MouseEvent('click'))
            }
        """)
but_raw = Button(label='Download Table', button_type='success', callback=js_raw)

# Download the pbe data
js_pbe = CustomJS(args=dict(source=source_dt_pbe), code="""
            var data = source.get('data');
            var filetext = 'mean,std,5 perc,95 perc\\n';
            for (i=0; i < data['mvs'].length; i++) {
                var currRow = [data['mvs'][i].toString(),
                              data['stds'][i].toString(),
                              data['p5'][i].toString(),
                              data['p95'][i].toString().concat('\\n')];

                var joined = currRow.join();
                filetext = filetext.concat(joined);
            }

            var filename = 'pbe_stats.csv';
            var blob = new Blob([filetext], { type: 'text/csv;charset=utf-8;' });

            //addresses IE
            if (navigator.msSaveBlob) {
                navigator.msSaveBlob(blob, filename);
            }

            else {
                var link = document.createElement("a");
                link = document.createElement('a')
                link.href = URL.createObjectURL(blob);
                link.download = filename
                link.target = "_blank";
                link.style.visibility = 'hidden';
                link.dispatchEvent(new MouseEvent('click'))
            }
        """)
but_pbe = Button(label='Download Table', button_type='success', callback=js_pbe)

###-----------------------------------------------------------------------###
###----------------------------PAGE LAYOUT--------------------------------###
### This section defines the basic layout of the GUI.                     ###
###-----------------------------------------------------------------------###
col_inputs = column(plot_ctls, up_ctls)
col_plots = column(plot_console, plot_raw, plot_pbe)
col_dts = column(dt_raw_title, but_raw, dt_raw, dt_pbe_title, but_pbe, dt_pbe)
row_page = row(col_inputs, col_plots, col_dts, width=1600)
curdoc().add_root(row_page)
curdoc().title = "Point Buy Equivalent Simulator (Powered by PyPBE)"