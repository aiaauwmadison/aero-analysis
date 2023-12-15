from math import sqrt, sin, pi
import variable_importer
# import sympy
import importlib
importlib.reload(variable_importer)

# TO-DO
# - add versioned naming to output.tex files
# - figure out if \SI{10}{ft/s} is corect or if there is an english equivalent command for \SI{}{}
# - rename variable_importer to var_importer
# - move as many variable imports to ork over user input
# - make the variables into a data structure
# - functionize the code to make error finding easier and program more readable
# - fix naming confusion such as V_m for v main and V_max for flutter, and g grave and G Shear modulus
# - add spaces before and after {} to make better formatting
# - move rounding to the string conversion lines
# - add proofs for every equation
# - add comments for readability and variable understanding
# - add divergence velocity
# - add primary and bakcup ejection charge calculations with a % modifier input for backup
# - rewrite symbolic equations without \cdot s
# - add metric converter
# - Add latex visualizer
# - add full legends to all calculations like with fin flutter
# - enclose units with [] like EES
# - add calcs for vent hole size and burnout deceleration force  
# - make air densities relative to temperature at location
# - add an import for desired drogue and main descent velocities and out put the required parachute diameters
# - Add customizable graphing from OR simulation data
# - change equation lags to labels so they can be referenced elseqhere in the document
# - ChatGPT feedback
#     - Use of Boldface for Section Headers: It's not common to use boldface text in the align* environment. You might want to move your section header "Fin Geometry Calculations" outside the align* environment. A \paragraph or \subsubsection command could work well here.
#     - Spacing Between Equations: You're using double backslashes \\ \\ for extra space between certain groups of equations. It's not incorrect, but \bigskip, \medskip, or \smallskip commands can be used to adjust the vertical space in a more controlled way.
#     - Equation Tagging: In the align* environment, the \tag command won't work as expected because the align* environment suppresses numbering. If you want to manually number some equations as in your code, use the align environment instead.
#     - Spacing Around & Symbols: In align environments, it's common to use a single & symbol to denote alignment points, and spacing is typically not placed around the &. For example: \text{Root Chord Length:} & c_{r} =\SI{12.0}{in}.
#     - Alignment of Comments: It's a good practice to align your LaTeX comments at the same indentation level for readability.

# - find actual engineering/physics book references for all the equations
# - check units of all calculations in EES, matlab, or OS equivalent
# - create an auto run github grabber
# - implement a python library for mathematics to simplify operations


author, c_r, c_t, FT, b, G, h_g, h_relVmax, m, v_i, v_f, t_infl, V_max, Cd_m, D_m, rho_m, Cd_d, rho_d, D_d, D_a, L_Dbay, L_Mbay, P_e = variable_importer.run()

# Flutter Calculations
S = (1/2)*(c_r + c_t)*b
AR = b**2/S                    
taper = c_t/c_r
h_Vmax = h_g + h_relVmax
T = 59 - 0.00356*h_Vmax
P_0 = 14.69
P = P_0*((T+459.7)/518.6)** 5.256
a = sqrt(1.4*1716.59*(T+460))
V_fl = sqrt(G/(((39.3*(AR**3))/(((FT/c_r) ** 3)*(AR+2))) * ((taper+1)/2) * (P/P_0))) * a
SM = V_fl / V_max
grav = 32.17
chute_F_max = ((2*m*v_i)/(grav * T))*(1 + (v_i/v_f)) + 2*m
V_d = sqrt((8*m*grav)/(pi*rho_d*Cd_d*D_d**2))
V_m = sqrt((8*m*grav)/(pi*rho_m*Cd_m*D_m**2))
Vol_d = (pi*D_a**2*L_Dbay)/4
Vol_m = (pi*D_a**2*L_Mbay)/4
# Update below with actual vars
m_bp_d = (454*P_e*Vol_d)/(265.92*3307)
m_bp_m = (454*P_e*Vol_m)/(265.92*3307)
A_bh = (pi * D_a**2)/4
F_e = P_e * A_bh
P_e_d = (2.5*265.92*3307)/(Vol_d * 454) 
P_e_m = (5*265.92*3307)/(Vol_m * 454) 
F_e_d = P_e_d * A_bh
F_e_m = P_e_m * A_bh

