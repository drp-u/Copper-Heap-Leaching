import matplotlib.pyplot as plt

def heap_leach():
    print('--Input Heap Data (assume 9m heap height and $15/ton operating costs)--')
    ore_mass = int(input('Enter the mass of the ore in tons: '))
    grade = float(input('Enter the grade of the ore: '))
    height = int(input('Choose the height of the heap in meters (3, 6, 9): '))
    metal_price_lb = float(input('Enter the market price of copper ($/lb): '))

    metal_price = metal_price_lb * 2000
    Total_Available_Cu = ore_mass * grade
    accumulated_profit = 0
    Cu_extracted_tally = 0
    yesterday_cum_Cu = 0
    yesterday_profit = 0
    total_profit = 0
    daily_op_cost = (ore_mass * 15)/365

    plot_days = []
    plot_profit =[]
    plot_copper =[]

    if height == 3:
        k = .31
        theta = 3.9
        R_max = 85.0
        n = .63
    if height == 6:
        k = .2
        theta = 7.87
        R_max = 75.23
        n = .84
    if height == 9:
        k = .26
        theta = 10.7
        R_max = 70.78
        n = .75

    for t in range(0 , 366):
        if t <= theta:
            R_today= 0
            today_cum_Cu = 0
            new_Cu_today = 0
        else:
            R_today = R_max * (1-(2.718281828 **(-(k * ((t - theta) ** n)))))
            today_cum_Cu = R_today * Total_Available_Cu
            new_Cu_today = today_cum_Cu - yesterday_cum_Cu

        if t>= theta:
            daily_rev = metal_price * new_Cu_today
            if daily_rev >= daily_op_cost:
                daily_profit = daily_rev - daily_op_cost
                Cu_extracted_tally += new_Cu_today
                total_profit += daily_profit
                plot_days.append(t)
                plot_profit.append(total_profit)
                plot_copper.append(Cu_extracted_tally)
            else:
                print(f'Shut down pumps on day {t}')
                break
        yesterday_cum_Cu = today_cum_Cu
    return plot_days, plot_profit, plot_copper, ore_mass, metal_price_lb, grade, daily_op_cost, height

def plot(plot_days, plot_profit, plot_copper, ore_mass, metal_price_lb, grade, daily_op_cost, height):
    copper_in_thousands = [x/1000 for x in plot_copper]
    profit_in_millions = [x/1000000 for x in plot_profit]
    last_copper = copper_in_thousands[-1]
    last_day = plot_days[-1]
    last_profit = profit_in_millions[-1]


    fig1, ax1 = plt.subplots()
    ax1.set_xlabel('Operating Time (Days)')
    ax1.set_ylabel('Total Copper Extracted (Thousands of Tons)')
    ax1.plot(last_day,last_copper, marker = 'o', ms = 8)
    ax1.plot(plot_days, copper_in_thousands, label = 'Cu Extracted')
    ax1.tick_params(axis='y')
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Total Profit (Millions of $)')
    ax2.plot(plot_days, profit_in_millions, label = 'Total Profit')
    ax2.annotate(
        f'Day {int(last_day)}',
        xy=(last_day, last_profit),
        xytext=(-15,-15),
        textcoords='offset points',
        fontweight='bold',
        fontsize=10
    )
    ax2.tick_params(axis='y')

    main_title = f'{height}m Copper Heap Leach Production Lifespan'
    subtitle = f'{int(ore_mass/1000)} thousand tons @ {grade*100}% grade | Price: \\${metal_price_lb}/lb Cu | OPEX: \\${int(daily_op_cost)}/day'
    plt.title(f'{main_title}\n{subtitle}', fontsize = 11)
    plt.show()

plot_days, plot_profit, plot_copper, ore_mass, metal_price, grade, daily_op_cost, height = heap_leach()
plot(plot_days, plot_profit, plot_copper, ore_mass, metal_price, grade, daily_op_cost, height)