import global_constants
from train import Train, DieselLoco

vehicle = DieselLoco(id = 'dmc_sd40',
            numeric_id = 2350,
            title = 'DMC SD40 [Diesel]',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 90,
            power = 3000,
            weight = 170,
            vehicle_length = 8,
            buy_menu_width = 32,
            loading_speed = 20,
            intro_date = 1975,
            str_type_info = 'COASTER',
            vehicle_life = 30,
            graphics_status = '')

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