# convert float vars to string
c_r_str = str(round(c_r, 2))
c_t_str = str(round(c_t, 2))
FT_str = str(round(FT, 2))
G_str = str(round(G, 2))
b_str = str(round(b, 2))
S_str = str(round(S, 2))
b_str = str(round(b, 2))
AR_str = str(round(AR, 3))
taper_str = str(round(taper, 2))
P_0_str = str(round(P_0, 2))
h_g_str = str(round(h_g, 2))
h_relVmax_str = str(round(h_relVmax, 2))
h_Vmax_str =str(round(h_Vmax, 2))
T_str = str(round(T, 2))
P_str = str(round(P, 2))
a_str = str(round(a, 2))
V_max_str = str(round(V_max, 2))
V_fl_str = str(round(V_fl, 2))
SM_str = str(round(SM, 2))
D_d_str = str(round(D_d, 2))
Cd_d_str = str(round(Cd_d, 2))
rho_d_str = str(round(rho_d, 2)) 
D_m_str = str(round(D_m, 2))
Cd_m_str = str(round(Cd_m, 2))
rho_m_str = str(round(rho_m, 2))
m_str = str(round(m, 2))
grav_str = str(round(grav, 2))
V_d_str = str(round(V_d, 2))
V_m_str = str(round(V_m,  2))
D_a_str = str(round(D_a, 2))
A_bh_str = str(round(A_bh, 2))
F_e_str = str(round(F_e, 2))
L_Dbay_str = str(round(L_Dbay, 2))
L_Mbay_str = str(round(L_Mbay, 2))
Vol_d_str = str(round(Vol_d, 2))
Vol_m_str = str(round(Vol_m, 2))
P_e_str = str(round(P_e, 2))
m_bp_d_str = str(round(m_bp_d, 2))
m_bp_m_str = str(round(m_bp_m, 2))
P_e_d_str = str(round(P_e_d, 2))
F_e_d_str = str(round(F_e_d, 2))
P_e_m_str = str(round(P_e_m, 2))
F_e_m_str = str(round(F_e_m, 2))
v_i_str = str(round(v_i, 2))
v_f_str = str(round(v_f, 2))
t_infl_str = str(round(t_infl, 2))
chute_F_max_str = str(round(chute_F_max, 2))


latex = ''
values = {"b_str": b_str, "S_str": S_str}

latex2 =r''
latex2 += r'&& &= \frac{\left( %(b_str)s \right)^2}{\SI{ %(S_str)s }{in^2}} \\' % values  + '\n\t\t'
print(latex2)

# add author variable to ork_importer

# document header
latex += r'\documentclass{article}' + '\n'
latex += r'\title{Fin Flutter Analysis}' + '\n'
latex += r'\author{' + author + '}' + '\n'
latex += r'\date{\today}' + '\n\n'

# latex += r'&& &= \frac{\left( %(b_str) \right)^2}{\SI{' + S_str + r'}{in^2}} \\' % values + '\n\t\t'

# import packages and set margins, block string format is used for simplification
latex += r'''\usepackage[group-separator={,}, group-digits=true]{siunitx}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath}
\allowdisplaybreaks''' +'\n'

latex += r'\begin{document}' + '\n\t'
latex += r'\begin{align*}' + '\n\t\t'

