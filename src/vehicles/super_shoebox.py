from train import EngineConsist, ElectroDieselEngineUnit

consist = EngineConsist(id='super_shoebox',
                        base_numeric_id=880,
                        name='Super Shoebox',
                        role='branch',
                        power=1100,
                        power_by_railtype={'RAIL': 1100, 'ELRL': 2200},
                        type_base_buy_cost_points=0,  # dibble buy cost for game balance
                        type_base_running_cost_points=-28,  # dibble run cost for game balance
                        random_reverse=True,
                        gen=5)

consist.add_unit(type=ElectroDieselEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)

