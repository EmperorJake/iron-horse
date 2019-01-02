from train import EngineConsist, DieselEngineUnit

# deprecated Dec 2018
# - can't make the 16/8 length work in a way that fits power progression + fits buy menu
# - shorter lengths run up against problem that HSTs 'only look right with all lux cars', but then integer lengths fail

# no wagon attach cb should be used, let them eat cake etc.

consist = EngineConsist(id='scorcher',
                        base_numeric_id=2950,
                        name='Scorcher',
                        role='heavy_express_1',
                        power=4050,
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        dual_headed=True,
                        intro_date_offset=-2, # let's be a little bit earlier for this one
                        gen=5,
                        sprites_complete=False)

consist.add_unit(type=DieselEngineUnit,
                 weight=70,
                 vehicle_length=8,
                 spriterow_num=0)