# Equations
# Fin Geometry Calculations Block
latex += r'% Fin Geometry Calculations Block' + '\n\t\t'
latex += r'\textbf{Fin Geometry Calculations} \\' + '\n\t\t'
latex += r'\text{Root Chord Length:}& &c_{r} &=\SI{' + c_r_str + r'}{in} \\' + '\n\t\t'
latex += r'\text{Tip Chord Length:}& &c_{t} &= \SI{' + c_t_str + r'}{in} \\' + '\n\t\t'
latex += r'\text{Fin Thickness:}& &FT &= \SI{' + FT_str + r'}{in} \\' + '\n\t\t'
latex += r'\text{Fin semi-span root to tip:}& &b &= \SI{4.75}{in} \\' + '\n\t\t'
latex += r'\text{Shear modulus of fin material (fiberglass):}& &G &= \SI{' + G_str + r'}{psi} \\' + '\n\t\t'
latex += r'\text{Fin surface area:}& &S &= \frac{1}{2} \left( c_{r} + c_{t} \right) \cdot b \tag{eqn. 1} \\' + '\n\t\t'
latex += r'&& &= \frac{1}{2} \left( ' + c_r_str + r' + ' + c_t_str + r' \right) \cdot' + b_str + r'\\' + '\n\t\t'
latex += r'&& &= \SI{' + S_str + r'}{in^2} \\ \\' + '\n\t\t'
latex += r'\text{Fin Aspect Ratio:}& &AR &= \frac{b^2}{S} \tag{eqn. 2} \\' + '\n\t\t'
latex += r'&& &= \frac{\left(' + b_str + r'\right)^2}{\SI{' + S_str + r'}{in^2}} \\' + '\n\t\t'
latex += r'&& &= ' + AR_str + r'\\ \\' + '\n\t\t'
latex += r'\text{Fin taper ratio:}& &\lambda &= \frac{c_{t}}{c_{r}} \tag{eqn. 3} \\' + '\n\t\t'
latex += r'&& &= \frac{' + c_t_str + r'}{' + c_r_str + r'} \\' + '\n\t\t'
latex += r'&& &= ' + taper_str + r'\\' + '\n\t\t'
latex += r'\\ \\' + '\n\t\t'

# Atmospheric Conditions Calculations Block
latex += r'% Atmospheric Conditions Calculations Block' + '\n\t\t'
latex += r'\textbf{Atmospheric Conditions Calculations} \\' + '\n\t\t'
latex += r'\text{Sea level atmospheric pressure:}& &P_{0} &= \SI{' + P_0_str + r'}{psi} \\' + '\n\t\t'
latex += r'\text{Altitude at launchpad:}& &h_{g} &= \SI{' + h_g_str + r'}{ft} \\' + '\n\t\t'
latex += r'\text{Altitude of max velocity relative to launchpad:}& &h_{relVmax} &= \SI{' + h_relVmax_str + r'}{ft} \\' + '\n\t\t'
latex += r'\text{Altitude of max velocity:}& &h_{Vmax} &= h_{g} + h_{relVmax} \\ \tag{eqn.4}' + '\n\t\t'
latex += r'&& &= ' + h_g_str + r' + ' + h_relVmax_str + r' \\' + '\n\t\t'
latex += r'&& &= \SI{' + h_Vmax_str + r'}{ft} \\ \\' + '\n\t\t'
latex += r'\text{Temperature at h\_Vmax:}& &T &= 59 - 0.00356 \cdot h_{Vmax} \tag{eqn. 5}\\' + '\n\t\t'
latex += r'&& &= 59 - 0.00356 \cdot ' + h_Vmax_str + r'\\' + '\n\t\t'
latex += r'&& &= \SI{' + T_str + r'}{\degree F} \\ \\' + '\n\t\t'
latex += r'\text{Pressure at h\_Vmax:}& &P &= P_{0} \cdot \left(\frac{T + 459.7}{ 518.6 }\right)^{5.256} \tag{eqn.6} \\' + '\n\t\t'
latex += r'&& &= ' + P_0_str + r'\cdot \left(\frac{' + T_str + r' + 459.7 }{ 518.6 }\right)^{5.256} \\' + '\n\t\t'
latex += r'&& &= \SI{' + P_str + r'}{psi} \\ \\' + '\n\t\t'
latex += r'\text{Speed of sound at h\_Vmax: }& &a &= \sqrt { 1.4 \cdot 1716.59 \cdot \left(T + 459.7 \right) } \tag{eqn. 7}\\'
latex += r'&& &= \sqrt { 1.4 \cdot 1716.59 \cdot \left(' + T_str + r' + 459.7 \right) } \\' + '\n\t\t'
latex += r'&& &= \SI{' + a_str + r'}{ft/s} \\ \\' + '\n\t\t'
latex += r'\\' + '\n\t\t'


