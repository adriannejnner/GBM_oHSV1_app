 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='rhostar_virus', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.rhostar_virus = FloatText(
          value=268.51,
          step=10,
          style=style, layout=widget_layout)

        param_name3 = Button(description='V0', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.V0 = FloatText(
          value=3.0248,
          step=0.1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='u_g', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.u_g = FloatText(
          value=0.002,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='m_half', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.m_half = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='gamma', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.gamma = FloatText(
          value=0.0081,
          step=0.001,
          style=style, layout=widget_layout)

        param_name7 = Button(description='alpha', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.alpha = FloatText(
          value=6600,
          step=100,
          style=style, layout=widget_layout)

        param_name8 = Button(description='rho_max', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.rho_max = FloatText(
          value=0.0125,
          step=0.001,
          style=style, layout=widget_layout)

        param_name9 = Button(description='delta_V', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.delta_V = FloatText(
          value=0.1466,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='R_cell_GBM', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.R_cell_GBM = FloatText(
          value=10.75,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='V_N_GBM', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.V_N_GBM = FloatText(
          value=740,
          step=10,
          style=style, layout=widget_layout)

        param_name12 = Button(description='N_GBM_sparse', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.N_GBM_sparse = IntText(
          value=5580,
          step=100,
          style=style, layout=widget_layout)

        param_name13 = Button(description='N_GBM_dense', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.N_GBM_dense = IntText(
          value=12556,
          step=1000,
          style=style, layout=widget_layout)

        param_name14 = Button(description='beta', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.beta = FloatText(
          value=0.000735,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name15 = Button(description='R_cell_stroma', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'tan'

        self.R_cell_stroma = FloatText(
          value=7.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='V_N_stroma', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'lightgreen'

        self.V_N_stroma = FloatText(
          value=500,
          step=10,
          style=style, layout=widget_layout)

        param_name17 = Button(description='N_stroma_sparse', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'tan'

        self.N_stroma_sparse = IntText(
          value=14306,
          step=1000,
          style=style, layout=widget_layout)

        param_name18 = Button(description='N_stroma_dense', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'lightgreen'

        self.N_stroma_dense = IntText(
          value=2861,
          step=100,
          style=style, layout=widget_layout)

        param_name19 = Button(description='u_s', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'tan'

        self.u_s = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='R_cell_CD4_CD8', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'lightgreen'

        self.R_cell_CD4_CD8 = FloatText(
          value=3.6,
          step=0.1,
          style=style, layout=widget_layout)

        param_name21 = Button(description='V_N_CD4', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'tan'

        self.V_N_CD4 = FloatText(
          value=95.21,
          step=1,
          style=style, layout=widget_layout)

        param_name22 = Button(description='V_N_CD8', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'lightgreen'

        self.V_N_CD8 = FloatText(
          value=96.23,
          step=1,
          style=style, layout=widget_layout)

        param_name23 = Button(description='nu', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'tan'

        self.nu = FloatText(
          value=4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name24 = Button(description='nu_max', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'lightgreen'

        self.nu_max = FloatText(
          value=24.6,
          step=1,
          style=style, layout=widget_layout)

        param_name25 = Button(description='nu_star', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'tan'

        self.nu_star = FloatText(
          value=0.005,
          step=0.001,
          style=style, layout=widget_layout)

        param_name26 = Button(description='b_CD8', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'lightgreen'

        self.b_CD8 = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name27 = Button(description='S_chemokine_CD4', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'tan'

        self.S_chemokine_CD4 = FloatText(
          value=0.0417,
          step=0.01,
          style=style, layout=widget_layout)

        param_name28 = Button(description='r_01_CD4', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'lightgreen'

        self.r_01_CD4 = FloatText(
          value=0.000079026,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name29 = Button(description='r_01_CD8', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'tan'

        self.r_01_CD8 = FloatText(
          value=0.000072206,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name30 = Button(description='r_10', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'lightgreen'

        self.r_10 = FloatText(
          value=0.00143,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name31 = Button(description='TH_prolif_increase_due_to_stimulus', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'tan'

        self.TH_prolif_increase_due_to_stimulus = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name32 = Button(description='CTL_prolif_increase_due_to_stimulus', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'lightgreen'

        self.CTL_prolif_increase_due_to_stimulus = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name33 = Button(description='d_attach', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'tan'

        self.d_attach = FloatText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name34 = Button(description='rhostar_chemokine', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'lightgreen'

        self.rhostar_chemokine = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name35 = Button(description='tau', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'tan'

        self.tau = FloatText(
          value=50,
          step=1,
          style=style, layout=widget_layout)

        param_name36 = Button(description='R', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'lightgreen'

        self.R = FloatText(
          value=1270,
          step=100,
          style=style, layout=widget_layout)

        param_name37 = Button(description='kappa', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'tan'

        self.kappa = FloatText(
          value=1.208,
          step=0.1,
          style=style, layout=widget_layout)

        param_name38 = Button(description='proportion', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'lightgreen'

        self.proportion = FloatText(
          value=0.7,
          step=0.1,
          style=style, layout=widget_layout)

        param_name39 = Button(description='xi', disabled=True, layout=name_button_layout)
        param_name39.style.button_color = 'tan'

        self.xi = FloatText(
          value=0.0039,
          step=0.001,
          style=style, layout=widget_layout)

        param_name40 = Button(description='f_F', disabled=True, layout=name_button_layout)
        param_name40.style.button_color = 'lightgreen'

        self.f_F = FloatText(
          value=0.75,
          step=0.1,
          style=style, layout=widget_layout)

        param_name41 = Button(description='elastic_coefficient', disabled=True, layout=name_button_layout)
        param_name41.style.button_color = 'tan'

        self.elastic_coefficient = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='virus/micron', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='virus', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='virus', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='virus', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='micron^3', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='cells', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='cells', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'tan'
        units_button16 = Button(description='micron^3', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'lightgreen'
        units_button17 = Button(description='cells', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'tan'
        units_button18 = Button(description='cells', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'lightgreen'
        units_button19 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'tan'
        units_button20 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'lightgreen'
        units_button21 = Button(description='micron^3', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'tan'
        units_button22 = Button(description='micron^3', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'lightgreen'
        units_button23 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'tan'
        units_button24 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'lightgreen'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'tan'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'lightgreen'
        units_button27 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'tan'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'lightgreen'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'tan'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'lightgreen'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'tan'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'lightgreen'
        units_button33 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'tan'
        units_button34 = Button(description='ng/micron', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'lightgreen'
        units_button35 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'tan'
        units_button36 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'lightgreen'
        units_button37 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'tan'
        units_button38 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'lightgreen'
        units_button39 = Button(description='cell/micron', disabled=True, layout=units_button_layout) 
        units_button39.style.button_color = 'tan'
        units_button40 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button40.style.button_color = 'lightgreen'
        units_button41 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button41.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button16 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'
        desc_button39 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button39.style.button_color = 'lightgreen'
        desc_button40 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button40.style.button_color = 'tan'
        desc_button41 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button41.style.button_color = 'lightgreen'
        desc_button42 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button42.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.rhostar_virus, units_button2, desc_button2] 
        row3 = [param_name3, self.V0, units_button3, desc_button3] 
        row4 = [param_name4, self.u_g, units_button4, desc_button4] 
        row5 = [param_name5, self.m_half, units_button5, desc_button5] 
        row6 = [param_name6, self.gamma, units_button6, desc_button6] 
        row7 = [param_name7, self.alpha, units_button7, desc_button7] 
        row8 = [param_name8, self.rho_max, units_button8, desc_button8] 
        row9 = [param_name9, self.delta_V, units_button9, desc_button9] 
        row10 = [param_name10, self.R_cell_GBM, units_button10, desc_button10] 
        row11 = [param_name11, self.V_N_GBM, units_button11, desc_button11] 
        row12 = [param_name12, self.N_GBM_sparse, units_button12, desc_button12] 
        row13 = [param_name13, self.N_GBM_dense, units_button13, desc_button13] 
        row14 = [param_name14, self.beta, units_button14, desc_button14] 
        row16 = [param_name15, self.R_cell_stroma, units_button15, desc_button16] 
        row17 = [param_name16, self.V_N_stroma, units_button16, desc_button17] 
        row18 = [param_name17, self.N_stroma_sparse, units_button17, desc_button18] 
        row19 = [param_name18, self.N_stroma_dense, units_button18, desc_button19] 
        row20 = [param_name19, self.u_s, units_button19, desc_button20] 
        row21 = [param_name20, self.R_cell_CD4_CD8, units_button20, desc_button21] 
        row22 = [param_name21, self.V_N_CD4, units_button21, desc_button22] 
        row23 = [param_name22, self.V_N_CD8, units_button22, desc_button23] 
        row24 = [param_name23, self.nu, units_button23, desc_button24] 
        row25 = [param_name24, self.nu_max, units_button24, desc_button25] 
        row26 = [param_name25, self.nu_star, units_button25, desc_button26] 
        row27 = [param_name26, self.b_CD8, units_button26, desc_button27] 
        row28 = [param_name27, self.S_chemokine_CD4, units_button27, desc_button28] 
        row29 = [param_name28, self.r_01_CD4, units_button28, desc_button29] 
        row30 = [param_name29, self.r_01_CD8, units_button29, desc_button30] 
        row31 = [param_name30, self.r_10, units_button30, desc_button31] 
        row32 = [param_name31, self.TH_prolif_increase_due_to_stimulus, units_button31, desc_button32] 
        row33 = [param_name32, self.CTL_prolif_increase_due_to_stimulus, units_button32, desc_button33] 
        row34 = [param_name33, self.d_attach, units_button33, desc_button34] 
        row35 = [param_name34, self.rhostar_chemokine, units_button34, desc_button35] 
        row36 = [param_name35, self.tau, units_button35, desc_button36] 
        row37 = [param_name36, self.R, units_button36, desc_button37] 
        row38 = [param_name37, self.kappa, units_button37, desc_button38] 
        row39 = [param_name38, self.proportion, units_button38, desc_button39] 
        row40 = [param_name39, self.xi, units_button39, desc_button40] 
        row41 = [param_name40, self.f_F, units_button40, desc_button41] 
        row42 = [param_name41, self.elastic_coefficient, units_button41, desc_button42] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)
        box40 = Box(children=row40, layout=box_layout)
        box41 = Box(children=row41, layout=box_layout)
        box42 = Box(children=row42, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          box38,
          box39,
          box40,
          box41,
          box42,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.rhostar_virus.value = float(uep.find('.//rhostar_virus').text)
        self.V0.value = float(uep.find('.//V0').text)
        self.u_g.value = float(uep.find('.//u_g').text)
        self.m_half.value = float(uep.find('.//m_half').text)
        self.gamma.value = float(uep.find('.//gamma').text)
        self.alpha.value = float(uep.find('.//alpha').text)
        self.rho_max.value = float(uep.find('.//rho_max').text)
        self.delta_V.value = float(uep.find('.//delta_V').text)
        self.R_cell_GBM.value = float(uep.find('.//R_cell_GBM').text)
        self.V_N_GBM.value = float(uep.find('.//V_N_GBM').text)
        self.N_GBM_sparse.value = int(uep.find('.//N_GBM_sparse').text)
        self.N_GBM_dense.value = int(uep.find('.//N_GBM_dense').text)
        self.beta.value = float(uep.find('.//beta').text)
        self.R_cell_stroma.value = float(uep.find('.//R_cell_stroma').text)
        self.V_N_stroma.value = float(uep.find('.//V_N_stroma').text)
        self.N_stroma_sparse.value = int(uep.find('.//N_stroma_sparse').text)
        self.N_stroma_dense.value = int(uep.find('.//N_stroma_dense').text)
        self.u_s.value = float(uep.find('.//u_s').text)
        self.R_cell_CD4_CD8.value = float(uep.find('.//R_cell_CD4_CD8').text)
        self.V_N_CD4.value = float(uep.find('.//V_N_CD4').text)
        self.V_N_CD8.value = float(uep.find('.//V_N_CD8').text)
        self.nu.value = float(uep.find('.//nu').text)
        self.nu_max.value = float(uep.find('.//nu_max').text)
        self.nu_star.value = float(uep.find('.//nu_star').text)
        self.b_CD8.value = float(uep.find('.//b_CD8').text)
        self.S_chemokine_CD4.value = float(uep.find('.//S_chemokine_CD4').text)
        self.r_01_CD4.value = float(uep.find('.//r_01_CD4').text)
        self.r_01_CD8.value = float(uep.find('.//r_01_CD8').text)
        self.r_10.value = float(uep.find('.//r_10').text)
        self.TH_prolif_increase_due_to_stimulus.value = float(uep.find('.//TH_prolif_increase_due_to_stimulus').text)
        self.CTL_prolif_increase_due_to_stimulus.value = float(uep.find('.//CTL_prolif_increase_due_to_stimulus').text)
        self.d_attach.value = float(uep.find('.//d_attach').text)
        self.rhostar_chemokine.value = float(uep.find('.//rhostar_chemokine').text)
        self.tau.value = float(uep.find('.//tau').text)
        self.R.value = float(uep.find('.//R').text)
        self.kappa.value = float(uep.find('.//kappa').text)
        self.proportion.value = float(uep.find('.//proportion').text)
        self.xi.value = float(uep.find('.//xi').text)
        self.f_F.value = float(uep.find('.//f_F').text)
        self.elastic_coefficient.value = float(uep.find('.//elastic_coefficient').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//rhostar_virus').text = str(self.rhostar_virus.value)
        uep.find('.//V0').text = str(self.V0.value)
        uep.find('.//u_g').text = str(self.u_g.value)
        uep.find('.//m_half').text = str(self.m_half.value)
        uep.find('.//gamma').text = str(self.gamma.value)
        uep.find('.//alpha').text = str(self.alpha.value)
        uep.find('.//rho_max').text = str(self.rho_max.value)
        uep.find('.//delta_V').text = str(self.delta_V.value)
        uep.find('.//R_cell_GBM').text = str(self.R_cell_GBM.value)
        uep.find('.//V_N_GBM').text = str(self.V_N_GBM.value)
        uep.find('.//N_GBM_sparse').text = str(self.N_GBM_sparse.value)
        uep.find('.//N_GBM_dense').text = str(self.N_GBM_dense.value)
        uep.find('.//beta').text = str(self.beta.value)
        uep.find('.//R_cell_stroma').text = str(self.R_cell_stroma.value)
        uep.find('.//V_N_stroma').text = str(self.V_N_stroma.value)
        uep.find('.//N_stroma_sparse').text = str(self.N_stroma_sparse.value)
        uep.find('.//N_stroma_dense').text = str(self.N_stroma_dense.value)
        uep.find('.//u_s').text = str(self.u_s.value)
        uep.find('.//R_cell_CD4_CD8').text = str(self.R_cell_CD4_CD8.value)
        uep.find('.//V_N_CD4').text = str(self.V_N_CD4.value)
        uep.find('.//V_N_CD8').text = str(self.V_N_CD8.value)
        uep.find('.//nu').text = str(self.nu.value)
        uep.find('.//nu_max').text = str(self.nu_max.value)
        uep.find('.//nu_star').text = str(self.nu_star.value)
        uep.find('.//b_CD8').text = str(self.b_CD8.value)
        uep.find('.//S_chemokine_CD4').text = str(self.S_chemokine_CD4.value)
        uep.find('.//r_01_CD4').text = str(self.r_01_CD4.value)
        uep.find('.//r_01_CD8').text = str(self.r_01_CD8.value)
        uep.find('.//r_10').text = str(self.r_10.value)
        uep.find('.//TH_prolif_increase_due_to_stimulus').text = str(self.TH_prolif_increase_due_to_stimulus.value)
        uep.find('.//CTL_prolif_increase_due_to_stimulus').text = str(self.CTL_prolif_increase_due_to_stimulus.value)
        uep.find('.//d_attach').text = str(self.d_attach.value)
        uep.find('.//rhostar_chemokine').text = str(self.rhostar_chemokine.value)
        uep.find('.//tau').text = str(self.tau.value)
        uep.find('.//R').text = str(self.R.value)
        uep.find('.//kappa').text = str(self.kappa.value)
        uep.find('.//proportion').text = str(self.proportion.value)
        uep.find('.//xi').text = str(self.xi.value)
        uep.find('.//f_F').text = str(self.f_F.value)
        uep.find('.//elastic_coefficient').text = str(self.elastic_coefficient.value)
