from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='intrepid',
                            base_numeric_id=4810,
                            name='Intrepid',
                            role='heavy_express',
                            role_child_branch_num=-1, # -ve because Joker
                            power=2200,
                            random_reverse=True,
                            gen=4,
                            fixed_run_cost_points=30, # give a bonus so this can be a genuine mixed-traffic engine
                            intro_date_offset=2,  # let's be a tiny bit later for this one
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=115, # bonus over Wyvern
                     vehicle_length=8,
                     spriterow_num=0)

    return consist