# Fin Flutter Velocity Calculations
latex += r'% Fin Flutter Velocity Calculations' + '\n\t\t'
latex += r'\textbf{Fin Velocity Calculations} \\' + '\n\t\t'
latex += r'\text{Max velocity of rocket:}& &V_{max} &= \SI{' + V_max_str + r'}{ft/s} \\ \\' + '\n\t\t'
latex += r'\text{Fin flutter velocity:}& &v_{fl} &= \sqrt {\frac{ G }{\left( \frac{ 39.3 \cdot \left( AR \right) ^{ 3 } }{ \left( \frac{ FT }{ c_{r} } \right) ^{ 3 } \cdot \left( AR + 2 \right) } \right) \left( \frac{ \lambda + 1 }{ 2 } \right) \left( \frac{ P }{ P_{0} } \right) } } \cdot a \tag{eqn. 8} \\'
latex += r'&& &= \sqrt { \frac{' + G_str + r'}{ \left( \frac{ 39.3 \cdot \left(' + AR_str + r' \right) ^{ 3 } }{ \left( \frac{' + FT_str + r'}{' + c_r_str + r'} \right) ^{3} \cdot \left(' + AR_str + r' + 2 \right) } \right) \left( \frac{' + taper_str + r'+ 1 }{ 2 } \right) \left( \frac{' + P_str + r'}{' + P_0_str + r'} \right) } } \cdot ' + a_str +  r'\\'
latex += r'&& &= \SI{' + V_fl_str + '}{ft/s} ' + r'\\ \\' + '\n\t\t'
latex += r'\text{Fin flutter safety margin:}& &SM &= \frac{V_{max}}{v_{fl}} \tag{eqn. 9} \\'
latex += r'&& &= \frac{' + V_max_str + r'}{' + V_fl_str + r'} \\' + '\n\t\t'
latex += r'&& &= ' + SM_str + r'\\' + '\n\t\t'
latex += r'\\' + '\n\t\t'

# Parachute Descent Velocity Equation Proof
latex += r'% Parachute Descent Velocity Equation Proof' + '\n\t\t'
latex += r'\textbf{Parachute Descent Velocity Equation Proof} \\' + '\n\t\t'
latex += r'\text{Drag force equation:}& &F_{d} &= \frac{1}{2} \cdot \rho \cdot V^{2} \cdot c_{d} \cdot A \tag{eqn. 10} \\' + '\n\t\t'
latex += r'\text{Parachute area:}& &A &= \pi \cdot \left( \frac{D^{2}}{4} \right) \\' + '\n\t\t'
latex += r'\text{Drag force equation with D:}& &F_{d} &= \frac{1}{2} \cdot \rho \cdot V^{2} \cdot c_{d} \cdot \pi \cdot \left( \frac{D^{2}}{4} \right) \\' + '\n\t\t'
latex += r'& &\implies F_{d} &= \frac{1}{8} \cdot \rho \cdot V^{2} \cdot c_{d} \cdot \pi \cdot D^{2} \\ \\' + '\n\t\t'
latex += r'\text{Weight force equation:}& &F_{w} &= m \cdot g \\' + '\n\t\t'
latex += r'\text{Force balance of drag and weight:}& &F_{w} &= F_{d} \\' + '\n\t\t'
latex += r'&& \implies m \cdot g&= \frac{1}{8} \cdot \rho \cdot V^{2} \cdot c_{d} \cdot \pi \cdot D^{2} \tag{eqn. 11} \\ \\' + '\n\t\t'
latex += r'\text{Re-arrange force balance equation for solution:}& & V_{chute} &= \sqrt{\frac{8 \cdot m \cdot g}{\rho \cdot c_{d} \cdot \pi \cdot D^{2}}} \tag{eqn. 12} \\ \\' + '\n\t\t'

