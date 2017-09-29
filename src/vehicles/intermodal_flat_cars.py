import global_constants
from train import IntermodalConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = IntermodalConsist(roster='pony',
                                base_numeric_id=1060,
                                gen=3,
                                subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=40,  # was matched for some time to RH and Squid containers, but blah
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    #--------------- llama ----------------------------------------------------------------------
