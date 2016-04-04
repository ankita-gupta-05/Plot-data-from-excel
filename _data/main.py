import sqlite3,os
import xlrd,statistics,math
import matplotlib.pyplot as plt
import webbrowser

os.chdir('C:\Users\IBM_ADMIN\Desktop\cointribe')
wb=xlrd.open_workbook('./company_data.xlsx')

conn = sqlite3.connect('cointribe.db')
c = conn.cursor()

c.execute('CREATE TABLE if not exists excel (Company TEXT,param1 FLOAT,param2 FLOAT,param3 FLOAT,param4 FLOAT,param5 FLOAT,param6 FLOAT,param7 FLOAT,param8 FLOAT,param9 FLOAT,param10 FLOAT,Rating FLOAT,Month INTEGER,CRS  FLOAT)')

a1=7.1
a2=1.2
a3=3.1
a4=0.9
a5=4.5
a6=0.28
a7=0.56
a8=0.81
a9=1.6
a10=2
asum=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10

for j in range(0,wb.nsheets):
    sheet = wb.sheet_by_index(j)
    data=[[sheet.cell_value(r, coll) for coll in range(sheet.ncols)] for r in range(sheet.nrows)]
    #print j+1
    for i in range(2, 102):
        c.execute("INSERT INTO EXCEL (Company,param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,Month) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8],
             data[i][9], data[i][10], j+1))
        conn.commit()
        statement="UPDATE EXCEL SET Rating= ({0}* param1 + {1}* param2+ {2}* param3 +{3}* param4+{4}* " \
                  "param5+{5}* param6+{6}* param7+{7}* param8 + {8}* param9 + {9}* param10)/{10}".format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,asum)
        c.execute(statement)
        conn.commit()

print "Task 0 and 1 Done!!!!!"
statement="SELECT avg(Rating) from excel GROUP BY Month"
c.execute(statement)
mu=c.fetchall()
mu=[x[0] for x in mu]
#print mu

cdf=[]
for i in range(1,13):
    statement="SELECT Rating from excel where Month={0}".format(i)
    c.execute(statement)
    rating = c.fetchall()
    rating = [x[0] for x in rating]
    sigma=(statistics.stdev(rating))
    cdf.append([  0.5 * math.erf((-1*(x-mu[i-1])) / (math.sqrt(2)*sigma )) for x in rating])
    cdf[i-1]=[100 if x>1 else x*100 if x>0 else x*-100 for x in cdf[i-1]]
    #print cdf[i-1]
    for j in range(100):
        c.execute("UPDATE EXCEL SET CRS={0} WHERE Month={1} AND Company like 'Company{2}' ".format(cdf[i-1][j],i,j+1))
        #statement = "UPDATE EXCEL SET CRS={0} WHERE Month={1} AND Company={2}".format(cdf[i-1][j],i,j+1)
        conn.commit()

print "Task 2 Done!!!!!"

os.chdir('C:\Users\IBM_ADMIN\Desktop\cointribe\graphs')
for i in range(0,100):
    crs=[  x[i] for x in cdf ]
    fig = plt.figure()
    plt.xticks(range(13))
    plt.yticks(range(0,110,10))
    plt.plot(range(1,13),crs)
    plt.xlabel("Compmany relative Score")
    plt.title("Company {0}".format(i+1))
    fig.savefig("res{0}.png".format(i+1))
    plt.close(fig)
    #plt.show()

c.close()
conn.close()

path=os.getcwd()+'\home.html'
if not webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('file://' +path):
    webbrowser.open('file://' + a)


print "Task 3 Done!!!!!"