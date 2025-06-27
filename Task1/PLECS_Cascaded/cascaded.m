%parameter system
Vin = 24;
Vout = 12;
R = 6;
fsw = 100e3;
perc_I = 20;
perc_V = 1;
Iout=Vout/R;
dI = (perc_I/100)*Iout;
dV = (perc_V/100)*Vout;

%duty cycle
D = Vout/Vin;
Ts = 1/fsw;

%inductance and capacitance
L = Vout * (1 - D) / (dI * fsw);
C = Vout * (1 - D) / (8 * dV * L * fsw^2);

% Kp and Ki
Fbp = fsw/20;     
Fbi = Fbp/10;    
Kp  = 2*pi*Fbp*C;
Ki  = 2*pi*Fbi*Kp;
