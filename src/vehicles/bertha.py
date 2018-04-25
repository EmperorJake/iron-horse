from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit

consist = EngineConsist(id='bertha',
                        base_numeric_id=70,
                        name='0-10-0 Big Bertha',
                        role='heavy_freight',
                        power=1800,
                        tractive_effort_coefficient=0.33,
                        type_base_buy_cost_points=10,  # dibble buy cost for game balance
                        gen=2)

consist.add_unit(type=SteamEngineUnit,
                 weight=95,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=SteamEngineTenderUnit,
                 weight=40,
                 vehicle_length=4,
                 spriterow_num=1)

