from src.Recipes.base_class import Recipe
from src.Recipes.variables import (cartesian_join_dict,union_change_dict,
                                   non_exist_to_left_dict,cte_merge_dict,cte_pre_agg_dict,magic_dict)


def appned_query_to_prompt(query, recipe):
        recipe_prompt = recipe.prompt
        updated_recipe_prompt = recipe_prompt + "\n Here is the query: " + query
        recipe.prompt = updated_recipe_prompt

def send_prompt_to_model(recipe):