# Desccent Velocity Calculations
latex += r'% Descent Velocity Calculations' + '\n\t\t'
latex += r'\textbf{Descent Velocity Calculations} \\' + '\n\t\t'
latex += r'\text{Parachute Descent Velocity Equation:}& & V_{chute} &= \sqrt{\frac{8 \cdot m \cdot g}{\rho \cdot C_{d} \cdot \pi \cdot D^{2}}} \tag{eqn. 12} \\ \\' + '\n\t\t'
# Parachute Parameters
latex += r'% Parchute Parameters' + '\n\t\t'
latex += r'\text{Drogue Chute Diameter:}& &D_{d} &= \SI{' + D_d_str + r'}{ft} \\' + '\n\t\t'
latex += r'\text{Drogue Chute Drag Coefficient:}& &Cd_{d} &= \SI{' + Cd_d_str + r'}{} \\' + '\n\t\t'
latex += r'\text{Air density under drogue chute descent:}& &\rho_{d} &= \SI{' + rho_d_str + r'}{lbs/ft^3} \\ \\' + '\n\t\t'
latex += r'\text{Main Chute Diameter:}& &D_{m} &= \SI{' + D_m_str + r'}{ft} \\' + '\n\t\t'
latex += r'\text{Main Chute Drag Coefficient:}& &Cd_{m} &= \SI{' + Cd_m_str + r'}{} \\' + '\n\t\t'
latex += r'\text{Air density under main chute descent:}& &\rho_{m} &= \SI{' + rho_m_str + r'}{lbs/ft^3} \\ \\' + '\n\t\t'
latex += r'\text{Rocket mass after motor burnout:}& &m &= \SI{' + m_str + r'}{lbs} \\ \\' + '\n\t\t'
latex += r'\text{Gravity:}& &g &= \SI{' + grav_str + r'}{ft/s^2} \\ \\' + '\n\t\t'
# Descent Velocity Solutions
latex += r'\text{Drogue chute descent velocity:}& &V_{drogue} &= \sqrt{\frac{8 \cdot ' + m_str + r' \cdot 32.2}{\pi \cdot ' + rho_d_str + r' \cdot ' + Cd_d_str + r' \cdot ' + D_d_str + r'^{2}}} \\' + '\n\t\t'
latex += r'&& &= \SI{' + V_d_str + r'}{ft/s} \\ \\' + '\n\t\t'
latex += r'\text{Main chute descent velocity:}& &V_{main} &= \sqrt{\frac{8 \cdot ' + m_str + r' \cdot 32.2}{\pi \cdot ' + rho_m_str + r' \cdot ' + Cd_m_str + r' \cdot ' + D_m_str + r'^{2}}} \\' + '\n\t\t'
latex += r'&& &= \SI{' + V_m_str + r'}{ft/s} \\ \\' + '\n\t\t'
# latex += '\\'

# Ejection Charge Size Calculations
latex += r'% Ejection Charge Size Calculations' + '\n\t\t'
latex += r'\textbf{Ejection Charge Size Calculations} \\' + '\n\t\t'
latex += r'\text{Airframe Diameter:}& &D_{a} &= \SI{' + D_a_str + r'}{in} \\ \\' + '\n\t\t'
latex += r'\text{Bulkhead area:}& & A_{bh} &= \frac{D_{a} \cdot pi}{4} \tag{eqn. 13} \\' + '\n\t\t'
latex += r'&& &= \SI{' + A_bh_str + r'}{in^2} \\ \\' + '\n\t\t'
latex += r'\text{Force applied to bulkheads by P\_{e}:}& &F_{e} &= P_{e} \cdot A_{bh} \\' + '\n\t\t'
latex += r'&& &= \SI{' + F_e_str + r'}{lbs} \\ \\' + '\n\t\t'
latex += r'\text{Airframe Section Volume Equation:}& &Vol_{s} &= \frac{ \pi \cdot D^{2} \cdot L}{4} \tag{eqn. 14} \\ \\' + '\n\t\t'
latex += r'\text{Volume of Drogue Chute Bay:}&' + r'&Vol_{d} &= \frac{\pi \cdot ' + D_a_str + '^{2} \cdot' + L_Dbay_str + r'}{4} \\' + '\n\t\t'
latex += r'&& &= \SI{' + Vol_d_str + r'}{in^3} \\ \\' + '\n\t\t'
latex += r'\text{Volume of Main Chute Bay:}&' + r'&Vol_{m} &= \frac{\pi \cdot ' + D_a_str + '^{2} \cdot' + L_Mbay_str + r'}{4} \\' + '\n\t\t'
latex += r'&& &= \SI{' + Vol_m_str + r'}{in^3} \\ \\' + '\n\t\t'
latex += r'\text{Combustion gas constant of black powder:}& &R &= 265.92 \frac{in \cdot lbf}{lbm \cdot \SI{}{\degree R}} \\ \\' + '\n\t\t'
latex += r'\text{Combustion gas temperature of black powder:}& &T_{c} &= 3307 \: \SI{}{\degree R} \\ \\' + '\n\t\t'
latex += r'\text{Black powder charge  mass equation:}& &m_{bp} &= \frac{454 g}{1 lbf} \cdot \frac{P_{e} \cdot Vol_{s}}{265.92 \frac{in \cdot lbf}{lbm \cdot \SI{}{\degree R}} \cdot 3307 \cdot \SI{}{\degree R}} \tag{eqn. 15} \\ \\' + '\n\t\t'
latex += r'\text{Black powder charge mass for drogue chute bay:}& &m_{bp,d} &= \frac{454 g}{1 lbf} \cdot \frac{' + P_e_str + r' \cdot ' + Vol_d_str + r'}{265.92  \cdot 3307 \cdot} \\' + '\n\t\t'
latex += r'&& &= \SI{' + m_bp_d_str + r'}{g} \\ \\' + '\n\t\t'
latex += r'\text{Black powder charge mass for main chute bay: }& &m_{bp,m} &= \frac{454 g}{1 lbf} \cdot \frac{' + P_e_str + r' \cdot ' + Vol_m_str + r'}{265.92  \cdot 3307} \\' + '\n\t\t'
latex += r'&& &= \SI{' + m_bp_m_str + r'}{g} \\ \\' + '\n\t\t'

