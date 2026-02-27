"""
UNAM - Facultad de Ciencias
"""
# -*- coding: utf-8 -*-
import matplotlib,matplotlib.pyplot,math
redondear=3
g=9.81 #m/s^2
gr=1.5
grafx,grafy=12,11
color_letras_graf="#404040"
matplotlib.style.use("default")
matplotlib.rcParams["figure.figsize"]=(grafx*gr, grafy*gr)
matplotlib.rcParams["axes.labelsize"]=(10*gr)
matplotlib.rcParams["xtick.labelsize"]=(10*gr)
matplotlib.rcParams["ytick.labelsize"]=(10*gr)
matplotlib.rcParams["figure.facecolor"]="#ffffff"
matplotlib.rcParams["xtick.color"]=color_letras_graf
matplotlib.rcParams["ytick.color"]=color_letras_graf
matplotlib.rcParams["axes.facecolor"]="silver"
matplotlib.rcParams["grid.color"]="gainsboro"
matplotlib.rcParams["grid.linestyle"]="dashed"
matplotlib.rcParams["axes.grid"]=True
def tex_list(tex):
    lista="["
    for c in tex:
        if c=="":
            lista=lista+","
        else:
            lista=lista+c
    return(eval(lista+"]"))

def min_cuad(list_x,list_y,redondear):
    n=len(list_x)
    if n!=len(list_y):
        print("Error, las listas no coinciden.")
        raise ValueError
    sum_x=sum(list_x)
    sum_y=sum(list_y)
    prom_x=sum_x/n
    prom_y=sum_y/n
    sum_xy=0
    sum_x2=0
    sum_dx2=0
    sum_dy2=0
    sum_dxdy=0
    for k in range(n):
        x=list_x[k]
        y=list_y[k]
        sum_xy+=x*y
        sum_x2+=x**2
        dx=x-prom_x
        dy=y-prom_y
        sum_dx2+=dx**2
        sum_dy2+=dy**2
        sum_dxdy+=(dx*dy)
    s2=sum_dx2/n
    div=n*sum_x2-(sum_x)**2
    m=((sum_xy)-((sum_x)*(sum_y)/n))/(sum_x2-((sum_x**2)/n))
    b=prom_y-m*prom_x
    r2=sum_dxdy**2/(sum_dx2*sum_dy2)
    dm=math.sqrt( n*s2/div )
    db=math.sqrt( s2*sum_x2/div )
    return(round(m,redondear),round(b,redondear),round(dm,redondear+1),round(db,redondear+1),r2)
def graf_dot(x_y,list_x,list_y,color_dot_graf,tam,etiqueta=None):
    global gr   
    x_y.scatter(list_x,list_y,s=tam*gr,color=color_dot_graf,label=etiqueta)
def graf_rect(x_y,ti,tf,m,b,color,style,linewidth,etiqueta=None):
    x_y.plot([ti,tf],[m*ti+b,m*tf+b],color=color,linestyle=style, linewidth=linewidth,label=etiqueta)
def graf(list_x,list_y,redondear,liquido):
    global color_letras_graf
    m,b,dm,db,r2=min_cuad(list_x,list_y,redondear)
    """fig, x_y = matplotlib.pyplot.subplots()
    matplotlib.pyplot.suptitle(f"Presión {liquido}",color=color_letras_graf, fontweight='regular', fontsize=gr*21, fontname="Cambria")
    matplotlib.pyplot.title(f"P(h) = ({m}±{dm}) h + {b}",color="#575757", fontweight='normal', fontsize=gr*16, fontname="Cambria")
    matplotlib.pyplot.xlabel("Profundidad [m]",color=color_letras_graf, fontweight='light',size=gr*16, fontname="Cambria")
    matplotlib.pyplot.ylabel(f"P(h) [kg/m^2]",color=color_letras_graf, fontweight='light',size=gr*16, fontname="Cambria")
    graf_dot(x_y,list_x,list_y,"#9e0035",20) #,etiqueta="Experimental")
    graf_rect(x_y,min(list_x),max(list_x),m,b,"#b5762a","solid",4) #,etiqueta="Media")
    #x_y.legend(loc='lower left', fontsize=gr*10)#, fontname="Cambria")
    matplotlib.pyplot.show()"""
    return(m,dm,r2)
def densidad(liquido,ρ_teorico,L,h):
    global g,redondear
    ρ_m=1000.84 #kg/m^3
    n=len(L)
    if n!=len(h):    
        print(f"\n\nLas listas en {liquido} no coinciden.\n\n")
        return()     
    P=[0]
    hg=[0]
    for l in L:  
        P.append(ρ_m*l/100)   
    for l in h:  
        hg.append(l/100)
    m,dm,r2=graf(hg,P,redondear,liquido)
    dif=round(abs(1-m/ρ_teorico)*100,redondear)
    return([liquido,m,dm,ρ_teorico,dif])
def valores_1(lista):
    liquido,ρ,ρm,ρ_teorico,dif=lista[0],lista[1],lista[2],lista[3],lista[4]
    print(f"\nPara {liquido} se obtuvo ρ={ρ}±{ρm} kg/m^3.\nTeniendo un coeficiente de determinación igual a {round(ρm,redondear)}")
    print(f"El valor teórico es de {ρ_teorico} kg/m^3, con una diferencia porcentual de {dif}%.")
def valores_2(lista):
    liquido,ρ,ρm,ρ_teorico,dif=lista[0],lista[1],lista[2],lista[3],lista[4]
    print(f"{liquido}x{ρ}±{ρm}x{ρ_teorico}x{dif}")
Aceite_Oliva=densidad("Aceite de Oliva",916,tex_list("1.5, 16.5, 15.7"),tex_list("1.6, 4, 5.8, 7.8, 9.8, 12.1, 14.1, 16.3, 18.2, 17.1"))
Acetona=densidad("Acetona",789.059,tex_list("1.4, 3.1, 5.1, 6.3, 8.1, 9.1, 11.2, 13.1, 14.2, 16.1"),tex_list("1.2, 3.2, 6, 7.9, 9.9, 11.8, 13.8, 15.8, 17.8, 19.6"))
Alcohol=densidad("Alcohol",786.907,tex_list("0.9, 2.4, 4, 5.7, 7.7, 9.8, 10.8, 12.8, 14.8, 15.9"),tex_list("0.6, 2.4, 4.5, 6.6, 8.5, 10.4, 12.6, 14.4, 16.5, 17.9"))
Shampoo=densidad("Shampoo",1093,tex_list("1.1, 1.4, 3.5, 4.9, 5.4"),tex_list("0.8, 2.1, 3.9, 5.9, 8.5"))
Agua=densidad("Agua",1000.84,tex_list("1, 3.1, 5.1, 7.2, 8.3, 10.3, 12.1, 14.1, 16.1, 17.2"),tex_list("1.3, 3.2, 4.8, 6.5, 8.6, 10.2, 12.2, 13.9, 15.8, 17.7"))

valores_1(Aceite_Oliva)
valores_1(Acetona)
valores_1(Alcohol)
valores_1(Shampoo)
valores_1(Agua)
print(f"\nLíquidoxMedidoxTeóricoxDiferencia")
valores_2(Aceite_Oliva)
valores_2(Acetona)
valores_2(Alcohol)
valores_2(Shampoo)
valores_2(Agua)