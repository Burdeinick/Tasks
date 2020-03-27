import global_var as g_v
import my_functions as m_f


for number_str in range(g_v.n):
    in_str = input().split()  
    g_v.list_com.append(in_str)  
    m_f.call_fun(g_v.list_com[number_str][0], g_v.list_com[number_str][1], g_v.list_com[number_str][2]) 


for element_lst in g_v.itog_list:
    print(element_lst)