# Ejection Charge Size Calculation Reversed
latex += r'% Ejection Charge Size Calculations Reversed' + '\n\t\t'
latex += r'\textbf{Ejection Charge Size Calculations Reversed } \\' + '\n\t\t'
latex += r'\text{Airframe Diameter:}& &D_{a} &= \SI{' + D_a_str + r'}{in} \\ \\' + '\n\t\t'
latex += r'\text{Bulkhead area:}& & A_{bh} &= \frac{D_{a} \cdot \pi}{4} \tag{eqn. 13} \\' + '\n\t\t'
latex += r'&& &= \SI{' + A_bh_str + r'}{in^2} \\ \\' + '\n\t\t'
latex += r'\text{Length of Drogue Chute Bay:}&' + r'&L_{d,bay} &= \SI{' + L_Dbay_str + r'}{in} \\' + '\n\t\t'
latex += r'\text{Length of Main Chute Bay:}&' +r'&L_{m,bay} &= \SI{' + L_Mbay_str + r'}{in} \\' + '\n\t\t'
latex += r'\text{Airframe Section Volume Equation:}& &Vol_{s} &= \frac{ \pi \cdot D^{2} \cdot L}{4} \tag{eqn. 14} \\ \\' + '\n\t\t'
latex += r'\text{Volume of Drogue Chute Bay:}&' + r'&Vol_{d} &= \frac{\pi \cdot ' + D_a_str + '^{2} \cdot' + L_Dbay_str + r'}{4} \\' + '\n\t\t'
latex += r'&& &= \SI{' + Vol_d_str + r'}{in^3} \\ \\' + '\n\t\t'
latex += r'\text{Volume of Main Chute Bay:}&' + r'&Vol_{m} &= \frac{\pi \cdot ' + D_a_str + '^{2} \cdot' + L_Mbay_str + r'}{4} \\' + '\n\t\t'
latex += r'&& &= \SI{' + Vol_m_str + r'}{in^3} \\ \\' + '\n\t\t'
latex += r'\text{Combustion gas constant of black powder:}& &R &= 265.92 \frac{in \cdot lbf}{lbm \cdot \SI{}{\degree R}} \\ \\' + '\n\t\t'
latex += r'\text{Combustion gas temperature of black powder:}& &T_{c} &= 3307 \: \SI{}{\degree R} \\ \\' + '\n\t\t'
latex += r'\text{Ejection pressure equation: }& &P_{e} &= \left( m_{bp} \cdot \frac{\SI{1}{lbf}}{\SI{454}{g}} \right) \cdot \frac{R \cdot T_{c}}{Vol_{S}} \tag{eqn. 15} \\ \\' + '\n\t\t' 
latex += r'\text{Force applied to bulkheads equaton:}& &F_{e} &= P_{e} \cdot A_{bh} \tag{eqn. 16} \\ \\' + '\n\t\t'
latex += r'\text{Black powder charge mass for drogue chute bay:}& &m_{bp,d} &= \SI{2.5}{g} \\' + '\n\t\t'
latex += r'	\text{Ejection pressure for drogue chute:}& &P_{e,d} &= \left(\SI{2.5}{g} \cdot \frac{1 lbf}{454 g} \right) \cdot \frac{265.92 \frac{in \cdot lbf}{lbm \cdot  \SI{}{\degree R}} \cdot 3307 \SI{}{\degree R}}{' + Vol_d_str + r'} \\ \\' + '\n\t\t'
latex += r'&& &= \SI{' + P_e_d_str + r'}{psi} \\ \\' + '\n\t\t'
latex += r'\text{Force applied to drogue chute bay bulkheads:}& &F_{e,d } &= P_{e} \cdot A_{bh} \\' + '\n\t\t'
latex += r'&& &= ' + P_e_d_str + r'\cdot ' + A_bh_str + r'\\' + '\n\t\t'
latex += r'&& &= \SI{' + F_e_d_str + r'}{lbs} \\ \\' + '\n\t\t'

