import global_constants
from train import OpenConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 820,
                          wagon_generation = 1,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 830,
                          wagon_generation = 2,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 840,
                          wagon_generation = 3,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 1450,
                          wagon_generation = 4,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'pony',
                          base_numeric_id = 850,
                          wagon_generation = 1,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                           capacity_freight = 12,
                           vehicle_length = 3))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 860,
                          wagon_generation = 1,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 1330,
                          wagon_generation = 2,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 870,
                          wagon_generation = 1,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'llama',
                          base_numeric_id = 1320,
                          wagon_generation = 2,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1760,
                          wagon_generation = 1,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1770,
                          wagon_generation = 2,
                          vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 70,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 2090,
                          wagon_generation = 1,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1830,
                          wagon_generation = 2,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = OpenConsist(title = '[Open Car]',
                          roster = 'antelope',
                          base_numeric_id = 1820,
                          wagon_generation = 3,
                          vehicle_life = 40,
                          track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])
