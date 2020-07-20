from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='bone',
                            base_numeric_id=4820,
                            name='Bone',
                            role='heavy_freight',
                            role_child_branch_num=-1, # -ve because Joker
                            power=3300, # drops a bit on hp/speed from previous gen, but engine weight is lower
                            random_reverse=True,
                            intro_date_offset=-2,  # let's be a little bit earlier for this one
                            gen=5,
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=125, # tiny nerf from Grid, because IRL reasons
                     vehicle_length=8,
                     spriterow_num=0)

    return consist