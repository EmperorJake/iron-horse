from train import MailEngineConsist, MetroUnit

consist = MailEngineConsist(id='longwater',
                            base_numeric_id=290,
                            name='Longwater',
                            role='mail_metro',
                            track_type='METRO',
                            power=600,
                            type_base_buy_cost_points=36,  # dibble buy cost for game balance
                            intro_date=1900)

consist.add_unit(type=MetroUnit,
                 weight=35,
                 vehicle_length=8,
                 capacity=60,
                 spriterow_num=0)

consist.add_unit(type=MetroUnit,
                 weight=35,
                 vehicle_length=8,
                 capacity=60,
                 spriterow_num=1)

