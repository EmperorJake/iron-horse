import global_constants
from train import LivestockConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = LivestockConsist(roster='pony',
                               base_numeric_id=1010,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = LivestockConsist(roster='pony',
                               base_numeric_id=1020,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=35,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = LivestockConsist(roster='pony',
                               base_numeric_id=1030,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=12,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    #--------------- llama ----------------------------------------------------------------------
    consist = LivestockConsist(roster='llama',
                               base_numeric_id=1040,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=25,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = LivestockConsist(roster='llama',
                               base_numeric_id=1430,
                               gen=2,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = LivestockConsist(roster='llama',
                               base_numeric_id=1050,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = LivestockConsist(roster='llama',
                               base_numeric_id=1520,
                               gen=2,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=35,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    #--------------- antelope ----------------------------------------------------------------------
    consist = LivestockConsist(roster='antelope',
                               base_numeric_id=1720,
                               gen=1,
                               subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = LivestockConsist(roster='antelope',
                               base_numeric_id=2150,
                               gen=1,
                               subtype='A',
                               track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)
