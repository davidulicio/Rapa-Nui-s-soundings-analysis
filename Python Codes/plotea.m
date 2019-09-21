%%%%% Paarameters for figure and panel size %%%%%%%%%%%%%%%
plotheight=20 ;   plotwidth=16  ;   subplotsx=1 ;   subplotsy=5;   
leftedge=1.6  ;   rightedge=0.4 ;   topedge=  1.3 ; bottomedge=1.2;
spacex=0.2    ;   spacey=0.4    ;   fontsize=5;
ylabb = {'ppmv' 'ppbv' 'pptv'};
ytrend = {'ppmv/decade' 'ppbv/decade' 'pptv/decade'};
xplot = datetime(num2str(years1),'inputformat','yyyy')+calmonths(0:cont-1);
    
sub_pos=subplot_pos(plotwidth,plotheight,leftedge,rightedge,bottomedge,...
    topedge,subplotsx,subplotsy,spacex,spacey);
%%%%  Setting the Matlab figure %%%%%%
f=figure('units','normalized','Position',[0 0 0.55 1],'visible','on');
clf(f);
set(gcf, 'PaperUnits', 'centimeters');
set(gcf, 'PaperSize', [plotwidth plotheight]);
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperPosition', [0 0 plotwidth plotheight]);
c = ['r' 'g' 'b' 'k' 'm' 'k' 'c' 'k' 'c' 'k' 'y' 'm' 'c' 'b' 'g' 'r'...
    'k' 'k' 'b'];
mtr = {'-sr' '-sg' '-sb' '-sk' '-sm' '-sr' '-sc' '-sm' '->c' '->g' '->b'...
    '->c' '->m' '->y' '->k' '->r'  '-^c' '-^m' '-^k' };
limyy = [min(Mensual(:,Numb)) max(Mensual(:,Numb)) ] ;

    for i =1:5
    ax=axes('position',sub_pos{1,5+1-i},'XGrid','off',...
        'XMinorGrid','off','Box','off','Layer','top'); 
    ylim(limyy)
    pos = Mensual(:,Numb)==auxprom;Numb ; 
    
    if i ==1     
    yplot = (ploteas{i}) ; Mensual(Mensual(:,Numb)==auxprom,Numb)= nan ;
    plot(xplot,Mensual(:,Numb),'o','MarkerSize',3,'MarkerEdgeColor',...
        'k','MarkerFaceColor','k') ; hold on  ; 
    plot(xplot,yplot,strjoin(mtr(i)),'LineWidth',1.2,'MarkerSize',...
        2.6,'MarkerEdgeColor',c(i),'MarkerFaceColor',c(i)) ;  
    ylabel( ylabb(Sc) ,'FontSize', 10)  ; set(ax,'xticklabel',[]) ;
    legend('Data' , 'Fourier') ;
    
    Type = ' (Model)'       ;
    title([sname Type],'FontSize',14) ;
    end 
    
    if i ==2
    yplot = (ploteas{i}) ;
    plot(xplot,yplot,strjoin(mtr(i)),'LineWidth',1.2,'MarkerSize',2.6,...
        'MarkerEdgeColor',c(i),'MarkerFaceColor',c(i)) ;  
    ylabel( ylabb(Sc) ,'FontSize', 10) ;   set(ax,'xticklabel',[]) ; 
    legend('First frequency ') ;
    end 
    
    if i ==3     
    yplot = (ploteas{i}) ;
    plot(xplot,yplot,strjoin(mtr(i)),'LineWidth',1.2,'MarkerSize',2.6,...
        'MarkerEdgeColor',c(i),'MarkerFaceColor',c(i)) ;  
    ylabel( ylabb(Sc) ,'FontSize', 10) ; set(ax,'xticklabel',[]) ;
    legend('Residual frequencies') ;

    end 
    
    if i ==4     
    yplot = (ploteas{i}) ;
    plot(xplot,yplot,'k','LineWidth',1.2) ;  
    ylabel( ylabb(Sc) ,'FontSize', 10)   ; set(ax,'xticklabel',[]) ;
    str = strcat('\beta =', num2str(round(fouW.g*12*10,3)), '\pm',...
        num2str(round(Tiao*12,3)), ' ', ytrend(Sc));
    legend(str);
   end 
    
    if i ==5     
    Res(pos) = nan ;
    yplot = (Res) ; 
    plot(xplot,yplot,'o','MarkerSize',2.6,'MarkerEdgeColor',c(i),...
        'MarkerFaceColor',c(i)) ;  
    ylabel( ylabb(Sc) ,'FontSize', 10)  
    legend('Noise')
    ylim([-40 40])
    end 
    end
%% Functions

function [ positions ] = subplot_pos(plotwidth,plotheight,...
    leftmargin,rightmargin,bottommargin,topmargin,nbx,nby,spacex,spacey)
 
    subxsize=(plotwidth-leftmargin-rightmargin-spacex*(nbx-1.0))/nbx;
    subysize=(plotheight-topmargin-bottommargin-spacey*(nby-1.0))/nby;
 
    for i=1:nbx
       for j=1:nby
 
           xfirst=leftmargin+(i-1.0)*(subxsize+spacex);
           yfirst=bottommargin+(j-1.0)*(subysize+spacey);
 
           positions{i,j}=[xfirst/plotwidth yfirst/plotheight ...
               subxsize/plotwidth subysize/plotheight];
 
       end
    end
end