latex += r'\text{Black powder charge mass for main chute bay:}& &m_{bp,m} &= \SI{5}{g} \\' + '\n\t\t'
latex += r'	\text{Ejection pressure for main chute:}& &P_{e,m} &= \left(\SI{5}{g} \cdot \frac{1 lbf}{454 g} \right) \cdot \frac{265.92 \frac{in \cdot lbf}{lbm \cdot  \SI{}{\degree R}} \cdot 3307 \SI{}{\degree R}}{' + Vol_m_str + r'} \\ \\' + '\n\t\t'
latex += r'&& &= \SI{' + P_e_m_str + r'}{psi} \\ \\' + '\n\t\t'
latex += r'\text{Force applied to main chute bay bulkheads:}& &F_{e,d } &= P_{e} \cdot A_{bh} \\' + '\n\t\t'
latex += r'&& &= ' + P_e_m_str + r'\cdot ' + A_bh_str + r'\\' + '\n\t\t'
latex += r'&& &= \SI{' + F_e_m_str + r'}{lbs} \\ \\' + '\n\t\t'

# Vent Hole Calculations

# Main Chute Opening Force Calculation
latex += r'% Main Chute Opening Force Calculation' + '\n\t\t'
latex += r'\textbf{Main Chute Opening Force Calculation} \\' + '\n\t\t'
latex += r'\text{Descent velocity before main chute opening:}& &V_{i} &= \SI{' + v_i_str + r'}{ft/s} \\ \\' + '\n\t\t'
latex += r'\text{Descent velocity after main chute opening:}& &V_{f} &= \SI{' + v_f_str + r'}{ft/s} \\ \\' + '\n\t\t'
latex += r'\text{Main chute opening time:}& &t_{infl} &= \SI{' + t_infl_str + r'}{s} \\ \\' + '\n\t\t'
latex += r'\text{Main Chute Opening Force Equation:}& &F_{max} &= \left( \frac{2 \cdot m \cdot v_{i}}{g \cdot t_{infl}} \right) \left( 1 - \frac{v_f}{v_i} \right) + 2 \cdot m \tag{eqn. 16} \\' + '\n\t\t'
latex += r'&& &= \left( \frac{2 \cdot ' + m_str + r' \cdot ' + v_i_str + r'}{' + grav_str + r'\cdot ' + t_infl_str + r'} \right) \left( 1 - \frac{' + v_f_str  +r'}{' + v_i_str + r'} \right)' + r' + 2 \cdot' + m_str + r'\\'
latex += r'&& &= \SI{' + chute_F_max_str + r'}{lbf} \\'

# latex += r'\\' + '\n\t\t'

#footer
latex += '\n\t'
latex += r'\end{align*}' + '\n'
latex += r'\end{document}'


# print(latex)
with open('output.tex', 'w') as file:
    file.write(latex)

with open('output.tex', 'r') as file:
    latex_content = file.read()
