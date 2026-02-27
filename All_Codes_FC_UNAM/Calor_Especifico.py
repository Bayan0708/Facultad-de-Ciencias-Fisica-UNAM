def calor_especifico(Material,c_1,m_1,T_1,T_2,T_f,m_2,unit_c):
 m_T=294.4
 m_1=m_1-m_T
 δ_M=.1
 δ_m=.05
 δ_T2=.05
 δ_T=0.5
 δ_τ=0.05
 c_2=(c_1*m_1*(T_f-T_1))/(m_2*(T_2-T_f))
 a,δ_a,b,δ_b=m_1,δ_M,T_f-T_1,2*δ_T
 c,δ_c,d,δ_d=m_2,δ_m,T_2-T_f,δ_τ+δ_T
 a,δ_a,b,δ_b=a*b,a*δ_b+b*δ_a,c*d,d*δ_c+c*δ_d
 D=c_1/(b**2-(δ_b)**2)
 c_2,δ_c_2=D*(a*b-δ_a*δ_b),D*(b*δ_a-a*δ_b)
 c_2,δ_c_2=round(c_2,3),round(δ_c_2,3)
 print(f"El calor específico de {Material} es {c_2}±{δ_c_2} [{unit_c}/°C g]")
c_1=1
calor_especifico("Latón",c_1,534.6,22,91.5,26,183.2,"cal")
calor_especifico("Aluminio",c_1,523.0,22,91.4,25,59.8,"cal")
calor_especifico("Cobre",c_1,525.7,20,91.3,22,61.6,"cal")
c_1=4.182
calor_especifico("Latón",c_1,534.6,22,91.5,26,183.2,"J")
calor_especifico("Aluminio",c_1,523.0,22,91.4,25,59.8,"J")
calor_especifico("Cobre",c_1,525.7,20,91.3,22,61.6,"J")
