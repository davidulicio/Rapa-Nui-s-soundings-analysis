%% Loading data
load('seriesmensuales.mat'); s = seriesmensuales;
clear seriesmensuales
% Species
co = s(1,:)'; co2 = s(2,:)'; e = s(3,:)'; p = s(4,:)'; np = s(5,:)'; 
nb = s(6,:)'; mp = s(7,:)'; mb = s(8,:)'; oz = s(9,:)';
clear s
%% Carbon Monoxide - CO 
Numb = 1; Sc = 2; sname = 'CO';
years1 = 2006 ; mes1 = 01 ; dia1 =01 ; hora1 = 1;
DD1 = [years1 mes1 dia1 hora1 0 0];
years2 = 2016 ; mes2 = 12 ; dia2 =01 ; hora2 = 23 ;
DD2 = [years2 mes2 dia2 hora2 0 0];
Mensual = co;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
%Mensual = Mobs_smo(:,3) ;
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea
%% Carbon Dioxide - CO2
Sc = 1; sname = '{CO}_{2}';
Mensual = co2;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea
%% Ethane 
Sc = 3; sname = 'Ethane';
Mensual = e;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea
%% Propane
Sc = 3; sname = 'Propane';
Mensual = p;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea
%% n-pentane
Sc = 3; sname = 'n-pentane';
Mensual = np;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea

%% n-butane
Sc = 3; sname = 'n-butane';
Mensual = nb;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea
%% Methylpropane
Sc = 3; sname = 'Methylpropane';
Mensual = mp;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea
%% Ethane 
Sc = 3; sname = 'Methylbutane';
Mensual = mb;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea
%% Tropospheric ozone - TO3
Sc = 2; sname = 'Ozone';
Mensual = oz;
linearfittype1 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)',...
    'sin(4*x*pi/12)','cos(4*x*pi/12)','sin(6*x*pi/12)',...
    'cos(6*x*pi/12)','x','1'});
linearfittype2 = fittype({'sin(2*x*pi/12)','cos(2*x*pi/12)','1'});

fecha=[datenum(DD1):datenum(0,0,0,1,0,0):datenum(DD2)]'; 
fechavec=datevec(fecha);
auxprom = nanmean(Mensual(:,Numb));
Mensual(isnan(Mensual)) = auxprom;
%%%%% Interpolacion %%%%%%%%  
largo = length(Mensual(:,:))/12;
Numb =1 ;
cont = largo*12 ;

for i=1:largo
    if      i==1      ; fou1        = {fit((1:12+6)',Mensual(1:12+6,Numb),linearfittype2)}                ; 
    elseif  i==largo  ; fou1(largo) = {fit((1:12+6)',Mensual(end-11-6:end,Numb),linearfittype2) }         ; 
    else                fou1(i)     = {fit((1:12+6)',Mensual((i-1)*12+1-3:(i)*12+3,Numb),linearfittype2)} ; 
    end
end

for i=1:length(fou1)
[Max1(i), Pos1(i)]  = max(coeffvalues(fou1{i})) ;
end
[Max2, Pos2 ]  = max(Max1);                

fouW  = fit((1:largo*12)',Mensual(:,Numb),linearfittype1); 
fou   = fouW(1:cont) - fouW.g*(1:cont)' - (Mensual(:,Numb)-fouW(1:cont)); 

fou1 = fou1{Pos2};
fou2 = fou(1:cont)-fou1(1:cont);
Res  = Mensual(:,Numb)-fouW(1:cont);

dataset = fit((1:length(fou2))',fou2,'poly1');

aut   = autocorr(Mensual(:,:),1);
Tiao  = (1-aut(2))^-(1/2)*std(Res)*0.023/12;
% Figure
ploteas = {fouW(1:cont) , fou1(1:cont) , fou2 ,fouW.g*(1:cont)',Res};plotea
